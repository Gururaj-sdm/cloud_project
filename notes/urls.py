from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.list_notes, name='list_notes'),
    path('add/', views.add_note, name='add_note'),
    path('delete/<int:id>/', views.delete_note),
    path('share/<int:id>/', views.share_note, name='share_note'),
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
]