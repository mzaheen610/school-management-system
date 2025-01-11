"""
Consumers for the messaging application.
"""

import json
from channels.generic.websocket import WebsocketConsumer

from . models import Message


class ChatConsumer(WebsocketConsumer):
    groups = ["school"]

    def connect(self):
        self.accept()
        self.send(text_data=json.dumps({
            'type':'connection_established',
            'message':'You are now connected!'
        }))

        chat_history = Message.objects.all().order_by('timestamp')
        for msg in chat_history:
            self.send(text_data=json.dumps({
                'type': 'chat_message',
                'message': msg.content,
                'sender': msg.sender.email,
                'timestamp': msg.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }))

    def receive(self, text_data=None):

        text_data_json = json.loads(text_data)
        message_content = text_data_json['message']
        print('Message:', message_content)

        sender = self.scope['user']

        message = Message.objects.create(
            sender=sender,
            receiver=sender,
            content=message_content
        )

        #To broadcast the message when a message is received

        self.channel_layer.group_send(
            'school',
            {
                'type': 'chat_message',
                'message': message_content,
                'sender': sender.email,
                'timestamp': message.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            }
        )

    def chat_message(self, event):
        message = event['message']
        sender = event['sender']
        timestamp = event['timestamp']

        self.send(text_data=json.dumps({
            'type': 'chat_message',
            'message': message,
            'sender': sender,
            'timestamp': timestamp
        }))