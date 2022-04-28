from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime
import re
#source .venv/bin/activate
# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")

def hello_there(request, name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return render(
        request,
        'hello_there.html',
        {
            'name': name,
            'date': datetime.now()
        }
    )
