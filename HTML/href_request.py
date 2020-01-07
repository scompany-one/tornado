import tornado.web

class RequestHandler(tornado.web.RequestHandler):
    def get(self):
        items = {"Web-socet": "websocet"}
        self.render("Request.html", title="Мой заголовок", items=items)    

if __name__ == "__main__":
    pass