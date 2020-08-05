from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    # 기본 방법
    # return HttpResponse("<h1> Hello world! </h1>")
    # 좀 advanced
    return render(request, "home.html", {})

def about_view(request, *args, **kwargs):
    my_context ={
        "my_text" : "This is about us",
        "my_number" : 123,
        "my_list" : [1,2,3],
    }
    return render(request, "about.html", my_context)
