#!/usr/bin/python

import api
import aggregator

if __name__ == '__main__':
    from wsgi import app
    app.run()
