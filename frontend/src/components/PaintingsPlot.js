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
  const colors = ["#3366cc", "#dc3912", "#ff9900", "#109618", "#990099",
    "#0099c6", "#dd4477", "#66aa00", "#b82e2e", "#316395",
    "#994499", "#22aa99", "#aaaa11", "#6633cc", "#e67300",
    "#8b0707", "#651067", "#329262", "#5574a6", "#3b3eac"]

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
        <Plot data={paintings} layout={{ width: 1280, height: 960, colorway: colors }}/>
      </div>
    );
  }
}

export default PaintingsPlot;
