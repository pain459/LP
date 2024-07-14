const express = require('express');
const bodyParser = require('body-parser');
const redis = require('./services/redisService');
const postgres = require('./services/postgresService');

const app = express();
app.use(bodyParser.json());

app.post('/activity', async (req, res) => {
  const activity = req.body;
  await postgres.saveActivity(activity);
  await redis.cacheActivity(activity);
  res.status(200).send('Activity recorded');
});

app.get('/dashboard', async (req, res) => {
  const stats = await redis.getDashboardStats();
  res.status(200).json(stats);
});

app.listen(5000, () => {
  console.log('Server is running on port 5000');
});
