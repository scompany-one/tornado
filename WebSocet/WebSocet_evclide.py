import logging
import tornado.web
import tornado.websocket
from Crypto.CommonEvclide import CommonEvclide
import json

class Websocet_evclide(tornado.websocket.WebSocketHandler):
    req = set() 

    def __init__(self, 
                application,
                request,
                **kwargs):
        
        super().__init__(application, request, **kwargs)
        self._int1 = 0
        self._int2 = 0
        self.on = False

    def get_compression_options(self):
        # Non-None enables compression with default options.
        return {}

    def open(self):
        x_real_ip = self.request.headers.get("X-Real-IP")
        self.ip = x_real_ip or self.request.remote_ip
        Websocet_evclide.req.add(self)
        Websocet_evclide.send_updates()
 
    def on_close(self):
        Websocet_evclide.req.remove(self)

    @classmethod
    def send_updates(cls):
        for waiter in cls.req:
            if waiter.on:
                waiter.on = False
                try:
                    gr = CommonEvclide(waiter._int1, waiter._int2)
                    data = {
                        'k1': str(gr[1]),
                        'k2': str(gr[2])
                    }
                    waiter.write_message(data)

                except:
                    logging.error("Error sending message", exc_info=True)

    def on_message(self, message):
        message = json.loads(message)
        logging.info("Got message %r" % message)
        self._int1 = int(message['k1'])
        self._int2 = int(message['k2'])
        self.on = True

def websocet_tick():
    Websocet_evclide.send_updates()

if __name__ == "__main__":
    pass