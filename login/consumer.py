from channels.generic.websocket import AsyncWebsocketConsumer
import json
class ChatConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        # user_id = self.scope["session"]["_auth_user_id"]
        # print(user_id)
        print("---------websocket-connected--------------")
        self.groupname = 'dashboard'
        await self.channel_layer.group_add(
            self.groupname,
            self.channel_name,
        )
        await self.accept()
        print("---------websocket-accepted--------------")
        
    async def disconnect(self,close_code):
        pass
        # await self.channel_layer.group_discard(
        #     self.group_name,
        #     self.channel_name
        # )

    async def receive (self,text_data=None,bytes_data = None):
        messages = json.loads(text_data)
        val = messages['value']
        await self.channel_layer.group_send(
            self.groupname,
            {
                'type':'deprocessing',
                'value':val
            }
        )
        print("textData",text_data)
        pass    
    async def deprocessing(self,event):
        valOther = event['value']
        await self.send(
            text_data=json.dumps({'value':valOther}))

