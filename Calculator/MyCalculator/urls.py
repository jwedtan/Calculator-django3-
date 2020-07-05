from django.urls import path

app_name= 'MyCalculator'

urlpatterns = [
    path('', views.HomePage.as_view()),
]
