var http = require('http');
var url = require('url');

var server = http.createServer(
    function (request, response) {

	response.writeHead(200, {'Conten-Type':'text/plain'});
	
	var parsedUrl = url.parse(request.url);
        var path = parsedUrl.pathname;
	var parsedPath = /^\/([^\/]+)\/([0-9]+)$/.exec(path);
	
	if (parsedPath === null) {
            response.end("Nothing to see here\n");
        } else {
	    try {
		var n = parseInt(parsedPath[2]);
		var msg = parsedPath[1];
		range(n).forEach(response.write(msg + "\n"));
	    } catch (x) {
		response.end("Error: " + x);
	    }
        }
	
	response.end();
});

server.listen(4000);
console.log('Server running at http://127.0.0.1:4000');