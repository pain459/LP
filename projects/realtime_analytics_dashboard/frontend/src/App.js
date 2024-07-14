import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [stats, setStats] = useState({ activityCount: 0 });

  useEffect(() => {
    fetch('/dashboard')
      .then(response => response.json())
      .then(data => setStats(data));
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>Real-Time Analytics Dashboard</h1>
        <p>Activity Count: {stats.activityCount}</p>
      </header>
    </div>
  );
}

export default App;
