from django.shortcuts import render

# Create your views here.

def index(request):
    biblio = {
        "texte":"un message",
        "num":11
    }

    return render(request, "page/index.html", biblio)