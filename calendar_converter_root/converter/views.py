import io
from converter.utils.main import convert_file
from django.core.files.storage import default_storage
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def home(request: HttpRequest):
    file_uploaded = False
    download_url = None

    if request.method == "POST":
        try:
            # Get the uploaded file
            excel_file = request.FILES["file"]
            
            # Convert the file (may throw an exception if there's an error)
            calendar = convert_file(excel_file)

            # Convert Calendar to ICS format in memory
            ics_file = io.BytesIO()
            ics_file.write(calendar.to_ical())
            ics_file.seek(0)

            # Save the ICS file temporarily in Django's storage
            filename = "schedule.ics"
            path = default_storage.save(filename, ics_file)

            # Set the file_uploaded flag to True and create a download URL
            file_uploaded = True
            download_url = default_storage.url(path)

        except Exception as e:
            # Optional: Log or print the exception for debugging
            print(f"Error processing file: {e}")
            return render(request, "index.html", {'file_uploaded': f"Error processing file: {e}", 'download_url': download_url})

    # Render the template and pass file_uploaded and download_url
    return render(request, "index.html", {'file_uploaded': file_uploaded, 'download_url': download_url})
