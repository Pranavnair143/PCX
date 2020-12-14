from django.urls import path
from .views import login_form,user_profile,profile_update


urlpatterns = [
    path('profile/',user_profile,name='u_profile'),
    path('update_p/',profile_update,name='upd_profile')
]