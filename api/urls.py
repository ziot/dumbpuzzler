from tornado import web
from tornado.web import URLSpec as url
from settings import settings
from utils import include
from handlers import *

urls = [
    url(r"/api", api.getAPIHandler),
    url(r"/api/(.*)", api.callAPIHandler),
]