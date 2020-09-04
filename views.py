from engine.templates import render


def index(request):
    count = request.get('count', 1)
    return '200 OK', render('index.html', count=count)


def about(request):
    count = request.get('count', 1)
    return '200 OK', render('about.html', count=count)