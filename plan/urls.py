from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registartionPage, name="registration"),
    path('', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('home/', views.homePage, name="home"),
    path('create_timetable/',views.createTimetable, name = "create_timetable"),
    path('update_timetable/<str:pk>/',views.updateTimetable, name = "update_timetable"),
    path('delete_timetable/<str:pk>/',views.deleteTimetable, name = "delete_timetable"),
    path('view/<str:pk>',views.timetableGeneralView, name = "timetable_view"),
    path('create_class/<str:pk>/',views.createClass, name ="create_class"),
    path('update_class/<str:pk>', views.updateClass, name = "update_class"),
    path('delete_class/<str:pk>', views.deleteClass, name="delete_class"),
    path('pdf/<str:pk>',views.render_to_pdf, name='viewPDF'),
]