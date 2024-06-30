// src/services/api.js
import axios from 'axios';

const API_URL = 'http://monitor:5000/status';

export const fetchServiceData = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error("Error fetching data", error);
    throw error;
  }
};
