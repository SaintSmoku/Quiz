from django.urls import path
from django.contrib import admin
from app_v2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Home page
    path('', views.index, name='index'),

    # Add user and view users
    path('adduser/', views.adduser, name='add_user'),

    # Delete user
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),

    # Assign leader to user
    path('assign_leader/', views.assign_leader, name='assign_leader'),

    # Update all users' leaders to null
    path('update_leader_null/', views.update_leader_null, name='update_leader_null'),

    # Team count view
    path('team_count/', views.team_count, name='team_count'),

    # Shuffle leader order
    path('shuffle_leader_order/', views.shuffle_leader_order, name='shuffle_leader_order'),

    # Quiz view
    path('quiz/', views.quiz, name='quiz'),

    # Subquiz details view
    path('subquiz/<int:subquiz_id>/', views.subquiz_detail, name='subquiz_detail'),

    # Show time for quiz
    path('show_time/<int:subquiz_id>/', views.show_time, name='show_time'),

    # Points calculation view
    path('point/', views.point, name='point'),

    # End game results view
    path('endgame/', views.endgame, name='endgame'),

    # Reset points
    path('reset/', views.reset, name='reset'),

    # Save data to Excel
    path('save_data_to_excel/', views.save_data_to_excel, name='save_data_to_excel'),
]
