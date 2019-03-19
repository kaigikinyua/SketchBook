const express=require('express');
const path=require('path');
const bodyParser=require('body-parser');
// done importing modules//

const server=express();
server.set('template engine','ejs');
var urlencodedParser=bodyParser.urlencoded({extended:false});
//done setting server variables//

//requests//
server.get('/',(req,res)=>{
	res.sendFile(path.join(__dirname,'/templates/index.html'));
});

server.post('/',urlencodedParser,(req,res)=>{
	//res.render('userpage.ejs',{ message:"Hello "+req.body.username+" "+req.body.pass});
	if(req.body.username=='antony' && req.body.pass=='jamesbond007'){
		console.log(req.body.username)
		res.redirect('/userpage:'+req.body.username);
	}
});

server.get('/userpage:user',function(req,res){
	console.log(req.query.username);
	res.render('userpage.ejs',{username:"Hello"});
});
server.get('/test',(req,res)=>{
	res.render('test.ejs',{ 
		buttons:[
		{btn:'button one'},
		{btn:'button two'},
		{btn:'Hello Boi'}
		] 
	});
});
server.listen(3000,()=>{console.log('server listening at port 3000')});
