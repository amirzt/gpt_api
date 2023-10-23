import requests
from django.http import StreamingHttpResponse
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from conversation.models import Conversation, Message, GPTModel
from conversation.serializers import CreateConversationSerializer, GetConversationSerializer, AddMessageSerializer, \
    GetMessageSerializer
from user.models import ApiKey


def get_chat_summary(data):

    # get summary
    api_key = ApiKey.objects.all().last().key
    openai_api_key = 'Bearer ' + api_key
    openai_url = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Authorization': openai_api_key,
        'Content-Type': 'application/json'
    }
    body = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "give me a short title for following question"
            },
            {
                "role": "system",
                "content": data['first_question']
            }

        ]
    }
    response = requests.post(openai_url, headers=headers, json=body, stream=False)
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return 'new conversation'


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_conversation(request):
    serializer = CreateConversationSerializer(data=request.data,
                                              context={'user': request.user,
                                                       'gpt_model': GPTModel.objects.get(
                                                           model_name=request.data['gpt_model'])})
    if serializer.is_valid():
        conversation = serializer.save()

        title = get_chat_summary(request.data)
        conversation.summary = title
        conversation.save()

        Message.objects.create(conversation=conversation,
                               role=Message.RoleChoices.user,
                               content=request.data['first_question'])

        return Response(status=status.HTTP_200_OK, data={
            'id': conversation.id
        })
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


@api_view(['POST'])
@permission_classes([AllowAny])
def send_message_to_gpt(request):
    api_key = ApiKey.objects.all().last().key
    openai_api_key = 'Bearer '+api_key
    openai_url = 'https://api.openai.com/v1/chat/completions'

    headers = {
        'Authorization': openai_api_key,
        'Content-Type': 'application/json'
    }

    response = requests.post(openai_url, headers=headers, json=request.data, stream=True)
    if response.status_code == 200:
        def stream_generator():
            for chunk in response.iter_content(chunk_size=8192):
                yield chunk
        return StreamingHttpResponse(stream_generator(), content_type=response.headers['Content-Type'])
    else:
        return Response(response.json(), status=response.status_code)

