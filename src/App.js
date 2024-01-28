import React, {useState} from 'react';
import './App.css';
import Meme from "./components/Meme"

function App() {
  const [memeList, setMemeList] = useState([]);

  const onGenBtnClick = event => {
    console.log("Button click")
    setMemeList(memeList.concat(<Meme key={memeList.length} />));
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
        <button className="button" onClick={onGenBtnClick}>Generate meme!</button>
      </div>

      <div className="row gallery mt-5">
        {memeList}
      </div>
    </div>
  );
}

export default App;
