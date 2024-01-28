import './App.css';

function App() {
  return (
    <div class="app-container container text-center d-flex flex-column h-100 p-0 pt-5">
      <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css"
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
      crossorigin="anonymous"
    />

      <div class="title row justify-content-center">Memeify</div>
      <div class="row justify-content-center">
        <button class="button">Generate meme!</button>
      </div>
    </div>
  );
}

export default App;
