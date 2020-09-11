from urllib.parse import unquote

TEXT_CONTENT = [('Content-Type', 'text/html')]


class Application:

    def __init__(self, paths, fronts):
        self.paths = paths
        self.fronts = fronts

    def __call__(self, environ, start_response):
        # parsing PATH
        path = environ['PATH_INFO']
        if not path.endswith('/'):
            path = f'{path}/'

        if path in self.paths:
            view = self.paths[path]
        else:
            view = self.not_found

        request = {}
        method = environ['REQUEST_METHOD']
        # parsing GET request parameters
        query_string = environ['QUERY_STRING']
        # print(query_string)
        params = self.parse_input_data(query_string)
        # parsing POST request parameters
        data = self.parse_wsgi_input_data(self.get_wsgi_input_data(environ))

        request['method'] = method
        request['data'] = data
        request['params'] = params

        # running middleware
        for fc in self.fronts:
            fc(request)

        code, content = view(request)
        start_response(code, TEXT_CONTENT)
        return [content.encode('utf-8')]

    @staticmethod
    def parse_input_data(query: str) -> dict:
        result = {}
        if query:
            params = query.split('&')
            for item in params:
                k, v = item.split('=')
                result[k] = v

        return result

    @staticmethod
    def get_wsgi_input_data(env: dict) -> bytes:
        content_length_data = env.get('CONTENT_LENGTH')
        content_length = int(content_length_data) if content_length_data else 0
        data = env['wsgi.input'].read(content_length) if content_length > 0 else b''
        return data

    def parse_wsgi_input_data(self, data: bytes) -> dict:
        result = {}
        if data:
            data_str = data.decode(encoding='utf-8')
            print(data_str)
            result = self.parse_input_data(unquote(data_str))
        return result

    def not_found(self, request):
        return '404 NOT FOUND', '404 Not Found'
