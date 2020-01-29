"""Bottle request argument parsing module.

Example: ::

    from bottle import route, run
    from marshmallow import fields
    from webargs.bottleparser import use_args

    hello_args = {
        'name': fields.Str(missing='World')
    }
    @route('/', method='GET', apply=use_args(hello_args))
    def index(args):
        return 'Hello ' + args['name']

    if __name__ == '__main__':
        run(debug=True)
"""
import bottle

from webargs import core
from webargs.multidictproxy import MultiDictProxy




