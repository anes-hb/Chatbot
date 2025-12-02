from django.urls import path
from .views import translate_text, summarize_text, chat

urlpatterns = [
    path('translate/', translate_text, name='translate'),
    path('summarize/', summarize_text, name='summarize'),
    path('chat/', chat, name='chat'),
]
