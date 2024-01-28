import React, { useState } from 'react';
import './App.css';
import Meme from "./components/Meme"

function App() {
  const [memeList, setMemeList] = useState([]);

  const onGenBtnClick = event => {

    setMemeList(memeList.concat(<Meme key={memeList.length} />));
  };

  const requestDataFromBackend = () => {

    console.log("Button click")

    fetch('http://localhost:5000/button_press', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({}) // Send an empty JSON object as the body
    })
      .then(response => response.text()) // Parse the response as text
      .then(data => {
        console.log('Response from backend:', data);
        // Handle the response from the backend (which is a string)
      })
      .catch(error => {
        console.error('Error:', error);
        // Handle errors
      });
  };

  return (
    <div className="app-container container text-center flex-column h-100 p-0 pt-5">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
        integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
        crossOrigin="anonymous"
      />

      <div className="title row justify-content-center">Memeify</div>
      <div className="row justify-content-center">
        <button className="button" onClick={requestDataFromBackend}>Generate meme!</button>
      </div>

      <div className="row gallery mt-5">
        {memeList}
      </div>
    </div>
  );
}

export default App;
