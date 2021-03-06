import tornado.web, sys, json
import requests

class CryptoHandler(tornado.web.RequestHandler):

    def getAddons(self):
        r = requests.get("http://127.0.0.1:1338/api")
        return r.text

    def get(self):
        addons = json.loads(self.getAddons())
        self.render(
            "crypto.html",
            addons = addons
        )
        return

class GetAddonsHandler(tornado.web.RequestHandler):
    def get(self):
        return

class ViewAddonHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('test')

class CallAddonHandler(tornado.web.RequestHandler):

    def callAddon(self, name, data):
        data = json.dumps(data)
        r = requests.post("http://127.0.0.1:1338/api/{}".format(name), data=data)
        return json.loads(r.text)

    def parseArgs(self):
        data = {}
        for key, arg in enumerate(self.request.arguments):
            data[arg]=self.request.arguments[arg][0]
        return data

    def runCipher(self, name, data):
        addon = self.callAddon(name, data)
        print addon
        self.render(
            "addon_{}.html".format(name),
            addon = addon,
            name = name,
        )
        return

    def get(self, name):
        data = self.parseArgs()
        if data:
            self.runCipher(name, data)
        else:
            self.render(
                "addon_{}.html".format(name),
                addon = "",
                name = name,
            )

    def post(self, name):
        data = self.parseArgs()
        self.runCipher(name, data)
        return
