from mitmproxy import ctx
from mitmproxy import http
# from mitmproxy import proxy
import mitmproxy
# from mitmproxy import

# class ChangeHTTPCode:
#     filter = "google.com"

#     def response(self, flow: http.HTTPFlow) -> None:
#         if (self.filter in flow.request.pretty_url):
#             flow.response.status_code = 503
#             flow.kill()


class GetCertificate():
    filter = "crypto-project.xyz"

    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        if (self.filter in flow.request.pretty_url):
            self.num = self.num + 1
            ctx.log.info("We've seen %d flows" % self.num)

    def tls_clienthello(self, data: mitmproxy.proxy.layers.tls.ClientHelloData):
        """
        Mitmproxy has received a TLS ClientHello message.

        This hook decides whether a server connection is needed
        to negotiate TLS with the client (data.establish_server_tls_first)
        """
        ctx.log(f"tls_clienthello: {data}")

    def tls_start_client(self, data: mitmproxy.proxy.layers.tls.TlsStartData):
        """
        TLS Negotation between mitmproxy and a client is about to start.

        An addon is expected to initialize data.ssl_conn.
        (by default, this is done by mitmproxy.addons.TlsConfig)
        """
        ctx.log(f"tls_start_client: {data}")

    def tls_start_server(self, data: mitmproxy.proxy.layers.tls.TlsStartData):
        """
        TLS Negotation between mitmproxy and a client is about to start.

        An addon is expected to initialize data.ssl_conn.
        (by default, this is done by mitmproxy.addons.TlsConfig)
        """
        ctx.log(f"tls_start_client: {data}")


addons = [
    GetCertificate()
]
