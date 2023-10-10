from rest_framework import serializers

from conversation.models import Conversation, Message


class CreateConversationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversation
        fields = ['gpt_model']

    def save(self, **kwargs):
        conversation = Conversation(user=self.context['user'],
                                    gpt_model=self.validated_data['gpt_model'])
        conversation.save()
        return conversation


class GetConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        fields = '__all__'


class AddMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['conversation', 'role']

    def save(self, **kwargs):
        message = Message(conversation=self.validated_data['conversation'],
                          role=self.validated_data['role'])
        message.save()
        return message


class GetMessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = '__all__'
