import React from "react";
import axios from "axios";

function Upload(props) {
  function handleSubmit(event) {
    event.preventDefault();
    const fd = new FormData();
    fd.append("file", fileInput.current.files[0]);
    axios.post("http://localhost:3000/paintings_list", fd).then(() => {
      props.onUpload();
    });
  }

  function clearUploads() {
    axios.delete("http://localhost:3000/paintings_list").then(() => {
      props.onUpload();
    });
  }

  let fileInput = React.createRef();

  return (
    <div>
      <form encType="multipart/form-data" onSubmit={handleSubmit}>
        <input type="file" name="file" ref={fileInput} />
        <input type="submit" value="upload" />
      </form>
      <br />
      <hr />
      <br />
      <button onClick={clearUploads}>Clear uploads</button>
    </div>
  );
}

export default Upload;
