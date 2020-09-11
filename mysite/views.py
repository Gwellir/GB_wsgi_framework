from engine.templates import render


def index(request):
    count = request.get('count', 1)
    return '200 OK', render('index.html', count=count)


def about(request):
    count = request.get('count', 1)
    return '200 OK', render('about.html', count=count)


def requests(request):
    params = {
        'count': request.get('count', 1),
        'get_field': request.get('test_get', None),
        'post_field': request.get('test_post', None),
    }
    return '200 OK', render('requests.html', **params)


def contacts(request):
    params = {
        'count': request.get('count', 1),
        'topic': request.get('topic', None),
        'message': request.get('message', None),
        'email': request.get('email', None),
    }

    if params['topic'] and params['message'] and params['email']:
        print(f'Получено сообщение:\nТема: {params["topic"]}\nТекст: {params["message"]}\n'
              f'от пользователя {params["email"]}')
        params['is_saved'] = True

    return '200 OK', render('contacts.html', **params)
