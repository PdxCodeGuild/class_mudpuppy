"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import path,include
from login import views as login_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls'), name='home'),

    path('signup/', login_views.signup, name='signup'),


    
    path('signin/', auth.LoginView.as_view(template_name='login/login.html'), name='login'),
    path('signout/', auth.LogoutView.as_view(template_name='login/logout.html'), name='logout'),
    path('account/', login_views.account, name='account'),
    # path('blog/', include('main_app.urls'), name='blog'),
    path('', include('complaint.urls'), name="complaint")
    # path('signup/', include('login.urls'), name="signup")



    # path('signout/', auth.LogoutView.as_view(template_name='login/logout.html')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
