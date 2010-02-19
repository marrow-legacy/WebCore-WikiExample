# encoding: utf-8
 
"""Web application root controller."""
 
 
import web.core
 
 
 
class RootController(web.core.Controller):
    def index(self):
        return 'Hello world!'
 
 
if __name__ == '__main__':
    from paste import httpserver
    
    app = web.core.Application.factory(root=RootController, debug=False)
    httpserver.serve(app, host='127.0.0.1', port='8080')
