import logging
import tornado
import tornado.options
import os.path
from tornado.options import define

path = lambda root,*a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=1338, help="", type=int)
tornado.options.parse_command_line()

settings = {

    # ---------------------------------
    # base
    # ---------------------------------

    'debug': True,
    'gzip': True,

    # ---------------------------------
    # logging
    # ---------------------------------
    
    # 'log_function': function_name,

    # ---------------------------------
    # security
    # ---------------------------------
    
    'xsrf_cookies': False,
    'autoescape': "xhtml_escape",

    # ---------------------------------
    # paths
    # ---------------------------------
    'template_path': path(ROOT, "templates"),
    'static_path': path(ROOT, "static"),
    'static_url_prefix': '/static/',
    
    # ---------------------------------
    # auth
    # ---------------------------------
    'cookie_secret': 'uxmRinfK8e7HC59jU4QKAGyEsnecPZHuVGUhmtAqHY5rdScC7FM',
    # 'login_url': '/login/',
    
}