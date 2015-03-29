from django.conf.urls import patterns, include, url
from django.contrib import admin
from columbiastu import views

# Override the Admin Site header
admin.site.site_header = "Django Template Administration"

# Set the error handlers
handler403 = views.PermissionDeniedView.as_view()
handler404 = views.NotFoundView.as_view()
handler500 = views.ErrorView.as_view()

urlpatterns = patterns('',
    
    url(r'^$', views.IndexPage.as_view(), name='index'),
    url(r'^login/', views.LoginPage.as_view()),
    url(r'^logout/', views.LogoutView.as_view()),
    url(r'^post/new', views.NewPostView.as_view()),
    url(r'^signup/', views.SignupPage.as_view()),    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^profile/', views.ProfilePage.as_view()),
    url(r'^1/post/(?P<post_id>[A-Za-z0-9-_]+)', views.PostAPI.as_view())
)