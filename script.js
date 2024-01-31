function alerting(){
alert('Please upload the file!')
}

function changeContent(fileName) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
          document.getElementById("content").innerHTML = this.responseText;
      }
  };
  xhttp.open("GET", fileName, true);
  xhttp.send();
}