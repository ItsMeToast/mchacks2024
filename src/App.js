import React, { useState } from 'react';
import './App.css';
import Meme from "./components/Meme"

function App() {
  const [memeList, setMemeList] = useState([]);

  const requestDataFromBackend = () => {

    //setMemeList(memeList.concat(<Meme key={memeList.length} url={"https://static.wikia.nocookie.net/villainsfanon/images/4/4e/Troll-Face-Meme-PNG.png"} />));

    console.log("Button click")

    fetch('http://localhost:5000/button_press', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({}) // Send an empty JSON object as the body
    })
      .then(response => response.json())
      .then(data => {
        //console.log('Response from backend:', data);
        const returnedString = data.message

        //console.log('Response from backend:', returnedString);

        setMemeList(memeList.concat(<Meme key={memeList.length} url={returnedString} />));

      })
      .catch(error => {
        console.error('Error:', error);
        // Handle errors
      });
  };

  return (
    <div className="app-container container-fluid text-center flex-column h-100 p-0 pt-5">

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
