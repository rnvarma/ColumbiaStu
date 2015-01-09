





function makePostImage(imgSrc) {
	var titleDiv = document.createElement("div");
	titleDiv.className = "col-md-2 col-sm-3 text-center";
	var titleLink = document.createElement("a");
	titleLink.className = "story-title";
	titleLink.setAttribute("href", "#");
	var titleImg = document.createElement("img");
	titleImg.className = "post-image img-circle";
	titleImg.setAttribute("src", imgSrc);
	titleLink.appendChild(titleImg);
	titleDiv.appendChild(titleImg);
	return titleDiv
}

function makePostTitle(title) {
	var postDiv = document.createElement("div");
	postDiv.className = "col-md-10 col-sm-9";
	var titleDiv = document.createElement("h3");
	titletext = document.createTextNode(title);
	titleDiv.appendChild(titletext);
	postDiv.appendChild(titleDiv);
	return postDiv
}

function makePost(title, imgSrc) {
	var newRow = document.createElement("div");
	newRow.className = "row post-row";
	newRow.appendChild(document.createElement("br"));
	var image = makePostImage(imgSrc);
	var title = makePostTitle(title);
	newRow.appendChild(image);
	newRow.appendChild(title)
	return newRow
}

$(document).ready(function() {
	var newsFeed = document.getElementById("newsfeed-head");
	for (var i = 0; i < 5; i++) {
		post = makePost("Repurpose Content to Reach a Wider Audience",
			"http://api.randomuser.me/portraits/thumb/men/58.jpg");
		newsFeed.appendChild(post);
		newsFeed.appendChild(document.createElement("hr"));
	}
})







