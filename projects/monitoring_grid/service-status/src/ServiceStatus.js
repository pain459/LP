import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './ServiceStatus.css';

const ServiceStatus = () => {
  const [statusData, setStatusData] = useState({});
  const [lastUpdated, setLastUpdated] = useState(null);
  // const apiUrl = process.env.REACT_APP_API_URL || 'http://172.19.0.4:5000/status';
  const apiUrl = process.env.REACT_APP_API_URL;


  useEffect(() => {
    const fetchStatusData = async () => {
      try {
        console.log('Fetching status data from API URL:', apiUrl);
        const response = await axios.get(apiUrl);
        console.log('Status data fetched successfully:', response.data);
        setStatusData(response.data.services);
        setLastUpdated(new Date().toLocaleString());
      } catch (error) {
        console.error('Error fetching status data:', error);
        if (error.response) {
          // Server responded with a status other than 2xx
          console.error('Response data:', error.response.data);
          console.error('Response status:', error.response.status);
          console.error('Response headers:', error.response.headers);
        } else if (error.request) {
          // Request was made but no response was received
          console.error('Request data:', error.request);
        } else {
          // Something happened in setting up the request
          console.error('Error message:', error.message);
        }
      }
    };

    // Fetch data immediately when the component mounts
    fetchStatusData();

    // Set up interval to fetch data every 20 seconds
    const interval = setInterval(() => {
      fetchStatusData();
    }, 20 * 1000);

    // Clean up the interval on component unmount
    return () => clearInterval(interval);
  }, [apiUrl]);

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
