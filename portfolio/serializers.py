from user.serializers import UserSerializerChat
from .models import Conversation, Message
from rest_framework import serializers
from user.serializers import UserDataChatSerializer
from user.models import User, UserData

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('conversation_id',)


class ConversationListSerializer(serializers.ModelSerializer):
    initiator = UserSerializerChat()
    receiver = UserSerializerChat()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['id', 'initiator', 'receiver', 'last_message']

    def get_last_message(self, instance):
        message = instance.message_set.first()
        if message:
            return MessageSerializer(instance=message).data
        else:
            return None

def get_user_chat(username):
    user = User.objects.filter(username=username).get()
    user_data = UserData.objects.filter(user_id=user.id).first()
    user_data_serializer = UserDataChatSerializer(user_data) if user_data else None

    if user_data_serializer:
        return user_data_serializer.data
    else: return None

class ConversationSerializer(serializers.ModelSerializer):
    initiator = UserSerializerChat()
    receiver = UserSerializerChat()
    message_set = MessageSerializer(many=True)

    class Meta:
        model = Conversation
        fields = ['id', 'initiator', 'receiver', 'message_set']

class ConversationSerializer1(serializers.ModelSerializer):
    initiator = UserSerializerChat()
    receiver = UserSerializerChat()
    message_set = MessageSerializer(many=True)
    initiator_chat = serializers.SerializerMethodField()  
    receiver_chat = serializers.SerializerMethodField()  

    class Meta:
        model = Conversation
        fields = ['id', 'initiator', 'receiver', 'message_set', 'initiator_chat', 'receiver_chat']

    def get_initiator_chat(self, obj):
        username = obj.initiator.username
        return get_user_chat(username)

    def get_receiver_chat(self, obj):
        username = obj.receiver.username
        return get_user_chat(username)

class ConversationListSerializer1(serializers.ModelSerializer):
    initiator = UserSerializerChat()
    receiver = UserSerializerChat()
    last_message = serializers.SerializerMethodField()
    initiator_chat = serializers.SerializerMethodField()  
    receiver_chat = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['id', 'initiator', 'receiver', 'last_message', 'initiator_chat', 'receiver_chat']

    def get_initiator_chat(self, obj):
        username = obj.initiator.username
        return get_user_chat(username)

    def get_receiver_chat(self, obj):
        username = obj.receiver.username
        return get_user_chat(username)

    def get_last_message(self, instance):
        message = instance.message_set.first()
        if message:
            return MessageSerializer(instance=message).data
        else:
            return None