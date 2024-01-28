import React, { useState } from 'react';
import './App.css';
import Meme from "./components/Meme"

function App() {
  const [memeList, setMemeList] = useState([]);
  const [loading, setLoading] = useState(false);
  const [splash, setSplash] = useState(["Loading..."])

  let splashes = [
    "Generating your meme...", 
    "Researching humor...", 
    "Performing standup comedy...", 
    "Pondering...", 
    "Analyzing human jokes...",
    "Generic loading splash...",
    "Procrastinating...",
    "Taking a break...",
    "Browsing iFunny...",
    "Distracting you...",
    "Meditating...",
    "Smelling the flowers...", 
    "Outsourcing creativity...",
    "Browsing CollegeHumor...", 
    "Debating syntax...", 
    "Watching grass grow...", 
    "Watching paint dry...",
    "Folding the dishes...",
    "Firing on all neurons...",
    "Losing sleep..."
  ]

  useState(() => {
    const interval = setInterval(() => {
      let random = Math.floor(Math.random() * splashes.length);
      setSplash(splashes[random]);
    }, 2000);

    return () => clearInterval(interval);
  }, []); 

  const requestDataFromBackend = () => {

    //setMemeList(memeList.concat(<Meme key={memeList.length} url={"https://static.wikia.nocookie.net/villainsfanon/images/4/4e/Troll-Face-Meme-PNG.png"} />));

    console.log("Button click")
    setLoading(true);

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

        setLoading(false);

      })
      .catch(error => {
        console.error('Error:', error);
        // Handle errors
      });
  };

  return (
    <div className="app-container container-fluid text-center flex-column h-100 m-0">

    <div className="position-absolute logo" >
      <img className="logo-img" src='memeify.png'></img>
    </div>

      <div className="title row justify-content-center">Memeify</div>
      <div className="row justify-content-center">
        <button className="button" onClick={requestDataFromBackend}>Generate meme!</button>
      </div>

      <div className="loading pt-1" style={{ visibility: loading ? "visible" : "hidden" }}>
        {splash}
      </div>

      <div className="row gallery mt-1">
        {memeList}
      </div>
    </div>
  );
}

export default App;
