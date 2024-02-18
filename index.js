//--------------------------------Libraries---------------------------------------

const express = require("express");
const multer = require("multer");
const path = require("path");
const fs = require("fs");
const cors = require("cors");
const bodyParser = require("body-parser");

//-------------spawning child process to run the python script-------------------

const { spawn } = require("child_process");

//------------------setting up app and port--------------------------------------
const port = 5173;

const app = express();
app.use(express.static(__dirname));
app.use(cors());
app.use(bodyParser.json());

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
//------------------------resetting middleware----------------------------

function totalReset(req, res, next) {
  //to delete uploaded file
  const fileDirectoryPath = path.join(__dirname, "uploads");

  fs.readdir(fileDirectoryPath, (err, files) => {
    if (err) {
      console.error(`Error reading directory: ${err}`);
      return;
    }

    for (let i = 0; i < files.length; i++) {
      const filePath = path.join(fileDirectoryPath, files[i]);
      if (files[i] == ".gitkeep") {
        continue;
      }
      // Deleting the file
      fs.unlink(filePath, (err) => {
        if (err) {
          console.error(`Error deleting file ${files[i]}: ${err}`);
        } else {
          console.log(`File ${files[i]} deleted successfully`);
        }
      });
    }
  });

  //to delete generated graphs
  const graphDirectoryPath = path.join(__dirname, "graphs");

  fs.readdir(graphDirectoryPath, (err, files) => {
    if (err) {
      console.error(`Error reading directory: ${err}`);
      return;
    }

    for (let i = 0; i < files.length; i++) {
      const filePath = path.join(graphDirectoryPath, files[i]);
      if (files[i] == ".gitkeep") {
        continue;
      }
      // Deleting the file
      fs.unlink(filePath, (err) => {
        if (err) {
          console.error(`Error deleting file ${files[i]}: ${err}`);
        } else {
          console.log(`File ${files[i]} deleted successfully`);
        }
      });
    }
  });
  next();
}

//------------------------setting up endpoints-----------------------------

app.get("/xtract", totalReset, (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/upload", upload.single("csvFile"), (req, res) => {
  console.log("file uploaded successfullly!");
  res.send("File uploaded successfully!");
});

app.get("/reset", totalReset);

//------------------------PYTHON SCRIPT ------------------------

// Function to handle communication with Python script
function runPythonScript(file, args, callback) {
  const pythonProcess = spawn("python", [file, ...args]);
  let pyData;

  pythonProcess.stdout.on("data", (data) => {
    pyData = data;
    //if you want to check the output in the logs
    //console.log(`Python script output: ${pyData}`);
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
//--------------------setting up get endpoint for retrieving the statistical data from the python script
app.get("/getData", (req, res) => {
  const attribute = req.query.attribute;
  const args = [attribute];
  runPythonScript("analysis.py", args, (pyData) => {
    res.json({
      output: pyData,
    });
  });
});

//--------------------setting up get endpoint for retrieving the graphs from the python script
app.post("/getGraph", (req, res) => {
  const selectedGraph = req.query.graph;
  const x = req.body.x;
  const y = req.body.y;
  const args = [selectedGraph, x, y];
  runPythonScript("graph.py", args, (pyData) => {
    res.json({
      path: pyData,
    });
  });
});

app.get("/getColumns", (req, res) => {
  const args = [];
  runPythonScript("columns.py", args, (pyData) => {
    res.send(pyData);
  });
});
//-------------------keeping the server alive and running---------------

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}/xtract`);
});
