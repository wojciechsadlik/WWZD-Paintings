import { useState, useEffect } from "react";

function Plot() {
  const [isLoading, setIsLoading] = useState(true);
  const [paintings, setPaintings] = useState([]);

  useEffect(() => {
    setIsLoading(true);
    fetch("http://localhost:3000/paintings_list")
      .then((response) => response.json())
      .then((data) => {
        setIsLoading(false);
        setPaintings(data);
      });
  }, []);

  if (isLoading) {
    return <div>L o a d i n g . . .</div>;
  } else {
    const records = paintings.map((painting) => (
      <tr key={painting.id}>
        <td>{painting.id}</td>
        <td>{painting.x}</td>
        <td>{painting.y}</td>
        <td>{painting.style}</td>
      </tr>
    ));
    return (
      <div>
        <table>
          <thead>
            <tr>
              <th>id</th>
              <th>x</th>
              <th>y</th>
              <th>style</th>
            </tr>
          </thead>
          <tbody>{records}</tbody>
        </table>
      </div>
    );
  }
}

export default Plot;
