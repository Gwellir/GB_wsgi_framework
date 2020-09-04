import views
from engine.core import Application


paths = {
    '': views.index,
    '/about': views.about,
}


class Counter:

    def __init__(self):
        self.count = 0

    def __call__(self, request):
        self.count += 1
        request['count'] = self.count


middleware = [
    Counter()
]

application = Application(paths, middleware)
