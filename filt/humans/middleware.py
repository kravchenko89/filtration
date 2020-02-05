import time
from humans.models import Logger


class AdminMiddleware(object):
    def __init__(self, response):
        self.response = response

    def __call__(self, request):
        request.start_time = time.time()
        response = self.response(request)

        if request.path.startswith('/admin/'):

            time_full = float(time.time() - request.start_time).__round__(2)
            # breakpoint()

            Logger.objects.create(path=request.path, method=request.method,
                                  user_id=request.user.id,
                                  time_delta=time_full)
            return response
        else:
            return response
