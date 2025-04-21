import json
from channels.generic.websocket import AsyncWebsocketConsumer
from aiortc import RTCPeerConnection, RTCSessionDescription
from aiortc.contrib.media import MediaPlayer

class VideoChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pc = None
        self.room_name = None
        self.room_group_name = None

    async def connect(self):
        # Get room name from the URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'video_chat_{self.room_name}'

        # Join the WebSocket group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Create the peer connection for the user
        self.pc = RTCPeerConnection()
        self.pc.on('iceconnectionstatechange', self.on_ice_connection_state_change)
        self.pc.on('datachannel', self.on_data_channel)

        # Set up local media (camera/audio)
        self.player = MediaPlayer('/dev/video0')  # Update with the correct path if necessary
        self.pc.addTrack(self.player.audio)
        self.pc.addTrack(self.player.video)

    async def disconnect(self, close_code):
        # Close the peer connection
        if self.pc:
            await self.pc.close()

        # Leave the group when the WebSocket is closed
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data['type']

        if message_type == 'offer':
            await self.handle_offer(data)
        elif message_type == 'answer':
            await self.handle_answer(data)
        elif message_type == 'candidate':
            await self.handle_candidate(data)

    async def handle_offer(self, data):
        offer = RTCSessionDescription(sdp=data['sdp'], type='offer')

        # Set remote offer description and create an answer
        await self.pc.setRemoteDescription(offer)
        answer = await self.pc.createAnswer()
        await self.pc.setLocalDescription(answer)

        # Send the answer back to the client
        await self.send(text_data=json.dumps({
            'type': 'answer',
            'sdp': self.pc.localDescription.sdp
        }))

    async def handle_answer(self, data):
        answer = RTCSessionDescription(sdp=data['sdp'], type='answer')

        # Set the remote description with the answer
        await self.pc.setRemoteDescription(answer)

    async def handle_candidate(self, data):
        candidate = data['candidate']

        # Add ICE candidates to the peer connection
        await self.pc.addIceCandidate(candidate)

    def on_ice_connection_state_change(self, state):
        print(f'ICE connection state: {state}')

    def on_data_channel(self, channel):
        # Handle incoming data channels if necessary
        pass
