var http=require('http')
var url=require('url')
var fs=require('fs')
var express=require('express')
var server=http.createServer(function (req,res){
	res.writeHead(200,{'Content-Type':'text/html'});
	console.log("Here is the path "+req.url);
	if (req.url=='/apps'){
		var read=fs.createReadStream(__dirname+'/apps.html','utf8');
		read.pipe(res);
	}else if(req.url=='/'){
		var read=fs.createReadStream(__dirname+'/index.html','utf8');
		read.pipe(res);
	}else{
		res.writeHead(200,{'Content-Type':'text/html'});
		res.end('Error');
	}
}
);
server.listen(3000,'127.0.0.1');
console.log('Server Running at port 3000');
