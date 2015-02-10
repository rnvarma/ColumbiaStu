import sys, datetime

from django.core.exceptions import PermissionDenied
from django.http import (HttpResponse, HttpResponseNotFound,
    HttpResponseBadRequest, HttpResponseServerError, HttpResponseRedirect)
from django.views.generic.base import View
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from backend.models import *
from backend.serializer import *

class ErrorView(View):
    """ HTTP 500: Internal Server Error """
    template_name = '500.html'
    status = 500
    
    def get(self, request):
        return render(request, self.template_name, status=self.status)
    
    
class PermissionDeniedView(ErrorView):
    """ HTTP 403: Forbidden """
    template_name = '403.html'
    status = 403
    
    
class NotFoundView(ErrorView):
    """ HTTP 404: Not Found """
    template_name = '404.html'
    status = 404
    
    
class NewPostView(TemplateView):
    """ the new post page"""
    template_name = "newPost.html"

    @method_decorator(login_required)
    def get(self, request):
        return render(request, self.template_name, {'user': request.user})

    def post(self, request):
        data = dict(request.POST)
        user = User.objects.get(username=str(request.user)).userdata
        topics = []
        for key in data:
            if "tag_" in key:
                if AreaTagModel.objects.filter(name=key[4:]).count():
                    topics.append(AreaTagModel.objects.get(name=key[4:]))
                else:
                    topic = AreaTagModel(name=key[4:])
                    topic.save()
                    topics.append(topic)
        title = data["title"][0]
        print "title after retrieve", title
        description = data["description"][0]
        if SchoolTagModel.objects.filter(name=data["college"]).count():
            college = SchoolTagModel.objects.get(name=data["college"][0])
        else:
            college = SchoolTagModel(name=data["college"][0])
            college.save()
        year = user.year
        if ClassTagModel.objects.filter(name=year).count():
            year = ClassTagModel.objects.get(name=year)
        else:
            year = ClassTagModel(name=year)
            year.save()
        post = PostModel(title=title, description=description,
                         date_submitted=datetime.datetime.now())
        post.save()
        print "title after save", post.title
        post.author.add(user)
        post.schoolTags.add(college)
        post.classTags.add(year)
        for topic in topics:
            post.areaTags.add(topic)
        return HttpResponseRedirect("/")


class IndexPage(TemplateView):
    """ The Index Page. """
    template_name = 'homePage.html'

    def get(self, request):
        return render(request, self.template_name, {'user': request.user})

class LoginPage(TemplateView):
    """ The Login Page. """
    template_name = 'accounts/login.html'

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(LoginPage, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'user': request.user})

    def post(self, request):
        data = dict(request.POST)
        username = data["username"][0]
        password = data["password"][0]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
        return HttpResponseRedirect("/login")

class LogoutView(TemplateView):
    """ the Logout Page"""

    def dispatch(self, *args, **kwargs):
        return super(LogoutView, self).dispatch(*args, **kwargs)

    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")

class ProfilePage(TemplateView):    
    """ The Profile Page """
    template_name = 'accounts/profile.html'

    def get(self, request):
	return render(request, self.template_name, {'user': request.user})
    
    def post(self, request):
        data = dict(request.POST)

class SignupPage(TemplateView):
    """ The Signup Page. """
    template_name = 'accounts/signup.html'

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(SignupPage, self).dispatch(*args, **kwargs)

    def get(self, request):
        return render(request, self.template_name, {'user': request.user})

    def post(self, request):
        data = dict(request.POST)
        pw = data["password1"][0]
        firstn, lastn = data["firstname"][0], data["lastname"][0]
        email = data["email"][0]
        year = int(data["year"][0])
        # create user object
        user = User.objects.create_user(email, email, pw)
        user.last_name = firstn + " " + lastn
        user.save()

        ud = UserData(user = user, year = year)
        ud.save()
        user_login = authenticate(username=email, password=pw)
        user_login.userdata = ud
        login(request, user_login)
        return HttpResponseRedirect("/")

class UserParser(object):

    @staticmethod
    def process_userdata_id(ud_id):
        user_info = {}
        userdata = UserData.objects.get(id=ud_id)
        user = userdata.user
        user_info["year"] = userdata.year
        user_info["is_admin"] = userdata.is_admin
        user_info["name"] = user.last_name
        user_info["email"] = user.email
        user_info["id"] = ud_id
        return user_info


class PostParser(object):

    objs_seen = {"classTags": {}, "schoolTags": {},
                 "areaTags": {}}

    post_cache = {}

    @staticmethod
    def process_post_id(p_id):
        if p_id in PostParser.post_cache:
            return PostParser.post_cache[p_id]
        post = PostModel.objects.get(id=p_id)
        data = PostSerializer(post).data
        processed_data = PostParser.process_post(data, post)
        PostParser.post_cache[p_id] = processed_data
        return processed_data

    @staticmethod
    def process_post(post, postObj):
        if post["id"] in PostParser.post_cache:
            return PostParser.post_cache[post["id"]]
        classTags, schoolTags, areaTags = [], [], []
        for class_id in post["classTags"]:
            if class_id in PostParser.objs_seen["classTags"]:
                classTags.append(PostParser.objs_seen["classTags"][class_id])
            else:
                classObj = ClassTagModel.objects.get(id=class_id)
                classTags.append(classObj.name)
                PostParser.objs_seen["classTags"][class_id] = classObj.name
        for sch_id in post["schoolTags"]:
            if sch_id in PostParser.objs_seen["schoolTags"]:
                schoolTags.append(PostParser.objs_seen["schoolTags"][sch_id])
            else:
                schoolObj = SchoolTagModel.objects.get(id=sch_id)
                schoolTags.append(schoolObj.name)
                PostParser.objs_seen["schoolTags"][sch_id] = schoolObj.name
        for area_id in post["areaTags"]:
            if area_id in PostParser.objs_seen["areaTags"]:
                areaTags.append(PostParser.objs_seen["areaTags"][area_id])
            else:
                areaObj = AreaTagModel.objects.get(id=area_id)
                areaTags.append(areaObj.name)
                PostParser.objs_seen["areaTags"][area_id] = areaObj.name
        post["classTags"] = classTags
        post["areaTags"] = areaTags
        post["schoolTags"] = schoolTags
        post["author"] = UserParser.process_userdata_id(post["author"][0])
        post["num_likes"] = postObj.likes.count()
        post["num_dislikes"] = postObj.dislikes.count()
        PostParser.post_cache[post["id"]] = post
        return post

class PostAPI(APIView):

    def get(self, request, post_id):
        return Response(PostParser.process_post_id(post_id))





