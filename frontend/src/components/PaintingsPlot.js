import { useState, useEffect } from "react";
import Plot from "react-plotly.js";

function getPaintingsPlotData(paintings) {
  const paintingsMap = new Map();

  paintings.forEach((painting) => {
    if (!paintingsMap.has(painting.style)) {
      paintingsMap.set(painting.style, {
        x: [],
        y: [],
        name: painting.style,
        mode: "markers",
        type: "scatter",
      });
    }

    paintingsMap.get(painting.style).x.push(painting.x);
    paintingsMap.get(painting.style).y.push(painting.y);
  });

  return Array.from(paintingsMap.values());
}

function PaintingsPlot() {
  const [isLoading, setIsLoading] = useState(true);
  const [paintings, setPaintings] = useState([]);

  useEffect(() => {
    setIsLoading(true);
    fetch("http://localhost:3000/paintings_list")
      .then((response) => response.json())
      .then((data) => {
        setPaintings(getPaintingsPlotData(data));
        setIsLoading(false);
      });
  }, []);

  if (isLoading) {
    return <div>L o a d i n g . . .</div>;
  } else {
    return (
      <div>
        <Plot data={paintings} layout={{width: 1280, height: 960}}/>
      </div>
    );
  }
}

export default PaintingsPlot;
