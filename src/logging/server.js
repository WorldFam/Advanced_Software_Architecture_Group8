const WebSocket = require('ws');

const wss = new WebSocket.Server({ port: 8765 });
const clients = new Set();

wss.on('connection', (ws) => {
  console.log('Client connected');

  // Add the new client to the set
  clients.add(ws);

  // Listen for messages from clients
  ws.on('message', (message) => {
    console.log(`Received: ${message}`);

    // Broadcast the message to all connected clients
    clients.forEach((client) => {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        // Check if the client is not the sender and is in the OPEN state
        client.send(`Broadcast: ${message}`);
      }
    });
  });

  // Handle connection close
  ws.on('close', () => {
    console.log('Client disconnected');
    
    // Remove the disconnected client from the set
    clients.delete(ws);
  });

  // Send a welcome message to the connected client
  ws.send('Welcome to the WebSocket server!');
});

console.log('WebSocket server is running. Listening on ws://localhost:8765');
