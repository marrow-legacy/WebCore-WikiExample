# encoding: utf-8
 
"""Web application data model."""
 
 
import web.core
import textile
 
from paste.registry import StackedObjectProxy
 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Unicode, UnicodeText, DateTime
 
 
 
__all__ = ['Base', 'prepare', 'Article']
 
 
Base = declarative_base()
metadata = Base.metadata
session = StackedObjectProxy()
 
 
def prepare():
    metadata.create_all()
 
 
class Article(Base):
    __tablename__ = 'articles'
    
    name = Column(Unicode(250), primary_key=True)
    content = Column(UnicodeText)
    modified = Column(DateTime)
    
    @property
    def rendered(self):
        @web.core.cache.cache('wiki', expires=3600)
        def cache(name, date):
            return textile.textile(self.content)
        
        if not self.content:
            return "<i>This article does not exist yet.</i>"
        
        return cache(self.name, self.modified)
