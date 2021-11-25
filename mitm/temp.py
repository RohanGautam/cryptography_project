from pprint import pprint
x = {'id': 'e4fc7f2d-2908-4c37-8dbd-e63d26326772',
     'error': None, 'client_conn': {'address': ('127.0.0.1', 33724), 'alpn': b'http/1.1', 'cipher_name': 'TLS_AES_256_GCM_SHA384', 'id': '7605e9c7-48e7-4bc2-89d1-45b141a76ae8', 'mitmcert': None, 'sni': 'crypto-project.xyz', 'timestamp_end': None, 'timestamp_start': 1637830920.8973324, 'timestamp_tls_setup': 1637830921.3321815, 'tls_established': True, 'tls_extensions': [], 'tls_version': 'TLSv1.3', 'state': 3, 'sockname': ('127.0.0.1', 8080), 'error': None, 'tls': True, 'certificate_list': [], 'alpn_offers': [b'h2', b'http/1.1'], 'cipher_list': ()}, 'server_conn': {'address': ('crypto-project.xyz', 443), 'alpn': b'http/1.1', 'id': '0cb3df3e-ae1c-4e54-a82f-99d35cbdd780', 'ip_address': ('35.239.113.22', 443), 'sni': 'crypto-project.xyz', 'source_address': ('172.20.135.2', 47592), 'timestamp_end': None, 'timestamp_start': 1637830920.899386, 'timestamp_tcp_setup': 1637830921.1124866, 'timestamp_tls_setup': 1637830921.3294146, 'tls_established': True, 'tls_version': 'TLSv1.3', 'via': None, 'state': 3, 'error': None, 'tls': True, 'certificate_list': [b'-----BEGIN CERTIFICATE-----\nMIIFKzCCBBOgAwIBAgISBIjiSKaYaopgoaTivIN9uonNMA0GCSqGSIb3DQEBCwUA\nMDIxCzAJBgNVBAYTAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB0MQswCQYDVQQD\nEwJSMzAeFw0yMTExMTgxMDQ3MTdaFw0yMjAyMTYxMDQ3MTZaMB0xGzAZBgNVBAMT\nEmNyeXB0by1wcm9qZWN0Lnh5ejCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC\nggEBALBZv4jJIMVpzcDnVx/5DnoRJQbyCmQ895AiQeTXOJdvPPqY4ZyPa5nmJwXc\nepuVOBzmdIKBCbV9s6bAKf7sGqGoJDII6svUm3kQ4BaWbiQDHA1wp4+OwAQmAx4D\n6jaMHt3T6CmA+f2iw35HsBSBG5UI95ackiAJINpw1WEQvq11zubBVtqoFlVWqHzC\nyqnl9oNulGB0amhZ4TVILq/nQKrFTZ1une6Zje68nfewnAbHu6QR+FO2G0gv31x9\nocswqeAG+QRvuQfMMD6i2S1Q/JljF0KZBvKhrSP7r1UXxSv4sjgLb6oFzrR/6/Sm\nmh42WJRchKuGg5SnU8pOmv9hmR0CAwEAAaOCAk4wggJKMA4GA1UdDwEB/wQEAwIF\noDAdBgNVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAwIwDAYDVR0TAQH/BAIwADAd\nBgNVHQ4EFgQUYSzpipAsmyq2bGrax70c++ptMVUwHwYDVR0jBBgwFoAUFC6zF7dY\nVsuuUAlA5h+vnYsUwsYwVQYIKwYBBQUHAQEESTBHMCEGCCsGAQUFBzABhhVodHRw\nOi8vcjMuby5sZW5jci5vcmcwIgYIKwYBBQUHMAKGFmh0dHA6Ly9yMy5pLmxlbmNy\nLm9yZy8wHQYDVR0RBBYwFIISY3J5cHRvLXByb2plY3QueHl6MEwGA1UdIARFMEMw\nCAYGZ4EMAQIBMDcGCysGAQQBgt8TAQEBMCgwJgYIKwYBBQUHAgEWGmh0dHA6Ly9j\ncHMubGV0c2VuY3J5cHQub3JnMIIBBQYKKwYBBAHWeQIEAgSB9gSB8wDxAHcAKXm+\n8J45OSHwVnOfY6V35b5XfZxgCvj5TV0mXCVdx4QAAAF9Mt9ZWAAABAMASDBGAiEA\n4Y2n9c+Nk+dQg2K0Q7QwkaRCwaGXSM1Yso3ucc9ZcjcCIQDX1+7VFXLAcjaLIxeu\n1Gayzeu8dq9PMnmSC4CG3PcWnwB2AG9Tdqwx8DEZ2JkApFEV/3cVHBHZAsEAKQaN\nsgiaN9kTAAABfTLfWqQAAAQDAEcwRQIgAoDWvHK+I0uKABiYtY+w0TgIK39CyzJN\nTfJfZPvy4skCIQCQwOGWf4ja+SfZXFX3BQEguJaKJsGbfqMuUfYNCJtHHTANBgkq\nhkiG9w0BAQsFAAOCAQEAFJJ1/a+6mT5FhzdzFiyxKyqNaGvT0Trs9b/cCVErqnOR\nb5xakTGGSxpSG8N17mI0uL3AWlanTxxbT8eIlCb9DmQb3VmIPjBw0O3EiFBEuI59\nozl+GG8t82uFi0Enya0pRKRnIeZupAhRqawLLBfas/IGxp0bhnDgrvyM97UUpCqr\ndL4awAFVI0s4DRwc7t8/QKflDwtFlczJsNAp8bJ8v/G7vNKus4Ov48KPyS1qkte1\nlDvB4tsVC8IWuBiit3iB0zGEdRRRpbmv4q0NxRYE8oCX/L1NqX7sTtoiLQtKdi+v\nHt1I+9dn6JStCbjUhOGHZYbNE/pCuSYMGl7d30V8HQ==\n-----END CERTIFICATE-----\n', b'-----BEGIN CERTIFICATE-----\nMIIFFjCCAv6gAwIBAgIRAJErCErPDBinU/bWLiWnX1owDQYJKoZIhvcNAQELBQAw\nTzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh\ncmNoIEdyb3VwMRUwEwYDVQQDEwxJU1JHIFJvb3QgWDEwHhcNMjAwOTA0MDAwMDAw\nWhcNMjUwOTE1MTYwMDAwWjAyMQswCQYDVQQGEwJVUzEWMBQGA1UEChMNTGV0J3Mg\nRW5jcnlwdDELMAkGA1UEAxMCUjMwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEK\nAoIBAQC7AhUozPaglNMPEuyNVZLD+ILxmaZ6QoinXSaqtSu5xUyxr45r+XXIo9cP\nR5QUVTVXjJ6oojkZ9YI8QqlObvU7wy7bjcCwXPNZOOftz2nwWgsbvsCUJCWH+jdx\nsxPnHKzhm+/b5DtFUkWWqcFTzjTIUu61ru2P3mBw4qVUq7ZtDpelQDRrK9O8Zutm\nNHz6a4uPVymZ+DAXXbpyb/uBxa3Shlg9F8fnCbvxK/eG3MHacV3URuPMrSXBiLxg\nZ3Vms/EY96Jc5lP/Ooi2R6X/ExjqmAl3P51T+c8B5fWmcBcUr2Ok/5mzk53cU6cG\n/kiFHaFpriV1uxPMUgP17VGhi9sVAgMBAAGjggEIMIIBBDAOBgNVHQ8BAf8EBAMC\nAYYwHQYDVR0lBBYwFAYIKwYBBQUHAwIGCCsGAQUFBwMBMBIGA1UdEwEB/wQIMAYB\nAf8CAQAwHQYDVR0OBBYEFBQusxe3WFbLrlAJQOYfr52LFMLGMB8GA1UdIwQYMBaA\nFHm0WeZ7tuXkAXOACIjIGlj26ZtuMDIGCCsGAQUFBwEBBCYwJDAiBggrBgEFBQcw\nAoYWaHR0cDovL3gxLmkubGVuY3Iub3JnLzAnBgNVHR8EIDAeMBygGqAYhhZodHRw\nOi8veDEuYy5sZW5jci5vcmcvMCIGA1UdIAQbMBkwCAYGZ4EMAQIBMA0GCysGAQQB\ngt8TAQEBMA0GCSqGSIb3DQEBCwUAA4ICAQCFyk5HPqP3hUSFvNVneLKYY611TR6W\nPTNlclQtgaDqw+34IL9fzLdwALduO/ZelN7kIJ+m74uyA+eitRY8kc607TkC53wl\nikfmZW4/RvTZ8M6UK+5UzhK8jCdLuMGYL6KvzXGRSgi3yLgjewQtCPkIVz6D2QQz\nCkcheAmCJ8MqyJu5zlzyZMjAvnnAT45tRAxekrsu94sQ4egdRCnbWSDtY7kh+BIm\nlJNXoB1lBMEKIq4QDUOXoRgffuDghje1WrG9ML+Hbisq/yFOGwXD9RiX8F6sw6W4\navAuvDszue5L3sz85K+EC4Y/wFVDNvZo4TYXao6Z0f+lQKc0t8DQYzk1OXVu8rp2\nyJMC6alLbBfODALZvYH7n7do1AZls4I9d1P4jnkDrQoxB3UqQ9hVl3LEKQ73xF1O\nyK5GhDDX8oVfGKF5u+decIsH4YaTw7mP3GFxJSqv3+0lUFJoi5Lc5da149p90Ids\nhCExroL1+7mryIkXPeFM5TgO9r0rvZaBFOvV2z0gp35Z0+L4WPlbuEjN/lxPFin+\nHlUjr8gRsI3qfJOQFy/9rKIJR0Y/8Omwt/8oTWgy1mdeHmmjk7j1nYsvC9JSQ6Zv\nMldlTTKB3zhThV1+XWYp6rjd5JW1zbVWEkLNxE7GJThEUG3szgBVGP7pSWTUTsqX\nnLRbwHOoq7hHwg==\n-----END CERTIFICATE-----\n',
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     b'-----BEGIN CERTIFICATE-----\nMIIFYDCCBEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzANBgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExtEaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB4XDTIxMDEyMDE5MTQwM1oXDTI0MDkzMDE4MTQwM1ow\nTzELMAkGA1UEBhMCVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh\ncmNoIEdyb3VwMRUwEwYDVQQDEwxJU1JHIFJvb3QgWDEwggIiMA0GCSqGSIb3DQEB\nAQUAA4ICDwAwggIKAoICAQCt6CRz9BQ385ueK1coHIe+3LffOJCMbjzmV6B493XC\nov71am72AE8o295ohmxEk7axY/0UEmu/H9LqMZshftEzPLpI9d1537O4/xLxIZpL\nwYqGcWlKZmZsj348cL+tKSIG8+TA5oCu4kuPt5l+lAOf00eXfJlII1PoOK5PCm+D\nLtFJV4yAdLbaL9A4jXsDcCEbdfIwPPqPrt3aY6vrFk/CjhFLfs8L6P+1dy70sntK\n4EwSJQxwjQMpoOFTJOwT2e4ZvxCzSow/iaNhUd6shweU9GNx7C7ib1uYgeGJXDR5\nbHbvO5BieebbpJovJsXQEOEO3tkQjhb7t/eo98flAgeYjzYIlefiN5YNNnWe+w5y\nsR2bvAP5SQXYgd0FtCrWQemsAXaVCg/Y39W9Eh81LygXbNKYwagJZHduRze6zqxZ\nXmidf3LWicUGQSk+WT7dJvUkyRGnWqNMQB9GoZm1pzpRboY7nn1ypxIFeFntPlF4\nFQsDj43QLwWyPntKHEtzBRL8xurgUBN8Q5N0s8p0544fAQjQMNRbcTa0B7rBMDBc\nSLeCO5imfWCKoqMpgsy6vYMEG6KDA0Gh1gXxG8K28Kh8hjtGqEgqiNx2mna/H2ql\nPRmP6zjzZN7IKw0KKP/32+IVQtQi0Cdd4Xn+GOdwiK1O5tmLOsbdJ1Fu/7xk9TND\nTwIDAQABo4IBRjCCAUIwDwYDVR0TAQH/BAUwAwEB/zAOBgNVHQ8BAf8EBAMCAQYw\nSwYIKwYBBQUHAQEEPzA9MDsGCCsGAQUFBzAChi9odHRwOi8vYXBwcy5pZGVudHJ1\nc3QuY29tL3Jvb3RzL2RzdHJvb3RjYXgzLnA3YzAfBgNVHSMEGDAWgBTEp7Gkeyxx\n+tvhS5B1/8QVYIWJEDBUBgNVHSAETTBLMAgGBmeBDAECATA/BgsrBgEEAYLfEwEB\nATAwMC4GCCsGAQUFBwIBFiJodHRwOi8vY3BzLnJvb3QteDEubGV0c2VuY3J5cHQu\nb3JnMDwGA1UdHwQ1MDMwMaAvoC2GK2h0dHA6Ly9jcmwuaWRlbnRydXN0LmNvbS9E\nU1RST09UQ0FYM0NSTC5jcmwwHQYDVR0OBBYEFHm0WeZ7tuXkAXOACIjIGlj26Ztu\nMA0GCSqGSIb3DQEBCwUAA4IBAQAKcwBslm7/DlLQrt2M51oGrS+o44+/yQoDFVDC\n5WxCu2+b9LRPwkSICHXM6webFGJueN7sJ7o5XPWioW5WlHAQU7G75K/QosMrAdSW\n9MUgNTP52GE24HGNtLi1qoJFlcDyqSMo59ahy2cI2qBDLKobkx/J3vWraV0T9VuG\nWCLKTVXkcGdtwlfFRjlBz4pYg1htmf5X6DYO8A4jqv2Il9DjXA6USbW1FzXSLr9O\nhe8Y4IWS6wY7bCkjCWDcRQJMEhg76fsO3txE+FiYruq9RUWhiF1myv4Q6W+CyBFC\nDfvp7OOGAN6dEOM4+qR9sdjoSYKEBpsr6GtPAQw4dy753ec5\n-----END CERTIFICATE-----\n'], 'alpn_offers': (b'h2', b'http/1.1'), 'cipher_name': 'TLS_AES_256_GCM_SHA384', 'cipher_list': (), 'via2': None}, 'type': 'http', 'intercepted': False, 'is_replay': None, 'marked': '', 'metadata': {}, 'comment': '', 'request': {'http_version': b'HTTP/1.1', 'headers': ((b'Host', b'crypto-project.xyz'), (b'User-Agent', b'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0) Gecko/20100101 Firefox/94.0'), (b'Accept', b'image/avif,image/webp,*/*'), (b'Accept-Language', b'en-US,en;q=0.5'), (b'Accept-Encoding', b'gzip, deflate, br'), (b'Connection', b'keep-alive'), (b'Referer', b'https://crypto-project.xyz/'), (b'Sec-Fetch-Dest', b'image'), (b'Sec-Fetch-Mode', b'no-cors'), (b'Sec-Fetch-Site', b'same-origin'), (b'If-Modified-Since', b'Thu, 30 Sep 2021 03:50:49 GMT'), (b'If-None-Match', b'"167a-5cd2e5a327840"'), (b'Cache-Control', b'max-age=0')), 'content': b'', 'trailers': None, 'timestamp_start': 1637830921.5760543, 'timestamp_end': 1637830921.5767424, 'host': 'crypto-project.xyz', 'port': 443, 'method': b'GET', 'scheme': b'https', 'authority': b'', 'path': b'/icons/openlogo-75.png'
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               }, 'response': None, 'websocket': None, 'mode': 'regular', 'version': 14
     }
pprint(x)
{'client_conn': {'address': ('127.0.0.1', 33724),
                 'alpn': b'http/1.1',
                 'alpn_offers': [b'h2', b'http/1.1'],
                 'certificate_list': [],
                 'cipher_list': (),
                 'cipher_name': 'TLS_AES_256_GCM_SHA384',
                 'error': None,
                 'id': '7605e9c7-48e7-4bc2-89d1-45b141a76ae8',
                 'mitmcert': None,
                 'sni': 'crypto-project.xyz',
                 'sockname': ('127.0.0.1', 8080),
                 'state': 3,
                 'timestamp_end': None,
                 'timestamp_start': 1637830920.8973324,
                 'timestamp_tls_setup': 1637830921.3321815,
                 'tls': True,
                 'tls_established': True,
                 'tls_extensions': [],
                 'tls_version': 'TLSv1.3'},
 'comment': '',
 'error': None,
 'id': 'e4fc7f2d-2908-4c37-8dbd-e63d26326772',
 'intercepted': False,
 'is_replay': None,
 'marked': '',
 'metadata': {},
 'mode': 'regular',
 'request': {'authority': b'',
             'content': b'',
             'headers': ((b'Host', b'crypto-project.xyz'),
                         (b'User-Agent',
                          b'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:94.0)'
                          b' Gecko/20100101 Firefox/94.0'),
                         (b'Accept', b'image/avif,image/webp,*/*'),
                         (b'Accept-Language', b'en-US,en;q=0.5'),
                         (b'Accept-Encoding', b'gzip, deflate, br'),
                         (b'Connection', b'keep-alive'),
                         (b'Referer', b'https://crypto-project.xyz/'),
                         (b'Sec-Fetch-Dest', b'image'),
                         (b'Sec-Fetch-Mode', b'no-cors'),
                         (b'Sec-Fetch-Site', b'same-origin'),
                         (b'If-Modified-Since',
                          b'Thu, 30 Sep 2021 03:50:49 GMT'),
                         (b'If-None-Match', b'"167a-5cd2e5a327840"'),
                         (b'Cache-Control', b'max-age=0')),
             'host': 'crypto-project.xyz',
             'http_version': b'HTTP/1.1',
             'method': b'GET',
             'path': b'/icons/openlogo-75.png',
             'port': 443,
             'scheme': b'https',
             'timestamp_end': 1637830921.5767424,
             'timestamp_start': 1637830921.5760543,
             'trailers': None},
 'response': None,
 'server_conn': {'address': ('crypto-project.xyz', 443),
                 'alpn': b'http/1.1',
                 'alpn_offers': (b'h2', b'http/1.1'),
                 'certificate_list': [b'-----BEGIN CERTIFICATE-----\nMIIFKzCC'
                                      b'BBOgAwIBAgISBIjiSKaYaopgoaTivIN9uonN'
                                      b'MA0GCSqGSIb3DQEBCwUA\nMDIxCzAJBgNVBAY'
                                      b'TAlVTMRYwFAYDVQQKEw1MZXQncyBFbmNyeXB'
                                      b'0MQswCQYDVQQD\nEwJSMzAeFw0yMTExMTgxMD'
                                      b'Q3MTdaFw0yMjAyMTYxMDQ3MTZaMB0xGzAZBg'
                                      b'NVBAMT\nEmNyeXB0by1wcm9qZWN0Lnh5ejCCA'
                                      b'SIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoC\n'
                                      b'ggEBALBZv4jJIMVpzcDnVx/5DnoRJQbyCmQ8'
                                      b'95AiQeTXOJdvPPqY4ZyPa5nmJwXc\nepuVOBz'
                                      b'mdIKBCbV9s6bAKf7sGqGoJDII6svUm3kQ4Ba'
                                      b'WbiQDHA1wp4+OwAQmAx4D\n6jaMHt3T6CmA+f'
                                      b'2iw35HsBSBG5UI95ackiAJINpw1WEQvq11zu'
                                      b'bBVtqoFlVWqHzC\nyqnl9oNulGB0amhZ4TVIL'
                                      b'q/nQKrFTZ1une6Zje68nfewnAbHu6QR+FO2G'
                                      b'0gv31x9\nocswqeAG+QRvuQfMMD6i2S1Q/Jlj'
                                      b'F0KZBvKhrSP7r1UXxSv4sjgLb6oFzrR/6/Sm'
                                      b'\nmh42WJRchKuGg5SnU8pOmv9hmR0CAwEAAaO'
                                      b'CAk4wggJKMA4GA1UdDwEB/wQEAwIF\noDAdBg'
                                      b'NVHSUEFjAUBggrBgEFBQcDAQYIKwYBBQUHAw'
                                      b'IwDAYDVR0TAQH/BAIwADAd\nBgNVHQ4EFgQUY'
                                      b'SzpipAsmyq2bGrax70c++ptMVUwHwYDVR0jB'
                                      b'BgwFoAUFC6zF7dY\nVsuuUAlA5h+vnYsUwsYw'
                                      b'VQYIKwYBBQUHAQEESTBHMCEGCCsGAQUFBzAB'
                                      b'hhVodHRw\nOi8vcjMuby5sZW5jci5vcmcwIgY'
                                      b'IKwYBBQUHMAKGFmh0dHA6Ly9yMy5pLmxlbmN'
                                      b'y\nLm9yZy8wHQYDVR0RBBYwFIISY3J5cHRvLX'
                                      b'Byb2plY3QueHl6MEwGA1UdIARFMEMw\nCAYGZ'
                                      b'4EMAQIBMDcGCysGAQQBgt8TAQEBMCgwJgYIK'
                                      b'wYBBQUHAgEWGmh0dHA6Ly9j\ncHMubGV0c2Vu'
                                      b'Y3J5cHQub3JnMIIBBQYKKwYBBAHWeQIEAgSB'
                                      b'9gSB8wDxAHcAKXm+\n8J45OSHwVnOfY6V35b5'
                                      b'XfZxgCvj5TV0mXCVdx4QAAAF9Mt9ZWAAABAM'
                                      b'ASDBGAiEA\n4Y2n9c+Nk+dQg2K0Q7QwkaRCwa'
                                      b'GXSM1Yso3ucc9ZcjcCIQDX1+7VFXLAcjaLIx'
                                      b'eu\n1Gayzeu8dq9PMnmSC4CG3PcWnwB2AG9Td'
                                      b'qwx8DEZ2JkApFEV/3cVHBHZAsEAKQaN\nsgia'
                                      b'N9kTAAABfTLfWqQAAAQDAEcwRQIgAoDWvHK+'
                                      b'I0uKABiYtY+w0TgIK39CyzJN\nTfJfZPvy4sk'
                                      b'CIQCQwOGWf4ja+SfZXFX3BQEguJaKJsGbfqM'
                                      b'uUfYNCJtHHTANBgkq\nhkiG9w0BAQsFAAOCAQ'
                                      b'EAFJJ1/a+6mT5FhzdzFiyxKyqNaGvT0Trs9b'
                                      b'/cCVErqnOR\nb5xakTGGSxpSG8N17mI0uL3AW'
                                      b'lanTxxbT8eIlCb9DmQb3VmIPjBw0O3EiFBEu'
                                      b'I59\nozl+GG8t82uFi0Enya0pRKRnIeZupAhR'
                                      b'qawLLBfas/IGxp0bhnDgrvyM97UUpCqr\ndL4'
                                      b'awAFVI0s4DRwc7t8/QKflDwtFlczJsNAp8bJ'
                                      b'8v/G7vNKus4Ov48KPyS1qkte1\nlDvB4tsVC8'
                                      b'IWuBiit3iB0zGEdRRRpbmv4q0NxRYE8oCX/L'
                                      b'1NqX7sTtoiLQtKdi+v\nHt1I+9dn6JStCbjUh'
                                      b'OGHZYbNE/pCuSYMGl7d30V8HQ==\n-----END'
                                      b' CERTIFICATE-----\n',
                                      b'-----BEGIN CERTIFICATE-----\nMIIFFjCC'
                                      b'Av6gAwIBAgIRAJErCErPDBinU/bWLiWnX1ow'
                                      b'DQYJKoZIhvcNAQELBQAw\nTzELMAkGA1UEBhM'
                                      b'CVVMxKTAnBgNVBAoTIEludGVybmV0IFNlY3V'
                                      b'yaXR5IFJlc2Vh\ncmNoIEdyb3VwMRUwEwYDVQ'
                                      b'QDEwxJU1JHIFJvb3QgWDEwHhcNMjAwOTA0MD'
                                      b'AwMDAw\nWhcNMjUwOTE1MTYwMDAwWjAyMQswC'
                                      b'QYDVQQGEwJVUzEWMBQGA1UEChMNTGV0J3Mg\n'
                                      b'RW5jcnlwdDELMAkGA1UEAxMCUjMwggEiMA0G'
                                      b'CSqGSIb3DQEBAQUAA4IBDwAwggEK\nAoIBAQC'
                                      b'7AhUozPaglNMPEuyNVZLD+ILxmaZ6QoinXSa'
                                      b'qtSu5xUyxr45r+XXIo9cP\nR5QUVTVXjJ6ooj'
                                      b'kZ9YI8QqlObvU7wy7bjcCwXPNZOOftz2nwWg'
                                      b'sbvsCUJCWH+jdx\nsxPnHKzhm+/b5DtFUkWWq'
                                      b'cFTzjTIUu61ru2P3mBw4qVUq7ZtDpelQDRrK'
                                      b'9O8Zutm\nNHz6a4uPVymZ+DAXXbpyb/uBxa3S'
                                      b'hlg9F8fnCbvxK/eG3MHacV3URuPMrSXBiLxg'
                                      b'\nZ3Vms/EY96Jc5lP/Ooi2R6X/ExjqmAl3P51'
                                      b'T+c8B5fWmcBcUr2Ok/5mzk53cU6cG\n/kiFHa'
                                      b'FpriV1uxPMUgP17VGhi9sVAgMBAAGjggEIMI'
                                      b'IBBDAOBgNVHQ8BAf8EBAMC\nAYYwHQYDVR0lB'
                                      b'BYwFAYIKwYBBQUHAwIGCCsGAQUFBwMBMBIGA'
                                      b'1UdEwEB/wQIMAYB\nAf8CAQAwHQYDVR0OBBYE'
                                      b'FBQusxe3WFbLrlAJQOYfr52LFMLGMB8GA1Ud'
                                      b'IwQYMBaA\nFHm0WeZ7tuXkAXOACIjIGlj26Zt'
                                      b'uMDIGCCsGAQUFBwEBBCYwJDAiBggrBgEFBQc'
                                      b'w\nAoYWaHR0cDovL3gxLmkubGVuY3Iub3JnLz'
                                      b'AnBgNVHR8EIDAeMBygGqAYhhZodHRw\nOi8ve'
                                      b'DEuYy5sZW5jci5vcmcvMCIGA1UdIAQbMBkwC'
                                      b'AYGZ4EMAQIBMA0GCysGAQQB\ngt8TAQEBMA0G'
                                      b'CSqGSIb3DQEBCwUAA4ICAQCFyk5HPqP3hUSF'
                                      b'vNVneLKYY611TR6W\nPTNlclQtgaDqw+34IL9'
                                      b'fzLdwALduO/ZelN7kIJ+m74uyA+eitRY8kc6'
                                      b'07TkC53wl\nikfmZW4/RvTZ8M6UK+5UzhK8jC'
                                      b'dLuMGYL6KvzXGRSgi3yLgjewQtCPkIVz6D2Q'
                                      b'Qz\nCkcheAmCJ8MqyJu5zlzyZMjAvnnAT45tR'
                                      b'Axekrsu94sQ4egdRCnbWSDtY7kh+BIm\nlJNX'
                                      b'oB1lBMEKIq4QDUOXoRgffuDghje1WrG9ML+H'
                                      b'bisq/yFOGwXD9RiX8F6sw6W4\navAuvDszue5'
                                      b'L3sz85K+EC4Y/wFVDNvZo4TYXao6Z0f+lQKc'
                                      b'0t8DQYzk1OXVu8rp2\nyJMC6alLbBfODALZvY'
                                      b'H7n7do1AZls4I9d1P4jnkDrQoxB3UqQ9hVl3'
                                      b'LEKQ73xF1O\nyK5GhDDX8oVfGKF5u+decIsH4'
                                      b'YaTw7mP3GFxJSqv3+0lUFJoi5Lc5da149p90'
                                      b'Ids\nhCExroL1+7mryIkXPeFM5TgO9r0rvZaB'
                                      b'FOvV2z0gp35Z0+L4WPlbuEjN/lxPFin+\nHlU'
                                      b'jr8gRsI3qfJOQFy/9rKIJR0Y/8Omwt/8oTWg'
                                      b'y1mdeHmmjk7j1nYsvC9JSQ6Zv\nMldlTTKB3z'
                                      b'hThV1+XWYp6rjd5JW1zbVWEkLNxE7GJThEUG'
                                      b'3szgBVGP7pSWTUTsqX\nnLRbwHOoq7hHwg==\n'
                                      b'-----END CERTIFICATE-----\n',
                                      b'-----BEGIN CERTIFICATE-----\nMIIFYDCC'
                                      b'BEigAwIBAgIQQAF3ITfU6UK47naqPGQKtzAN'
                                      b'BgkqhkiG9w0BAQsFADA/\nMSQwIgYDVQQKExt'
                                      b'EaWdpdGFsIFNpZ25hdHVyZSBUcnVzdCBDby4'
                                      b'xFzAVBgNVBAMT\nDkRTVCBSb290IENBIFgzMB'
                                      b'4XDTIxMDEyMDE5MTQwM1oXDTI0MDkzMDE4MT'
                                      b'QwM1ow\nTzELMAkGA1UEBhMCVVMxKTAnBgNVB'
                                      b'AoTIEludGVybmV0IFNlY3VyaXR5IFJlc2Vh\n'
                                      b'cmNoIEdyb3VwMRUwEwYDVQQDEwxJU1JHIFJv'
                                      b'b3QgWDEwggIiMA0GCSqGSIb3DQEB\nAQUAA4I'
                                      b'CDwAwggIKAoICAQCt6CRz9BQ385ueK1coHIe'
                                      b'+3LffOJCMbjzmV6B493XC\nov71am72AE8o29'
                                      b'5ohmxEk7axY/0UEmu/H9LqMZshftEzPLpI9d'
                                      b'1537O4/xLxIZpL\nwYqGcWlKZmZsj348cL+tK'
                                      b'SIG8+TA5oCu4kuPt5l+lAOf00eXfJlII1PoO'
                                      b'K5PCm+D\nLtFJV4yAdLbaL9A4jXsDcCEbdfIw'
                                      b'PPqPrt3aY6vrFk/CjhFLfs8L6P+1dy70sntK'
                                      b'\n4EwSJQxwjQMpoOFTJOwT2e4ZvxCzSow/iaN'
                                      b'hUd6shweU9GNx7C7ib1uYgeGJXDR5\nbHbvO5'
                                      b'BieebbpJovJsXQEOEO3tkQjhb7t/eo98flAg'
                                      b'eYjzYIlefiN5YNNnWe+w5y\nsR2bvAP5SQXYg'
                                      b'd0FtCrWQemsAXaVCg/Y39W9Eh81LygXbNKYw'
                                      b'agJZHduRze6zqxZ\nXmidf3LWicUGQSk+WT7d'
                                      b'JvUkyRGnWqNMQB9GoZm1pzpRboY7nn1ypxIF'
                                      b'eFntPlF4\nFQsDj43QLwWyPntKHEtzBRL8xur'
                                      b'gUBN8Q5N0s8p0544fAQjQMNRbcTa0B7rBMDB'
                                      b'c\nSLeCO5imfWCKoqMpgsy6vYMEG6KDA0Gh1g'
                                      b'XxG8K28Kh8hjtGqEgqiNx2mna/H2ql\nPRmP6'
                                      b'zjzZN7IKw0KKP/32+IVQtQi0Cdd4Xn+GOdwi'
                                      b'K1O5tmLOsbdJ1Fu/7xk9TND\nTwIDAQABo4IB'
                                      b'RjCCAUIwDwYDVR0TAQH/BAUwAwEB/zAOBgNV'
                                      b'HQ8BAf8EBAMCAQYw\nSwYIKwYBBQUHAQEEPzA'
                                      b'9MDsGCCsGAQUFBzAChi9odHRwOi8vYXBwcy5'
                                      b'pZGVudHJ1\nc3QuY29tL3Jvb3RzL2RzdHJvb3'
                                      b'RjYXgzLnA3YzAfBgNVHSMEGDAWgBTEp7Gkey'
                                      b'xx\n+tvhS5B1/8QVYIWJEDBUBgNVHSAETTBLM'
                                      b'AgGBmeBDAECATA/BgsrBgEEAYLfEwEB\nATAw'
                                      b'MC4GCCsGAQUFBwIBFiJodHRwOi8vY3BzLnJv'
                                      b'b3QteDEubGV0c2VuY3J5cHQu\nb3JnMDwGA1U'
                                      b'dHwQ1MDMwMaAvoC2GK2h0dHA6Ly9jcmwuaWR'
                                      b'lbnRydXN0LmNvbS9E\nU1RST09UQ0FYM0NSTC'
                                      b'5jcmwwHQYDVR0OBBYEFHm0WeZ7tuXkAXOACI'
                                      b'jIGlj26Ztu\nMA0GCSqGSIb3DQEBCwUAA4IBA'
                                      b'QAKcwBslm7/DlLQrt2M51oGrS+o44+/yQoDF'
                                      b'VDC\n5WxCu2+b9LRPwkSICHXM6webFGJueN7s'
                                      b'J7o5XPWioW5WlHAQU7G75K/QosMrAdSW\n9MU'
                                      b'gNTP52GE24HGNtLi1qoJFlcDyqSMo59ahy2c'
                                      b'I2qBDLKobkx/J3vWraV0T9VuG\nWCLKTVXkcG'
                                      b'dtwlfFRjlBz4pYg1htmf5X6DYO8A4jqv2Il9'
                                      b'DjXA6USbW1FzXSLr9O\nhe8Y4IWS6wY7bCkjC'
                                      b'WDcRQJMEhg76fsO3txE+FiYruq9RUWhiF1my'
                                      b'v4Q6W+CyBFC\nDfvp7OOGAN6dEOM4+qR9sdjo'
                                      b'SYKEBpsr6GtPAQw4dy753ec5\n-----END CE'
                                      b'RTIFICATE-----\n'],
                 'cipher_list': (),
                 'cipher_name': 'TLS_AES_256_GCM_SHA384',
                 'error': None,
                 'id': '0cb3df3e-ae1c-4e54-a82f-99d35cbdd780',
                 'ip_address': ('35.239.113.22', 443),
                 'sni': 'crypto-project.xyz',
                 'source_address': ('172.20.135.2', 47592),
                 'state': 3,
                 'timestamp_end': None,
                 'timestamp_start': 1637830920.899386,
                 'timestamp_tcp_setup': 1637830921.1124866,
                 'timestamp_tls_setup': 1637830921.3294146,
                 'tls': True,
                 'tls_established': True,
                 'tls_version': 'TLSv1.3',
                 'via': None,
                 'via2': None},
 'type': 'http',
 'version': 14,
 'websocket': None}
