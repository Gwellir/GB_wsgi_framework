TEXT_CONTENT = [('Content-Type', 'text/html')]


class Application:

    def __init__(self, paths, fronts):
        self.paths = paths
        self.fronts = fronts

    def __call__(self, environ, start_response):
        path = environ['PATH_INFO'].rstrip('/')
        if path in self.paths:
            view = self.paths[path]
        else:
            view = self.not_found
        request = {}
        for fc in self.fronts:
            fc(request)
        code, content = view(request)
        start_response(code, TEXT_CONTENT)
        print(content.encode('utf-8'))
        return [content.encode('utf-8')]

    def not_found(self, request):
        return '404 NOT FOUND', '404 Not Found'
