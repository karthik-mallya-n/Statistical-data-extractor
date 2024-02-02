//--------------------------------Libraries---------------------------------------

const express = require("express");
const multer = require("multer");
const path = require("path");
const fs = require("fs");
const cors = require("cors");

//-------------spawning child process to run the python script-------------------

const { spawn } = require("child_process");
const { log } = require("console");

//------------------setting up app and port--------------------------------------
const port = 5173;

const app = express();
app.use(express.static(__dirname));
app.use(cors());

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

app.get("/xtract", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.post("/upload", upload.single("csvFile"), (req, res) => {
  console.log("file uploaded successfullly!");
  res.send("File uploaded successfully!");
});
//-----------------------reset protocol--------------------------------------
app.get("/reset/:uploadedFile", (req, res) => {
  const fileName = req.params.uploadedFile;
  const filePath = path.join("./uploads", fileName);

  if (fs.existsSync(filePath)) {
    fs.unlinkSync(filePath);
    console.log(`File ${fileName} removed successfully`);
    res.send("File removed successfully!");
  } else {
    console.log(`File ${fileName} not found`);
    res.status(404).send("File not found");
  }
  //    fs.writeFile(
  //      "extracts.html",
  //      "<center>no valid input available</center>",
  //      (err) => {
  //        if (err) {
  //          console.error(`Error writing file: ${err}`);
  //        } else {
  //          return;
  //        }
  //      }
  //    );
});

//------------------------handling the python script and writing the data into extracts.html------------------------

// Function to handle communication with Python script
function runPythonScript(callback) {
  const pythonProcess = spawn("python", ["analysis.py"]);
  let pyData;
  pythonProcess.stdout.on("data", (data) => {
    pyData = data;
    //  console.log(`Python script output: ${pyData}`);
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
  runPythonScript((pyData) => {
    res.json({
      output: pyData,
    });
    //  fs.writeFile(
    //    "extracts.html",
    //    `<pre style="margin-left :30px;">` + pyData + `</pre>`,
    //    (err) => {
    //      if (err) {
    //        console.error(`Error writing file: ${err}`);
    //      } else {
    //        console.log("File written successfully.");
    //      }
    //    }
    //  );
  });
});

//-------------------keeping the server alive and running---------------

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}/xtract`);
});
