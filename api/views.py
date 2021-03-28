from rest_framework import generics

from .models import Message
from .serializers import MessageSerializer


class MessageList(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        mes_set = 10 * self.kwargs['page']
        return Message.objects.all()[mes_set-10:mes_set]


class MessageRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageCreateAPIView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
