import { useState } from "react";
import PaintingsPlot from "./PaintingsPlot";
import Upload from "./Upload";

function PaintingsVisualisation() {
  const [isLoading, setIsLoading] = useState(true);

  function onPlotLoad() {
    setIsLoading(false);
  }

  function onUpload() {
    setIsLoading(true);
  }

  return (
    <div>
      <PaintingsPlot isLoading={isLoading} onLoad={onPlotLoad} />
      <Upload onUpload={onUpload} />
    </div>
  );
}

export default PaintingsVisualisation;
