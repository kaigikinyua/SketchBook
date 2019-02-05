var express=require('express')
var app=express()
var bodyparser=require('body-parser')
var urlencoded=bodyparser.urlencoded({extended:false});
app.set('view engine','ejs');
app.use('/index',express.static('static'));
app.get('/index',function (req,res){
    res.render('index');
});

app.get('/index/apps',function (req,res){
    res.render('basic');
})
app.listen(3001);
console.log('server running on 3001');