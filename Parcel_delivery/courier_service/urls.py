from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home', views.home, name='home'),
    path('login',views.Login,name='login'),
    path('signup',views.signup,name='signup'),
    path('signupxtra',views.signupxtra,name='signupxtra'),
    path('About', views.About, name='About'),
    path('ContactUs', views.ContactUs, name='ContactUs'),
    path('Help', views.Help, name='Help'),
    path('place_parcel', views.place_parcel, name='place_parcel'),
    path('track_parcel', views.track_parcel, name='track_parcel'),
    path('estimate', views.estimate, name='estimate'),
    path('abc', views.abc, name='abc'),
    # path('user_profile', views.user_profile, name='user_profile'),
]
