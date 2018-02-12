from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from django.contrib.sitemaps.views import sitemap
from django.http.response import HttpResponseServerError
from django.shortcuts import render_to_response
from django.template import Context, loader
from rest_framework import routers
from Shelfie.views import api_home
from knox import views as knox_views
from Shelfie.views import LoginView

from ShelfieUser.views import login_redirect


def handler404(request):  # Handles page not found
    # You need to create a 500.html template.
    t = loader.get_template('404.html')
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))


def handler500(request):  # Handles server errors
    # You need to create a 500.html template.
    t = loader.get_template('500.html')
    return HttpResponseServerError(t.render(Context({
        'request': request,
    })))


def csrf_failure(request, reason=""):  # Expired CSRF Token
    ctx = {'message': 'some custom messages'}
    return render_to_response('./common/403.html', ctx)


'''
Django REST Frameworks Urls
'''
router = routers.DefaultRouter()

urlpatterns = [
    url(r'^api/v1/$', api_home,
        name='api_home'),
    url(r'^api/v1/login', LoginView.as_view(),
        name='knox_login'),
    url(r'^api/v1/logout', knox_views.LogoutView.as_view(),
        name='knox_logout'),
    url(r'^api/v1/logoutall', knox_views.LogoutAllView.as_view(),
        name='knox_logoutall'),
    url(r'^api/v1/', include('ShelfieUser.urls',
        namespace='ShelfieUser')),
    url(r'^api/v1/games', include('ShelfieGame.urls',
        namespace='ShelfieGame')),
    url(r'^api/v1/challenges/', include('ShelfieChallenge.urls',
        namespace='ShelfieChallenge')),
    url(r'^api/v1/posts', include('ShelfiePost.urls',
        namespace='ShelfiePost')),
    url(r'^api/v1/prizes', include('ShelfiePrize.urls',
        namespace='ShelfiePrize')),
    url(r'^api/v1/teams', include('ShelfieTeam.urls',
        namespace='ShelfieTeam')),
]
urlpatterns += [

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile', login_redirect, name='login_redirect'),
    url(r'^logout/$', logout, {'next_page': '/'}, name='logout'),

]
