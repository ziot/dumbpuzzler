import tornado.web, sys, json

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
            "index.html"
        )
        return
