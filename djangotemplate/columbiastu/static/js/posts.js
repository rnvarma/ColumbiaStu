





function makePostImage(imgSrc) {
	var titleDiv = document.createElement("div");
	titleDiv.className = "col-md-2 col-sm-3 text-center";
	var titleLink = document.createElement("a");
	titleLink.className = "story-title";
	titleLink.setAttribute("href", "#");
	var titleImg = document.createElement("img");
	titleImg.className = "post-image img-circle";
	img.setAttribute("src", imgSrc);
	titleLink.appendChild(titleImg);
	titleDiv.appendChild(titleImg);
	return titleDiv
}

function makePostContent(title, ageOfPost) {
	var postDiv = document.createElement("div");
	postDiv.className = "col-md-10 col-sm-9";
	var titleDiv = document.createElement("h3");
	titleDiv.text = title
	postDiv.appendChild(titleDiv);
	var contentDiv = document.createElement("div");
	contentDiv.className = "row";
	var 
}

function makePost(title, ageOfPost, imgSrc) {
	var newRow = document.createElement("div");
	newRow.className = "row";
	newRow.appendChild(document.createElement("br"));
	var titleDiv = makePostImage(imgSrc);
	var contentDiv = makePostContent(title, ageOfPost);
}






<div class="row">    
<br>
<div class="col-md-2 col-sm-3 text-center">
  <a class="story-title" href="#"><img alt="" src="http://api.randomuser.me/portraits/thumb/men/58.jpg" style="width:100px;height:100px" class="img-circle"></a>
</div>
<div class="col-md-10 col-sm-9">
  <h3>Repurpose Content to Reach a Wider Audience</h3>
  <div class="row">
    <div class="col-xs-9">
      <h4><span class="label label-default">97thfloor.com</span></h4><h4>
      <small style="font-family:courier,'new courier';" class="text-muted">2 hours ago  • <a href="#" class="text-muted">Read More</a></small>
      </h4></div>
    <div class="col-xs-3"></div>
  </div>
  <br><br>
</div>
</div>

