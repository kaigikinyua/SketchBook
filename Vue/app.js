var search=new Vue({
	el:"#s-box",
	data:{
		item:"search..."
	}
});

var messages=new Vue({
	el:"#chatPage",
	data:{
		messages:[
		{name:"John Doe",message:"Hello World"},
		{name:"Jane Doe",message:"Hello Human"},
		{name:"Mr Robot",message:"Hello Friend"},
		{name:"Jocker",message:"Hello BatMan :)"},
		{name:"BatMan",message:"I am BatMan"}
		],
	}
});