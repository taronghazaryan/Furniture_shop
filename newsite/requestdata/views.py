from django.shortcuts import render
from .forms import UploadFile
from django.core.files.storage import FileSystemStorage

# Create your views here.


def upload_file(request):
    if request.method == 'POST':
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            myfile = form.cleaned_data['file']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
    else:
        form = UploadFile()

    context = {
        'form': form,
    }

    return render(request, 'requestdata/upload_form.html', context=context)
