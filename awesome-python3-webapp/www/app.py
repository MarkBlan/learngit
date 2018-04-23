#import the log module
import logging; logging.basicConfig(level=logging.INFO)
#import the asyncio os json time modules
import asyncio, os, json, time 
#from module import a,b,c
from datetime import datetime
from aiohttp import web

#define the fuctions in this file 

#function index - the default mainpage
def index (request):
    return web.Response(body = b'<h1>Awesome</h1>')

#function init - start the server
@asyncio.coroutine
def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000....')
    return srv



#these are all functions from module asyncio
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
