from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from s2p import app

https = False
print('Success2Pass Server Running')

http_server = HTTPServer(WSGIContainer(app))
if https:
    http_server = HTTPServer(WSGIContainer(app),ssl_options={
           "certfile": os.path.join(os.path.abspath("."), "server.crt"),
           "keyfile": os.path.join(os.path.abspath("."), "server.key")
    })
http_server.listen(5555, address="0.0.0.0")
IOLoop.instance().start()
