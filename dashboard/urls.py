from django.urls import path
from dashboard import views
urlpatterns = [
    path('test/', views.test_view),
    path('home/', views.home, name='home')
]