import mitmproxy
from mitmproxy import ctx
from mitmproxy import http
from mitmproxy import addons
from cryptography import x509
from cryptography.hazmat.backends import default_backend
# from mitmproxy import

# class ChangeHTTPCode:
#     filter = "google.com"

#     def response(self, flow: http.HTTPFlow) -> None:
#         if (self.filter in flow.request.pretty_url):
#             flow.response.status_code = 503
#             flow.kill()

addons.default_addons()


class MitmLogic():
    filter = "crypto-project.xyz"

    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):
        if (self.filter in flow.request.pretty_url):
            self.num = self.num + 1
            ctx.log.info("We've seen %d flows" % self.num)
            state = flow.get_state()
            ctx.log.info(state['client_conn']['sni'])
            ctx.log.info(state['client_conn']['tls_version'])
            ctx.log.info(state['client_conn']['cipher_name'])
            ctx.log.info(state['server_conn']['cipher_name'])
            l = len(state['server_conn']['certificate_list'])
            ctx.log.info(f'number of certificates : {l}')
            for cert_data in state['server_conn']['certificate_list']:
                # parse the certificate
                cert = x509.load_pem_x509_certificate(
                    cert_data, default_backend())
                # print relavant info
                # e, n for RSA
                e, n = cert.public_key().public_numbers().e, cert.public_key().public_numbers().n
                n_str = str(n)[:20]+'...'
                ctx.log.info(f'RSA public params: e={e}, n={n_str}')
                ctx.log('################')

    def tls_clienthello(self, data: mitmproxy.proxy.layers.tls.ClientHelloData):
        """
        Mitmproxy has received a TLS ClientHello message.

        This hook decides whether a server connection is needed
        to negotiate TLS with the client (data.establish_server_tls_first)
        """
        # ctx.log(f"tls_clienthello: {data}")
        # # ctx.log(f"tls_clienthello: {data.context}")
        # # ctx.log(f"tls_clienthello: {data.context.client}")
        # ctx.log(f"tls_clienthello alpn: {data.context.client.alpn}")
        # ctx.log(
        #     f"tls_clienthello alpn_offers: {data.context.client.alpn_offers}")
        # ctx.log(
        #     f"tls_clienthello alpn_proto_negotiated: {data.context.client.alpn_proto_negotiated}")
        # ctx.log(f"tls_clienthello cipher: {data.context.client.cipher}")
        # ctx.log(
        #     f"tls_clienthello cipher_list: {data.context.client.cipher_list}")
        # ctx.log(
        #     f"tls_clienthello cipher_name: {data.context.client.cipher_name}")
        # ctx.log(
        #     f"tls_clienthello tls_version: {data.context.client.tls_version}")
        # ctx.log(f"tls_clienthello: {dir(data.context.client)}")
        # ctx.log(f"tls_clienthello: {dir(data.context)}")

    def tls_start_client(self, data: mitmproxy.proxy.layers.tls.TlsStartData):
        """
        TLS Negotation between mitmproxy and a client is about to start.

        An addon is expected to initialize data.ssl_conn.
        (by default, this is done by mitmproxy.addons.TlsConfig)
        """
        # ctx.log(f"tls_start_client: {data}")
        ctx.log(f"tls_start_client alpn: {data.context.server.alpn}")
        ctx.log(
            f"tls_start_client alpn_offers: {data.context.server.alpn_offers}")
        ctx.log(
            f"tls_start_client alpn_proto_negotiated: {data.context.server.alpn_proto_negotiated}")
        ctx.log(f"tls_start_client cipher: {data.context.server.cipher}")
        ctx.log(
            f"tls_start_client cipher_list: {data.context.server.cipher_list}")
        ctx.log(
            f"tls_start_client cipher_name: {data.context.server.cipher_name}")
        ctx.log(
            f"tls_start_client tls_version: {data.context.server.tls_version}")
        # pass

    def tls_start_server(self, data: mitmproxy.proxy.layers.tls.TlsStartData):
        """
        TLS Negotation between mitmproxy and a server is about to start.

        An addon is expected to initialize data.ssl_conn.
        (by default, this is done by mitmproxy.addons.TlsConfig)
        """
        # ctx.log(f"tls_start_server: {data}")
        ctx.log(f"tls_clienthello: {data}")
        # ctx.log(f"tls_clienthello: {data.context}")
        # ctx.log(f"tls_clienthello: {data.context.client}")
        ctx.log(f"tls_clienthello alpn: {data.context.client.alpn}")
        ctx.log(
            f"tls_clienthello alpn_offers: {data.context.client.alpn_offers}")
        ctx.log(
            f"tls_clienthello alpn_proto_negotiated: {data.context.client.alpn_proto_negotiated}")
        ctx.log(f"tls_clienthello cipher: {data.context.client.cipher}")
        ctx.log(
            f"tls_clienthello cipher_list: {data.context.client.cipher_list}")
        ctx.log(
            f"tls_clienthello cipher_name: {data.context.client.cipher_name}")
        ctx.log(
            f"tls_clienthello tls_version: {data.context.client.tls_version}")
        pass


addons = [
    MitmLogic()
]
