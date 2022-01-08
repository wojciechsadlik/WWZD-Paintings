import { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import axios from "axios";

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
        marker: { size: 8 },
      });
    }

    paintingsMap.get(painting.style).x.push(painting.x);
    paintingsMap.get(painting.style).y.push(painting.y);
  });

  if (paintingsMap.get("uploads") != undefined) {
    paintingsMap.get("uploads").marker.symbol = "x";
  }

  return Array.from(paintingsMap.values());
}

function PaintingsPlot(props) {
  const [paintings, setPaintings] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:3000/paintings_list").then((response) => {
      if (response.status == 200) {
        setPaintings(getPaintingsPlotData(response.data));
        props.onLoad();
      }
    });
  }, [props.isLoading]);

  if (props.isLoading) {
    return <div>L o a d i n g . . .</div>;
  } else {
    return (
      <div>
        <Plot data={paintings} layout={{ width: 1280, height: 960 }} />
      </div>
    );
  }
}

export default PaintingsPlot;
