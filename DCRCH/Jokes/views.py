from django.shortcuts import render

# Create your views here.

def JokesView(request):

    context = {
        'title': 'Jokes App',
    }

    return render(request, 'jokes/index.html', context)
