async function uploadAndGetData() {
  const form = document.getElementById("fileUploadForm");
  const formData = new FormData(form);

  try {
    const request = await fetch("http://localhost:5173/upload", {
      method: "POST",
      body: formData,
    });
    const message = await request.text();
    console.log(message);
  } catch (err) {
    console.error(err);
  }

  try {
    const response = await fetch("http://localhost:5173/getData");
    const data = await response.json();

    // Convert the Buffer data to a string using TextDecoder
    const textDecoder = new TextDecoder("utf-8");
    const decodedData = textDecoder.decode(
      new Uint8Array(data.output.data)
    );
    
    const dataContainer = document.getElementById("dataContainer");
    dataContainer.innerHTML = `<pre>${decodedData}</pre>`;

  } catch (err) {
    console.error(err);
  }
}

      async function resetForm() {
        const fileInput =
          document.getElementById("fileUploadForm").elements.csvFile;
        const fullPath = fileInput.value;
        const fileName = fullPath.split("\\").pop();
        const form = document.getElementById("fileUploadForm");
        form.reset();
        document.getElementById("dataContainer").innerHTML="No csv file uploaded";
        try {
          const response = await fetch(
            `http://localhost:5173/reset/${encodeURIComponent(fileName)}`
          );

          if (!response.ok) {
            console.error(`Error resetting file: ${response.statusText}`);
            return;
          }

          const reply = await response.text();
          console.log(reply);
        } catch (err) {
          console.error(err);
        }
      }

      window.addEventListener("beforeunload", resetForm);

      // Adjust margin-top dynamically when scrolling
      window.addEventListener("scroll", function () {
        const headerHeight = document.querySelector("header").offsetHeight;
        const navHeight = document.querySelector("nav").offsetHeight;
        const content = document.querySelector(".content");
        content.style.marginTop = headerHeight + navHeight + "px";
      });