var http=require('http')
var url=require('url')
var fs=require('fs')
var server=http.createServer(function (req,res){
	res.writeHead(200,{'Content-Type':'text/html'});
	var path=url.parse(req.url).pathname;
	console.log("Here is the path "+path);
	var read=fs.createReadStream(__dirname+'/index.html','utf8');
	read.pipe(res)
}
);
server.listen(3000,'127.0.0.1');
console.log('Server Running at port 3000');
