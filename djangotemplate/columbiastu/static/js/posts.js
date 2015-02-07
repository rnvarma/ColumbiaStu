var hello = [];

function makePost() {
	var mainRow = document.createElement("div");
	mainRow.className = "row post-row";

	var br = document.createElement("br");
	var leftSection = leftSide();
	mainRow.appendChild(leftSection);

	var rightSection = rightSide();
	mainRow.appendChild(rightSection);

	return mainRow;
}

function leftSide() {
	var leftSection = document.createElement("div");
	leftSection.className = "col-md-3 col-sm-3 text-center";
	var feedback = document.createElement("div");
	feedback.className = "col-md-12 col-sm-12 text-center";
	var feedback_text = document.createTextNode("Feedback Score:");

	var number = document.createElement("div");
	number.className = "col-md-12 col-sm-12 text-center number_count";
	var number_text = document.createTextNode("69");

	var vote = document.createElement("div");
	vote.className = "col-md-12 col-sm-12 text-center";
	var upvote = document.createElement("div");
	upvote.className = "col-md-6 col-sm-6 text-center";
	var upvote_button = document.createElement("div");
	upvote_button.className = "upvote";
	var upvote_button_text = document.createTextNode("I agree");
	var downvote = document.createElement("div");
	downvote.className = "col-md-6 col-sm-6 text-center";
	var downvote_button = document.createElement("div");
	downvote_button.className = "downvote";
	var downvote_button_text = document.createTextNode("I don't");

	feedback.appendChild(feedback_text);

	number.appendChild(number_text);

	upvote_button.appendChild(upvote_button_text);
	upvote.appendChild(upvote_button);
	downvote_button.appendChild(downvote_button_text);
	downvote.appendChild(downvote_button);
	vote.appendChild(upvote);
	vote.appendChild(downvote);

	leftSection.appendChild(feedback);
	leftSection.appendChild(number);
	leftSection.appendChild(vote);

	return leftSection;

}

function rightSide() {
	var rightSection = document.createElement("div");
	rightSection.className = "col-md-9 col-sm-9";


	return rightSection;

}


// function makePostImage(imgSrc) {
// 	var titleDiv = document.createElement("div");
// 	titleDiv.className = "col-md-2 col-sm-3 text-center";
// 	var titleLink = document.createElement("a");
// 	titleLink.className = "story-title";
// 	titleLink.setAttribute("href", "#");
// 	var titleImg = document.createElement("img");
// 	titleImg.className = "post-image img-circle";
// 	titleImg.setAttribute("src", imgSrc);
// 	titleLink.appendChild(titleImg);
// 	titleDiv.appendChild(titleImg);
// 	return titleDiv
// }

// function makePostTitle(title) {
// 	var postDiv = document.createElement("div");
// 	postDiv.className = "col-md-10 col-sm-9";
// 	var titleDiv = document.createElement("h3");
// 	titletext = document.createTextNode(title);
// 	titleDiv.appendChild(titletext);
// 	postDiv.appendChild(titleDiv);
// 	return postDiv
// }

// function makePost(title, imgSrc) {
// 	var newRow = document.createElement("div");
// 	newRow.className = "row post-row";
// 	newRow.appendChild(document.createElement("br"));
// 	var image = makePostImage(imgSrc);
// 	var title = makePostTitle(title);
// 	newRow.appendChild(image);
// 	newRow.appendChild(title)
// 	return newRow
// }

$(document).ready(function() {
	var newsFeed = document.getElementById("newsfeed-head");
	for (var i = 0; i < 2; i++) {
		post = makePost();
		newsFeed.appendChild(post);
		newsFeed.appendChild(document.createElement("hr"));
	}
})







