import websockets
import json

async def send_message(message):
    async with websockets.connect("ws://logging:8765") as websocket:
        await websocket.send(json.dumps(message.__dict__).encode('utf-8'))
