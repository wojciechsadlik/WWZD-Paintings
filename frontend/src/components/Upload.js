import React from "react";
import axios from "axios";

function Upload() {
  function handleSubmit(event) {
    event.preventDefault();
    console.log(fileInput.current.files[0]);
    const fd = new FormData();
    fd.append("file", fileInput.current.files[0]);
    axios.post("http://localhost:3000/paintings_list", fd);
  }

  let fileInput = React.createRef();

  return (
    <form encType="multipart/form-data" onSubmit={handleSubmit}>
      <input type="file" name="file" ref={fileInput} />
      <br />
      <input
        type="submit"
        value="upload"
      />
    </form>
  );
}

export default Upload;
