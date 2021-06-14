
var allblogresp,renderdash;
function renderallblogs(){

$("#allblogs").empty();
		$.ajax({
					  url:blogurl+"blogs/getallblogs/",
					  type:"GET",
					  contentType: "application/json",
					  dataType: "json",
					  success: function(res){
					    allblogresp = res;
					    console.log(allblogresp);
					    for (var k in allblogresp){
					    	renderdash = '';
					    renderdash +='<div class="card">'
						renderdash +=conversiontoimg(allblogresp[k]["image"])
						renderdash +='  <div class="container">'
						renderdash +='    <h4 ><b>'+k+'</b></h4> <div>'
						renderdash +='    <p>Created by <span>'+allblogresp[k]["creator"]+'<span></p>' 
						var date = allblogresp[k]["date"].split(" ");
						renderdash +='    <p>Date '+date[0]+'</p>'
						renderdash +='    <p>'+allblogresp[k]["description"]+'</p> <p onclick="openblog(this)" name="'+k+'" style="color:lightblue" class="gg" class="btn btn-info btn-lg" data-toggle="modal" data-target="#myModal">View Full Post</p>'
						renderdash +='  </div>'
						renderdash +='</div>'
						$("#allblogs").append(renderdash)
					}
					
					  },
					  error: function(e) {
					    console.log(e);
					  },
					});

}

var renderfull;

function openblog(elm) {
  document.getElementById("mySidenav").style.width = "100%";
  rendersidenav(elm.getAttribute("name"));
 
}

function rendersidenav(e){
	console.log(e);
var name = e;
$("#mySidenav").empty();
renderfull='';
   renderfull+='<div class="cont"><a href="javascript:void(0)" class="closebtn" onclick="closeNav()">&times;</a>'
  renderfull+='<div>'
  renderfull+='	<h1>'+name+'</h1>'
  renderfull+='	<h3> Created by '+allblogresp[name]["creator"]+'</h3>'
  renderfull+=conversiontoimg(allblogresp[name]["image"])
  renderfull+='	<p>'+allblogresp[name]["description"]+'</p>'
  renderfull+='	<p>'+allblogresp[name]["detail"]+'</p><br>'
  renderfull+='	<h3>Comments</h3><br>'
  renderfull+='<div class="comment_sec" id="comment_sec">';
  // for(var key in allblogresp[name]["comments"]){
  // 	renderfull+='<h5>'+allblogresp[name]["comments"][key]["creator"]+'</h5><p>'+allblogresp[name]["comments"][key]["comment"]+'</p><br>'
  // }
  renderfull+='</div>';

  renderallcomments(allblogresp[name]["creator"],name);

  renderfull+='</div>';
  renderfull+='<div class="postcomment"><input style="width:50%;height:50px" type="text" id="comment" placeholder="Add comments"> <button style="padding:10px;" onclick="post(this)" name="'+name+'" user="'+allblogresp[name]["creator"]+'">Post</button></div></div>'
$("#mySidenav").append(renderfull);	
}

var commentsresp,commentrender;
function renderallcomments(elm,e){
	$("#comment_sec").empty();
	console.log(elm,e)
	$.ajax({
					  url:blogurl+"blogs/get_comment/"+elm+"/"+e,
					  type:"GET",
					  contentType: "application/json",
					  dataType: "json",
					  success: function(res){
					  	commentsresp = res;
					  	for(var i in commentsresp){
					  	commentrender = '';
  						commentrender+='<div class="sep_comm"><h5>'+commentsresp[i]["creator"]+'</h5><p>'+commentsresp[i]["comment"]+'</p><br></div>'
					  	$("#comment_sec").append(commentrender);
					  	}
					  }

});
}

function post(elm){
		var comm = {
			"comment": $("#comment").val(),
		}
		console.log(comm);
		$.ajax({
					  url:blogurl+"blogs/comment/"+localStorage.getItem("username")+"/"+elm.getAttribute("name"),
					  type:"POST",
					  contentType: "application/json",
					  data:JSON.stringify(comm),
					  dataType: "json",
					  success: function(){
					    
					    // rendersidenav(elm.getAttribute("name"));
					    renderallcomments(elm.getAttribute("user"),elm.getAttribute("name"))
					  },
					  error: function(e) {
					    console.log(e);
					  },
					});
	}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}


function conversiontoimg(con){

	var item_image=con;
	var src = "data:image/jpeg;base64,";
	src += item_image;
	var newImage = document.createElement('img');
	newImage.src = src;
	newImage.width = "1000";
	newImage.height = "600";
	console.log(newImage);
	/*document.querySelector('#imageContainer').innerHTML = newImage.outerHTML;*/
	return newImage.outerHTML;

	}


window.onload = renderallblogs();