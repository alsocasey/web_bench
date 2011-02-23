#!/usr/bin/env python
import re
import sys
from gevent import wsgi

parts_re = re.compile("^/([^/]+)/([0-9]+)$")
def basic_response(env, start_response):
    txt, num = parts_re.match(env['PATH_INFO']).groups()
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
