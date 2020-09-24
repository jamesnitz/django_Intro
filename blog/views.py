from django.shortcuts import render

posts = [
  {
    'author': 'james',
    'title': 'blog post 1',
    'content': 'first post content',
    'date_posted': 'September 24, 2020'
  },
  {
    'author': 'slab',
    'title': 'bruh',
    'content': 'second post content',
    'date_posted': 'September 25, 2020'
  }
]


def home(request):
  context = {
    'posts': posts
  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html')
  