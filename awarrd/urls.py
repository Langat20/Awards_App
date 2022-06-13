from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('search/', views.search_project, name='search'),
    path('project/<post>', views.project, name='project'),
    path('profile/<username>/', views.profile, name='profile'),
    path('<username>/profile', views.user_profile, name='userprofile'),
    path('profile/<username>/settings', views.edit_profile, name='edit'),
    #  path('api/v1/projects',views.ProjectList.as_view(),name='projectsEndpoint'),
    # re_path(r'^api/projects/$', views.ProjectList.as_view()),
    # re_path(r'^api/profiles/$', views.ProfileList.as_view()),
    # re_path(r'^api/users/$', views.UserList.as_view()),
    # re_path(r'api/Award/project-id/(?P<pk>[0-9]+)/$',
    #     views.ProjectDescription.as_view()),
]