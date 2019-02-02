var express=require('express')
var app=express()
app.set('view engine','ejs');
app.use('/apps',function(res,req,next){
    next();
});
app.get('/apps',function (req,res){
    res.render('basic');
})
app.listen(3001);
console.log('server running on 3001');