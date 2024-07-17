const express = require('express');
const WebSocket = require('ws');
const kafka = require('kafka-node');
const app = express();
const port = 8080;

const kafkaClient = new kafka.KafkaClient({ kafkaHost: 'kafka:9092' });
const producer = new kafka.Producer(kafkaClient);

app.get('/', (req, res) => {
  res.send('Kafka Chat Backend');
});

const wss = new WebSocket.Server({ port: 8081 });

wss.on('connection', (ws) => {
  ws.on('message', (message) => {
    producer.send([{ topic: 'chatroom-1', messages: message }], (err, data) => {
      if (err) console.error(err);
    });
  });

  const consumer = new kafka.Consumer(
    kafkaClient,
    [{ topic: 'chatroom-1' }],
    { autoCommit: true }
  );

  consumer.on('message', (message) => {
    ws.send(message.value);
  });
});

app.listen(port, () => {
  console.log(`Backend service running at http://localhost:${port}`);
});
