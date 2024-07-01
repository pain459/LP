// src/ServiceStatus.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const ServiceStatus = () => {
  const [statusData, setStatusData] = useState({});
  const [lastUpdated, setLastUpdated] = useState(null);

  const fetchStatusData = async () => {
    try {
      const response = await axios.get('http://localhost:5000/status');
      setStatusData(response.data.services);
      setLastUpdated(new Date().toLocaleString());
    } catch (error) {
      console.error('Error fetching status data:', error);
    }
  };

  useEffect(() => {
    // Fetch data immediately when the component mounts
    fetchStatusData();

    // Set up interval to fetch data every 20 minutes
    const interval = setInterval(() => {
      fetchStatusData();
    }, 20 * 60 * 1000);

    // Clean up the interval on component unmount
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h1>Service Status</h1>
      <p>Last Updated: {lastUpdated}</p>
      <table>
        <thead>
          <tr>
            <th>Service</th>
            <th>Dependents</th>
            <th>Genesis</th>
            <th>Potentials</th>
          </tr>
        </thead>
        <tbody>
          {Object.keys(statusData).map((service) => (
            <tr key={service}>
              <td>{service}</td>
              <td>{statusData[service].dependents}</td>
              <td>{statusData[service].genesis}</td>
              <td>{statusData[service].potentials}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ServiceStatus;
