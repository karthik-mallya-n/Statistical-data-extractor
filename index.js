//--------------------------------Libraries---------------------------------------

const express = require("express");
const multer = require("multer");
const path = require("path");

//-------------spawning child process to run the python script-------------------

const { spawn } = require("child_process");

//------------------setting up app and port--------------------------------------

const app = express();
const port = 3000;

//-----------------------Multer for storing the uploads---------------------------

const storage = multer.diskStorage({
  destination: (req, file, cb) => {
    cb(null, path.join(__dirname, "uploads"));
  },
  filename: (req, file, cb) => {
    cb(null, file.originalname);
  },
});

const upload = multer({ storage: storage });

//------------------------setting up protocols-----------------------------
app.use(express.static(__dirname));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname ,"index.html"));
});

app.post("/upload", upload.single("csvFile"), (req, res) => {
  res.send("File uploaded successfully!");
});

//------------------------handling the python script------------------------

// Function to handle communication with Python script
function runPythonScript(callback) {
  const pythonProcess = spawn("python", ["analysis.py"]);
  let pyData;
  pythonProcess.stdout.on("data", (data) => {
    pyData = data;
    console.log(`Python script output: ${pyData}`);
  });

  pythonProcess.stderr.on("data", (data) => {
    pyData = data;
    console.error(`Error from Python script: ${pyData}`);
  });

  pythonProcess.on("close", (code) => {
    console.log(`Python script exited with code ${code}`);
    // Invoke the callback with the collected data
    callback(pyData);
  });
}
//--------------------setting up get protocol for retrieving the statistical data from the python script
app.get("/getData", (req, res) => {
  runPythonScript((data) => {
    res.json({ output: data });
  });
});

//-------------------keeping the server alive and running---------------

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
