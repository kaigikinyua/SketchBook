var http=require('http')
var url=require('url')
var fs=require('fs')
var server=http.createServer(function (req,res){
	res.writeHead(200,{'Content-Type':'text/html'});
	console.log("Here is the path "+req.url);
	if(req.url=='/apps'){
		res.writeHead(200,{'Content-Type':'text/html'});
		var myRes=fs.createReadStream(__dirname+'/apps.html','utf8');
		myRes.pipe(res);
	}
	else if(req.url=='/json'){
		var myJson={name:'Kraken',type:'1964 Ford',use:'DragStar'};
		res.writeHead(200,{'Content-Type':'application/json'});
		res.end(JSON.stringify(myJson));
	}
	else{
		res.writeHead(200,{'Content-Type':'text/html'});
		var myRes=fs.createReadStream(__dirname+'/index.html','utf8');
		myRes.pipe(res);
	}
}
).listen(3000,'127.0.0.1');
console.log('Server Running at port 3000');
