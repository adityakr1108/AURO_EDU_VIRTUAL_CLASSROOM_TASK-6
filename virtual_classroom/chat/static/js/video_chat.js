// chat/static/js/video_chat.js
const roomName = "{{ room_name }}";
const chatSocket = new WebSocket(
    'ws://' + window.location.host + '/ws/video_chat/' + roomName + '/'
);

chatSocket.onopen = function(e) {
    console.log('WebSocket connected');
};

// Receive message from WebSocket
chatSocket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    const message = data['message'];

    // Handle WebRTC signaling messages (SDP, ICE candidates)
    console.log(message);
};

// Send message through WebSocket
function sendMessage(message) {
    chatSocket.send(JSON.stringify({ 'message': message }));
}
