
from django.urls import path
from authapp.views import LoginListView, RegisterListView, Logout, ProfileFormView

app_name = 'authapp'
urlpatterns = [
    path('login/', LoginListView.as_view(), name='login'),
    path('register/', RegisterListView.as_view(), name='register'),
    path('profile/', ProfileFormView.as_view(), name='profile'),
    path('', Logout.as_view(), name='logout'),
    path('verify/<str:email>/<str:activate_key>/',RegisterListView.verify,name='verify')
    ]

