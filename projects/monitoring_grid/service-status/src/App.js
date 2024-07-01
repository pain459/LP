// src/App.js
import React from 'react';
import './App.css';
import ServiceStatus from './ServiceStatus';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ServiceStatus />
      </header>
    </div>
  );
}

export default App;
