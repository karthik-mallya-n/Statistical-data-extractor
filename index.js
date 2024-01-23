function resetFileSelection() {
  const openFileExplorer = document.getElementById('openFileExplorer');
  const fileInfo = document.getElementById('fileInfo');
  const container = document.getElementById('container');

  openFileExplorer.textContent = 'Click me to open File Explorer';
  fileInfo.innerHTML = '';

  // Update the content of the container, including excelViewer, tableContainer, and fileInfo
  container.innerHTML = `
    <div id="excelViewer"
         class="out bg-neutral-50 hover:bg-amber-100 rounded-xl h-56 border-solid border-blue-300 border-7 border-r-4"
         ondragover="allowDrop(event)" ondrop="handleDrop(event)">
      <div id="tableContainer" class="in content font-sans text-lg text-gray-600 italic leading-relaxed">
        <p class="flex justify-center items-center h-52">Drag Here</p>
      </div>
      <div id="fileInfo"></div>
    </div>
  `;
  const main = document.getElementById('main');
  const main2 = document.getElementById('main2');

  main.classList.remove('trans');
  main2.style.width= '';
  main2.style.height= '';
  main2.classList.add('right');
  main2.innerHTML=``
}

function downbutton() {
  
  const main = document.getElementById('main');
  const main2 = document.getElementById('main2');

  main.classList.add('trans');
  main2.style.width= '20vw';
  main2.style.height= 'auto';
  main2.classList.add('left');
  main2.innerHTML=`<div class="m-4 bg-indigo-100 rounded-xl h-96 md:w-3/4 shake">
  <div class="  w-full h-full">
      <div class="w-full h-1/2 inline-flex justify-center items-center" ><div class="button ">Share</div></div>
      <div class="w-full h-1/2 inline-flex justify-center items-center" ><div class="button ">Download</div></div>
  </div>
</div>`

}
function changeColor(element) {
  // Remove 'active' class from all li elements
  var lis = document.querySelectorAll('.navi');
  lis.forEach(function(li) {
    li.classList.remove('active');
  });

  // Add 'active' class to the clicked li element
  element.parentNode.classList.add('active');
}


document.getElementById('openFileExplorer').addEventListener('click', function () {
  const fileInput = document.createElement('input');
  fileInput.type = 'file';
  fileInput.accept = '.xlsx, .xls, .csv, .json';
  fileInput.style.display = 'none';

  document.body.appendChild(fileInput);

  fileInput.addEventListener('change', function () {
    handleFileSelection(fileInput); v
  });

  fileInput.click();

  document.body.removeChild(fileInput);
});

