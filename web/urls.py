from tornado import web
from tornado.web import URLSpec as url
from settings import settings
from utils import include

from handlers import *

urls = [
    url(r"/", main.MainHandler),
    url(r"/static/(.*)", web.StaticFileHandler, {"path": settings.get('static_path')}),
    url(r"/crypto", crypto.CryptoHandler),
    url(r"/crypto/(.*)", crypto.CallAddonHandler),
]