# encoding: utf8
 
"""Web application root controller."""
 
 
import web.core
import datetime
 
from megawiki import model as db
 
 
 
__all__ = ['RootController']


class Article(web.core.RESTMethod):
    def __init__(self, name):
        self.name = name
        self.record = db.session.query(db.Article).get(name)
        super(Article, self).__init__()
    
    def get(self, raw=False):
        record = self.record
        
        if raw:
            web.core.response.content_type = 'text/x-web-textile'
            return record.content if record else ""
        
        return 'megawiki.templates.wiki', dict(
                name = self.name,
                record = record,
                content = record.rendered if record else "<i>No content.</i>"
            )
    
    def post(self, content):
        if not self.record:
            self.record = db.Article(name=self.name)
            db.session.add(self.record)
        
        self.record.content = content
        self.record.modified = datetime.datetime.now()
        
        return self.record.rendered
    
    def delete(self):
        if not self.record:
            raise web.core.http.HTTPSeeOther(location='/')
        
        db.session.delete(self.record)
        raise web.core.http.HTTPSeeOther(location='/') 
 
class RootController(web.core.Controller):
    def index(self):
        raise web.core.http.HTTPSeeOther(location='/WikiHome')
    
    def __lookup__(self, article, *parts, **data):
        try:
            controller = ArticleController(self, unicode(article))
            web.core.request.path_info_pop()
            return controller, parts

        except:
            raise web.core.http.HTTPNotFound()