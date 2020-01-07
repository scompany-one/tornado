import tornado.web
import json
import logging
from Crypto.CommonEvclide import CommonEvclide

async def Evclide(a, b):
    return CommonEvclide(a, b)

class EvclideHandler(tornado.web.RequestHandler):
    async def post(self):
        body = self.request.body.decode("UTF8")
        message = json.loads(body)
        logging.info("Got message %r" % message)

        gr = await Evclide(int(message['k1']), int(message['k2']))
        data = {
           'k1': str(gr[1]),
           'k2': str(gr[2])
            }
        self.write(data)

if __name__ == "__main__":
    pass