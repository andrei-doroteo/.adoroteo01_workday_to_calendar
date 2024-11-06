import io

from converter.utils.main import convert_file
from django.core.files.storage import default_storage
from django.http import HttpRequest
from django.shortcuts import HttpResponse, render

# Create your views here.


def home(request: HttpRequest):

    if request.method == "POST":

        try:
            excel_file = request.FILES["file"]
            calendar = convert_file(excel_file)

            # Convert Calendar to ICS file in memory
            ics_file = io.BytesIO()
            ics_file.write(calendar.to_ical())
            ics_file.seek(0)

            # Create response to download the processed file
            response = HttpResponse(ics_file, content_type="text/calendar")
            response['Content-Disposition'] = 'attachment; filename=schedule.ics'
            # Pass the file name to the template to show a download button
            return response
    
        except:
            return render(request, "index.html")

    return render(request, "index.html")
