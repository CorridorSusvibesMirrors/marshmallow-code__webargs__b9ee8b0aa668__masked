"""Webapp2 request argument parsing module.

Example: ::

    import webapp2

    from marshmallow import fields
    from webargs.webobparser import use_args

    hello_args = {
        'name': fields.Str(missing='World')
    }

    class MainPage(webapp2.RequestHandler):

        @use_args(hello_args)
        def get_args(self, args):
            self.response.write('Hello, {name}!'.format(name=args['name']))

        @use_kwargs(hello_args)
        def get_kwargs(self, name=None):
            self.response.write('Hello, {name}!'.format(name=name))

    app = webapp2.WSGIApplication([
        webapp2.Route(r'/hello', MainPage, handler_method='get_args'),
        webapp2.Route(r'/hello_dict', MainPage, handler_method='get_kwargs'),
    ], debug=True)
"""
import webapp2
import webob.multidict

from webargs import core
from webargs.multidictproxy import MultiDictProxy





