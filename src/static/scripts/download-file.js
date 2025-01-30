const downloadButton = document.getElementById("download-button");
const googleCalendarButton = document.getElementById(
	"upload-to-google-calendar-button"
);

let downloaded = false;

downloadButton.addEventListener("click", (event) => (downloaded = true));
googleCalendarButton.addEventListener("click", (event) => {
	if (!downloaded) {
		downloaded = true;
		downloadButton.click();
	}
});
