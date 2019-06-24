from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from s2p import app
print('Success2Pass Server Running')
http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5555)
IOLoop.instance().start()
