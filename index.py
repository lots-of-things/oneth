import webapp2
import jinja2
import os

from models import Article

# This just says to load templates from the same directory this file exists in
jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):

  def get(self): 
    """Generate the main index page"""
    articles = Article.all().order(posts.rating)
    template_values = {
      'articles': articles,
    }

    template = jinja_environment.get_template('index.html')
    self.response.out.write(template.render(template_values))

class Article(webapp2.RequestHandler):

  def get(self):
    """Generate a page for a specific article"""
    id = self.request.PARAMS['article_id']
    post = Posts.get_by_id(id)
    template_values = {
      'title': post.title,
      'date': post.date,
      'rating': post.rating,
      'id': post.id,
    }

    template = jinja_environment.get_template('article.html')
    self.response.out.write(template.render(template_values))

# Here we can set up more advanced routing rules
APP = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/article/.*', Article),
], debug=True)

