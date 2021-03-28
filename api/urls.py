from django.urls import path
from .views import MessageList, MessageRetrieveAPIView,  MessageCreateAPIView


urlpatterns = [
    path('messages/list/<int:page>', MessageList.as_view()),
    path('messages/single/<int:pk>', MessageRetrieveAPIView.as_view()),
    path('messages/create/', MessageCreateAPIView.as_view()),
    # path('api/', include('api.urls')),
]