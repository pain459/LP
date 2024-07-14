const redis = require('redis');
const client = redis.createClient({
  url: process.env.REDIS_URL,
});

const cacheActivity = async (activity) => {
  client.incr('activity_count');
  client.set(`activity:${Date.now()}`, JSON.stringify(activity));
};

const getDashboardStats = async () => {
  const activityCount = await new Promise((resolve, reject) => {
    client.get('activity_count', (err, count) => {
      if (err) reject(err);
      resolve(count);
    });
  });
  return { activityCount };
};

module.exports = {
  cacheActivity,
  getDashboardStats,
};
