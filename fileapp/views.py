from django.shortcuts import render
from django.http import JsonResponse, FileResponse
import os, subprocess
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES_DIR = os.path.join(BASE_DIR, 'local_txt_files')
GOOGLE_DRIVE_FOLDER = 'https://drive.google.com/uc?export=download&id='

# Mock file-to-ID map
DRIVE_FILES = {
    'example1.txt': 'GOOGLE_DRIVE_FILE_ID_1',
    'example2.txt': 'GOOGLE_DRIVE_FILE_ID_2'
}

def home(request):
    all_files = list(DRIVE_FILES.keys())
    return render(request, 'fileapp/index.html', {'files': all_files})

def check_file(request):
    filename = request.GET.get('filename')
    filepath = os.path.join(FILES_DIR, filename)
    return JsonResponse({'exists': os.path.exists(filepath)})

def open_file(request):
    filename = request.GET.get('filename')
    filepath = os.path.join(FILES_DIR, filename)
    if os.path.exists(filepath):
        subprocess.Popen(['notepad.exe', filepath])
    return JsonResponse({'status': 'ok'})

def download_file(request):
    filename = request.GET.get('filename')
    file_id = DRIVE_FILES.get(filename)
    if file_id:
        url = GOOGLE_DRIVE_FOLDER + file_id
        r = requests.get(url)
        with open(os.path.join(FILES_DIR, filename), 'wb') as f:
            f.write(r.content)
    return JsonResponse({'status': 'downloaded'})
