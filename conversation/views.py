from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from conversation.models import Conversation, Message
from conversation.serializers import CreateConversationSerializer, GetConversationSerializer, AddMessageSerializer, \
    GetMessageSerializer


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_conversation(request):
    serializer = CreateConversationSerializer(data=request.data, context={'user': request.user})
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_conversation(request):
    conversations = Conversation.objects.filter(user=request.user)
    serializer = GetConversationSerializer(conversations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_conversation(request):
    conversation = Conversation.objects.get(id=request.data['id'])
    if 'summary' in request.data:
        conversation.summary = request.data['summary']
    conversation.save()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def delete_conversation(request):
    conversation = Conversation.objects.get(id=request.data['id'])
    conversation.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_message(request):
    serializer = AddMessageSerializer(data=request.data)
    if serializer.is_valid():
        message = serializer.save()
        if 'content' in request.data:
            message.content = request.data['content']
        elif 'image' in request.data:
            message.image = request.data['image']
        message.save()
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def get_message(request):
    messages = Message.objects.filter(conversation=request.data['conversation'])
    serializer = GetMessageSerializer(messages, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



