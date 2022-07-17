from django.shortcuts import render
# Create your views here.

posts = [
    {
    "author":"Ayodeji",
    "title":"Blog Post 1",
    "content":"First post content",
    "date_posted":"July 17th, 2022",
    },
   {
    "author":"Dejavu",
    "title":"Blog Post 2",
    "content":"Second post content",
    "date_posted":"July 18th, 2022",
    }
]


def home(request):
    context = {
    "posts":posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {"title":"About"})
