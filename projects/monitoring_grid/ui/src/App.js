// src/App.js
import React, { useEffect, useState } from 'react';
import { fetchServiceData } from './services/api';
import './App.css';

function App() {
  const [data, setData] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    console.log("Using API URL:", process.env.REACT_APP_API_URL || 'http://monitor:5000/status');
    const getData = async () => {
      try {
        const result = await fetchServiceData();
        console.log("Fetched Data: ", result);
        setData(result.services);
      } catch (err) {
        console.error("Error fetching data: ", err);
        setError(err.message || "Error fetching data");
      }
    };
    getData();
  }, []);

  const renderGrid = () => {
    if (!data) return null;

    const boxes = [];
    Object.keys(data).forEach(serviceKey => {
      const service = data[serviceKey];
      boxes.push(
        <div key={`${serviceKey}-dependents`} className={`box ${service.dependents.toLowerCase()}`}>
          {serviceKey} Dependents
        </div>
      );
      boxes.push(
        <div key={`${serviceKey}-genesis`} className={`box ${service.genesis.toLowerCase()}`}>
          {serviceKey} Genesis
        </div>
      );
      boxes.push(
        <div key={`${serviceKey}-potentials`} className={`box ${service.potentials.toLowerCase()}`}>
          {serviceKey} Potentials
        </div>
      );
    });

    return <div className="grid-container">{boxes}</div>;
  };

  return (
    <div className="App">
      <h1>Service Status Dashboard</h1>
      {error && <div className="error">Error: {error}</div>}
      {renderGrid()}
    </div>
  );
}

export default App;
