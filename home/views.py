from django.shortcuts import render


# Create your views here.

def home(request):
    articles=[{
        "id":1,
        "heading":"dv",
        "desc":"eiveodv",

    },
    {
        "id":2,
        "heading":"iduf",
        "desc":"eiveoddsckjbskjcvbj",

    }]
    context={
        "articles":articles
        
    }

    return render(request,"pages/home.html",context)

def about(request):

    return render(request,"pages/about.html")

def contact(request):

    return render(request,"pages.contact.html")