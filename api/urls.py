from django.urls import path
from api.views import SendTextView


urlpatterns = [
    path('send-text/', SendTextView.as_view(), name='name-text'),
]
