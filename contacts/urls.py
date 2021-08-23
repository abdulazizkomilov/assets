from django.urls import path
from .views import HomePageView, ContactFormView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contacts/', ContactFormView.as_view(), name='contactform'),
]