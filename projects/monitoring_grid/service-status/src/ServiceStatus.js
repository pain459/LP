// src/ServiceStatus.js
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './ServiceStatus.css';

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

    // Set up interval to fetch data every 20 seconds
    const interval = setInterval(() => {
      fetchStatusData();
    }, 20 * 1000);

    // Clean up the interval on component unmount
    return () => clearInterval(interval);
  }, []);

  const getStatusClass = (status) => {
    switch (status) {
      case 'UP':
        return 'status-up';
      case 'DOWN':
        return 'status-down';
      case 'DEGRADED':
        return 'status-degraded';
      default:
        return '';
    }
  };

  return (
    <div>
      <h1>Service Status</h1>
      <p>Last Updated: {lastUpdated}</p>
      <table>
        <thead>
          <tr>
            <th>Service</th>
            <th>Genesis</th>
            <th>Dependents</th>
            <th>Potentials</th>
            <th>Impacted Dependents</th>
            <th>Impacted Potentials</th>
          </tr>
        </thead>
        <tbody>
          {Object.keys(statusData).map((service) => (
            <tr key={service}>
              <td>{service}</td>
              <td className={getStatusClass(statusData[service].genesis)}>
                {statusData[service].genesis}
              </td>
              <td className={getStatusClass(statusData[service].dependents)}>
                {statusData[service].dependents}
              </td>
              <td className={getStatusClass(statusData[service].potentials)}>
                {statusData[service].potentials}
              </td>
              <td className="impact-data">
                {statusData[service].impacted_dependents.join(', ')}
              </td>
              <td className="impact-data">
                {statusData[service].impacted_potentials.join(', ')}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ServiceStatus;
