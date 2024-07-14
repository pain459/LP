const { Pool } = require('pg');
const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
});

const saveActivity = async (activity) => {
  const client = await pool.connect();
  try {
    await client.query('INSERT INTO activities(data) VALUES($1)', [activity]);
  } finally {
    client.release();
  }
};

module.exports = {
  saveActivity,
};
