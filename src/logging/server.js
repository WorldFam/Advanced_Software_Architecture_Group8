const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8765 });
const clients = new Set();

wss.on('connection', (ws) => {
  console.log('Client connected');

  clients.add(ws);

  ws.on('message', (message) => {
    console.log(`Received: ${message}`);

    clients.forEach((client) => {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(message)
        }
      }
    );
  });

  ws.on('close', () => {
    console.log('Client disconnected');
    
    clients.delete(ws);
  });

});

console.log('WebSocket server is running. Listening on ws://localhost:8765');
