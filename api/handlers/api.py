# imports
import tornado.web, sys, json

# import puzzler, relative path
sys.path.insert(0, '../puzzler')
import puzzler

class getAPIHandler(tornado.web.RequestHandler):
    def get(self):
        addons = puzzler.main.getAddons(False)
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(addons))
        
class callAPIHandler(tornado.web.RequestHandler):

    def get(self, addonName):
        self.write('invalid request method')
        
    def post(self, addonName):
        addon = puzzler.main.getAddon(addonName)
        self.set_header("Content-Type", "application/json")

        data = json.loads(self.request.body)
        
        # expose POST data for debugging
        print data

        # try:
        obj = addon["module"]()
        result = getattr(obj, data["method"])(data)
        output = {
            "method": data["method"],
            "args": data,
            "result": result,
        }
        #except:
        #    output = 'exception: {}'.format(sys.exc_info()[0])

        self.write(output)