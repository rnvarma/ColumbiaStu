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

from backend.models import *

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
        description = data["description"][0]
        if SchoolTagModel.objects.filter(name=data["college"]).count():
            college = SchoolTagModel.objects.get(name=data["college"][0])
        else:
            college = SchoolTagModel(name=data["college"][0])
            college.save()
        post = PostModel(title=title, description=description,
                         date_submitted=datetime.datetime.now())
        post.save()
        post.author.add(user)
        post.schoolTags.add(college)
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

def staff_only(view):
    """ Staff-only View decorator. """
    
    def decorated_view(request, *args, **kwargs):
        if not request.user.is_authenticated():
            return redirect_to_login(request.get_full_path())
            
        if not request.user.is_staff:
            raise PermissionDenied
            
        return view(request, *args, **kwargs)
        
    return decorated_view
    
    
