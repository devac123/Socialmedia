# chat/consumers.py
import asyncio
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from channels.consumer import AsyncConsumer
from channels.db import database_sync_to_async


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        print("--------------------connected with cosumer----------------------")
        # user_id = self.scope["session"]["_auth_user_id"]

        self.group_name = user_id
        print("------------------user id-------------------------")
        # Join room group

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        print("--------------------accepted---------------------")

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data=None,bytes_data = None):

        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Send message to room group
        await self.channel_layer.group_send(
            self.chat_group_name,
            {
                'type': 'recieve_group_message',
                'message': message
            }
        )
        print("---------connection-completed 1----------------")
    
    async def recieve_group_message(self, event):
        message = event['message']
        print("--------------------recieved-----------------------")
        # Send message to WebSocket
        print("--------------------sended-----------------------")
        await self.send(
             text_data=json.dumps({
            'message': message
        }))
        print("---------connection-completed----------------")