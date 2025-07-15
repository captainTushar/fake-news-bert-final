import React, { useState } from 'react';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState('');

  const handlePredict = async () => {
    const response = await fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    const data = await response.json();
    setResult(data.prediction);
  };

  return (
    <div className="App">
      <h1>Fake News Detector</h1>
      <textarea value={text} onChange={(e) => setText(e.target.value)} />
      <br />
      <button onClick={handlePredict}>Check News</button>
      <h2>Result: {result}</h2>
    </div>
  );
}

export default App;

