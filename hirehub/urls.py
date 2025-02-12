from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.user_create, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/',views.users_logout, name='logout'),
    path('profile/setup/', views.profile_setup, name="profile_setup"),
    path('profile/',views.user_profile, name='profile'),
    path('update/<int:id>',views.profile_update, name='update'),
    path('delete/<int:id>',views.user_delete, name='delete'),
    path('about/',views.aboutus, name='about'),
    path('view/profile/<int:id>/',views.profile_view, name='profile-view'),
    path('main/',views.main_page,name='main_page'),
    path('search/', views.search_list, name='search'),
]