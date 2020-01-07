import tornado.escape
import tornado.ioloop
import tornado.options
from tornado import gen
import os.path

from WebSocet.WebSocet_evclide import Websocet_evclide, websocet_tick
from Rest.Request_evclide import EvclideHandler

from HTML.href_index import IndexHandler
from HTML.href_websocet import WebsocetHandler
from HTML.href_request import RequestHandler

from tornado.options import define, options

define("port", default=8080, help="прослушивать на порту", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/int_websocet", WebsocetHandler),
            (r"/int_req", RequestHandler),

            (r"/ws/service", Websocet_evclide),
            
            (r"/hs/req", EvclideHandler)
        ]
        settings = dict(
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            template_path=os.path.join(os.path.dirname(__file__), "Template"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            autoreload=True,
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

def main():
    tornado.options.parse_command_line()
    app = Application()
    app.listen(options.port)
    tornado.ioloop.PeriodicCallback(websocet_tick, 10000).start()
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
