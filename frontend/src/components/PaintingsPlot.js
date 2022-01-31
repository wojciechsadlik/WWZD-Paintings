import { useState, useEffect } from "react";
import Plot from "react-plotly.js";
import React, {Component} from 'react';
import Plotly from 'plotly.js/dist/plotly-cartesian';
import axios from "axios";
import createPlotlyComponent from 'react-plotly.js/factory';

import { render } from "react-dom";
import asdf from "react-plotly.js/factory";


function getPaintingsPlotData(paintings) {
  const paintingsMap = new Map();

  paintings.forEach((painting) => {
    if (!paintingsMap.has(painting.style)) {
      paintingsMap.set(painting.style, {
        x: [],
        y: [],
        name: painting.style,
        file_path: [],
        mode: "markers",
        type: "scatter",
        marker: { size: 8 },
      });
    }

    paintingsMap.get(painting.style).x.push(painting.x);
    paintingsMap.get(painting.style).y.push(painting.y);
    paintingsMap.get(painting.style).file_path.push(painting.file_path);
  });

  if (paintingsMap.get("uploads") != undefined) {
    paintingsMap.get("uploads").marker.symbol = "x";
  }

    //console.log([paintingsMap.values()]);
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



    let data = [paintings[0],paintings[1],paintings[2],paintings[3],paintings[4],paintings[5],paintings[6],
                paintings[7],paintings[8],paintings[9],paintings[10],paintings[11],paintings[12],paintings[13],
                paintings[14]]
    let layout = {width: 1280, height: 960,};


  if (props.isLoading) {
    return <div>L o a d i n g . . .</div>;
  } else {
    var Plot2 = createPlotlyComponent(Plotly);

    var elem = document.getElementById('root')
    const hoverInfo = document.createElement("newdiv")
    const newContent = document.createTextNode("");
    hoverInfo.appendChild(newContent);
    const rootDiv = document.getElementById("root");
    document.body.appendChild(hoverInfo, rootDiv);
    Plotly.newPlot('root', data, layout);

    elem.on('plotly_hover', function(data){
        var pn='',
              tn='',
              colors=[];
          for(var i=0; i < data.points.length; i++){
            pn = data.points[i].pointNumber;
            tn = data.points[i].curveNumber;

            var obj = paintings[tn].file_path
            var pic_name = obj[pn]
          };

        var infotext = data.points.map(function(d){


          return ("File_path: " +  pic_name);
        });

        hoverInfo.innerHTML = infotext.join('<br/>');
    })
     .on('plotly_unhover', function(data){
        hoverInfo.innerHTML = '';
    });

    return (
      rootDiv
    );
  }
}


export default PaintingsPlot;
