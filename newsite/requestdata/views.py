from django.shortcuts import render
from .forms import UploadFile

# Create your views here.


def upload_file(request):
    # if request.method == 'POST':
    #     form =
    return render(request, 'requestdata/upload_form.html')
