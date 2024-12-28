const fileUploadForm = document.getElementById("file-upload-form");
const fileName = document.getElementById("file-name");
const fileInput = document.getElementById("file-input");
const uploadButton = document.getElementById("upload-button");
const browseButton = document.getElementById("browse-files-button");

fileUploadForm.addEventListener('dragover', fileUploadDragOver);
fileUploadForm.addEventListener('dragenter', fileUploadDragEnter);
fileUploadForm.addEventListener('dragleave', fileUploadDragLeave);
fileUploadForm.addEventListener('drop', fileUploadDrop);
fileInput.addEventListener('change', fileInputChange);
browseButton.addEventListener('click', browseButtonClick);


// Event Listeners
function fileUploadDragOver(event) {
    event.preventDefault();
}

function fileUploadDragEnter(event) {
    fileUploadForm.classList.add('over');
    uploadButton.classList.add('over');
}

function fileUploadDragLeave(event) {
    fileUploadForm.classList.remove('over');
    uploadButton.classList.remove('over');
}

function fileUploadDrop(event) {
    event.preventDefault();
    fileUploadForm.classList.remove('over');
    uploadButton.classList.remove('over');
    const file = event.dataTransfer.files[0];



    if (file) {
        fileInput.files = event.dataTransfer.files; // Update input files
        fileName.querySelector('strong').textContent = file.name; // TODO: make it so the name switches whenever the fileInput file is changed
    }
}

function browseButtonClick(event) {
    fileInput.click();
}

function fileInputChange(event) {

    const file = fileInput.files[0];
    if (file) {
        fileName.querySelector('strong').textContent = file.name; // TODO: make it so the name switches whenever the fileInput file is changed
    }
}