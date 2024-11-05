from django.shortcuts import render, HttpResponse
from django.http import HttpRequest
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django import forms
from utils.main import convert_file

import io

# Create your views here.


def home(request:HttpRequest):
    class UploadFileForm(forms.Form):
        file = forms.FileField()

    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            excel_file = request.FILES['file']
            calendar = convert_file(excel_file)
            
            # Convert Calendar to ICS file in memory
            ics_file = io.BytesIO()
            ics_file.write(calendar.to_ical())
            ics_file.seek(0)

            # Save the file temporarily in Django's default file storage
            file_name = 'calendar.ics'
            file_path = default_storage.save(file_name, ContentFile(ics_file.read()))

             # Pass the file name to the template to show a download button
            return render(request, 'index.html', {
                'form': form,
                'file_name': file_name
            })
    
    else:
        form = UploadFileForm()
    
    return render(request, "index.html", {'form': form})

def download_file(request:HttpRequest, file_name:str):
    file_path = default_storage.path(file_name)
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='text/calendar')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
