from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import File
import os

def index(request):
    if request.method == 'POST':
        fs = FileSystemStorage()
        file = request.FILES.get('file')
        fileName = str(file)
        fileSize = file.size
        file_extension = os.path.splitext(fileName)[1].lower()
        max_size = 400 * (1024 * 1024)
        
        if fileSize < max_size:

            # Save file information to the database
            new_file = File.objects.create(file=file, fileName=fileName, fileSize=fileSize/ (1024 * 1024), fileType=file_extension)
            new_file.save()

            # Redirect to the unique link page
            messages.info(request, 'Successfully Uploaded')
            return redirect('uniqueLink', pk=new_file.uniqueLink)  # Use the view name and arguments
        else:
            messages.info(request, 'File size exceeded')
            return redirect('/')
            

    return render(request, 'index.html')

def uniqueLink(request, pk):
    fileInfo = File.objects.get(uniqueLink=pk)
    return render(request, 'uniqueLink.html', {'fileInfo': fileInfo})
