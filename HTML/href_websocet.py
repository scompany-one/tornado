import tornado.web

class WebsocetHandler(tornado.web.RequestHandler):
    def get(self):
        items = {"Web-socet": "websocet"}
        self.render("Websocet.html", title="Мой заголовок", items=items)    

if __name__ == "__main__":
    pass