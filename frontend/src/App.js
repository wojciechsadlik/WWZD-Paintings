import PaintingsPlot from "./components/PaintingsPlot";
import Upload from "./components/Upload";

function App() {
  return (
    <div className="App">
      <h1>Painting dataset visualisation</h1>

      <PaintingsPlot />
      <Upload />
    </div>
  );
}

export default App;
