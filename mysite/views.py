from engine.templates import render


def index(request):
    params = {
        'title': 'Главная страница',
        'count': request.get('count', 1),
    }

    return '200 OK', render('index.html', **params)


def about(request):
    params = {
        'title': 'О сайте',
        'count': request.get('count', 1),
    }
    return '200 OK', render('about.html', **params)


def requests(request):
    params = {
        'title': 'Тест запросов',
        'count': request.get('count', 1),
        'get_field': request.get('params', {}).get('test_get', None),
        'post_field': request.get('data', {}).get('test_post', None),
    }
    return '200 OK', render('requests.html', **params)


def contacts(request):
    params = {
        'title': 'Контакты',
        'count': request.get('count', 1),
    }

    if request['method'] == 'POST':
        data = request['data']
        params['topic'] = data.get('topic', None)
        params['message'] = data.get('message', None)
        params['email'] = data.get('email', None)

        if params['topic'] and params['message'] and params['email']:
            print(f'Получено сообщение:\nТема: {params["topic"]}\nТекст: {params["message"]}\n'
                  f'от пользователя {params["email"]}')
            params['is_saved'] = True

    return '200 OK', render('contacts.html', **params)
