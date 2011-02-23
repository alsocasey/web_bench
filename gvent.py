#!/usr/bin/env python
import sys
from gevent import wsgi

def basic_response(env, start_response):
    _, txt, num = env['PATH_INFO'].split('/')
    start_response('200 OK', [('Content-Type', 'text/html')])
    try:
        n = int(num)
    except ValueError:
        return
    return ["%d: %s\n" % (i, txt) for i in xrange(n)]

if __name__ == "__main__":
    port = int(sys.argv[1])
    print 'Serving on %s...' % port
    wsgi.WSGIServer(('', port), basic_response, log=None).serve_forever()
