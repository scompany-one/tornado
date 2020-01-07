import tornado.web

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        items = {"Web-socet": "int_websocet",
            "REST": "int_req"};
        self.render("index.html", title="Мой заголовок", items=items)    

if __name__ == "__main__":
    pass