from mitmproxy import http
from mitmproxy import ctx


# class ChangeHTTPCode:
#     filter = "google.com"

#     def response(self, flow: http.HTTPFlow) -> None:
#         if (self.filter in flow.request.pretty_url):
#             flow.response.status_code = 503
#             flow.kill()

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)


addons = [
    Counter()
]

addons = [
    # ChangeHTTPCode(),
    Counter()

]
