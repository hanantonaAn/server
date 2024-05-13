from uuid import UUID
from channels.generic.websocket import WebsocketConsumer
import json
import base64
import secrets
from datetime import datetime

from asgiref.sync import async_to_sync
from django.core.files.base import ContentFile

from user.models import User
from .models import Message, Conversation
from .serializers import MessageSerializer

class EchoConsumer(WebsocketConsumer):
    def connect(self):
        print("here")
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )
        print("here2")
        self.accept()
        print("here3")

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data=None, bytes_data=None):
        # parse the json data into dictionary object
        text_data_json = json.loads(text_data)

        # unpack the dictionary into the necessary parts
        message, attachment = (
            text_data_json["message"],
            text_data_json.get("attachment"),
        )

        conversation = Conversation.objects.get(id=int(self.room_name))
        uuid_user = self.scope["user"]
        sender = User.objects.get(id=uuid_user)
        print("______SENDER____")
        print(uuid_user)
        # Attachment
        if attachment:
            file_str, file_ext = attachment["data"], attachment["format"]

            file_data = ContentFile(
                base64.b64decode(file_str), name=f"{secrets.token_hex(8)}.{file_ext}"
            )
            _message = Message.objects.create(
                sender=sender,
                attachment=file_data,
                text=message,
                conversation_id=conversation,
            )
        else:
            _message = Message.objects.create(
                sender=sender,
                text=message,
                conversation_id=conversation,
            )
        # Send message to room group
        chat_type = {"type": "chat_message"}
        message_serializer = (dict(MessageSerializer(instance=_message).data))
        return_dict = {**chat_type, **message_serializer}
        if _message.attachment:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "sender": sender.email,
                    "attachment": _message.attachment.url,
                    "time": str(_message.timestamp),
                },
            )
        else:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                return_dict,
            )

    # Receive message from room group
    def chat_message(self, event):
        dict_to_be_sent = event.copy()
        dict_to_be_sent.pop("type")

        # Преобразование UUID в строку перед сериализацией
        if isinstance(dict_to_be_sent.get("sender"), UUID):
            dict_to_be_sent["sender"] = str(dict_to_be_sent["sender"])

        # Send message to WebSocket
        self.send(
                text_data=json.dumps(
                    dict_to_be_sent
                )
            )

    # def connect(self):
    #     self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
    #     self.room_group_name = f"chat_{self.room_name}"

    #     # Join room group
    #     async_to_sync(self.channel_layer.group_add)(
    #         self.room_group_name, self.channel_name
    #     )
    #     self.accept()

    # def disconnect(self, close_code):
    #     pass

    # def receive(self, text_data):
    #     text_data_json = json.loads(text_data)
    #     message = text_data_json['message']

    #     self.send(text_data=json.dumps({
    #         'message': message,
    #         'resepient': "hi"
    #     }))