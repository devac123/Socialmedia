from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    # path('register/' , views.index , name = 'home'),
    path('sign_up',views.sign_up,name='signup'),
    path('^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate_account, name='activate'),
    
    
    
]
