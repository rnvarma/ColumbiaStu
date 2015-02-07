// [score, area category, title, comment, submitted by, time];
var data = [["30", "math", "lerner sucks", "seriously it sucks a lot", "gml2153", "1 day"], ["31", "math", "lerner sucks", "seriously it sucks a lot", "gml2153", "1 day"], ["30", "math", "lerner sucks", "seriously it sucks a lot", "gml2153", "1 day"], ["42", "math", "lerner sucks", "seriously it sucks a lot", "gml2153", "1 day"], ["53", "math", "lerner sucks", "seriously it sucks a lot", "gml2153", "1 day"]];

function makePost(data) {
	var mainRow = document.createElement("div");
	mainRow.className = "row post-row";

	var br = document.createElement("br");
	var leftSection = leftSide(data);
	mainRow.appendChild(leftSection);

	var rightSection = rightSide(data);
	mainRow.appendChild(rightSection);

	return mainRow;
}

function leftSide(data) {
	var leftSection = document.createElement("div");
	leftSection.className = "col-md-3 col-sm-3 text-center";
	var feedback = document.createElement("div");
	feedback.className = "col-md-12 col-sm-12 text-center";
	var feedback_text = document.createTextNode("Feedback Score:");

	var number = document.createElement("div");
	number.className = "col-md-12 col-sm-12 text-center number_count";
	var number_text = document.createTextNode(data[0]);

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

function rightSide(data) {
	var rightSection = document.createElement("div");
	rightSection.className = "col-md-9 col-sm-9";

	var areaCategory = document.createElement("div");
	areaCategory.className = "'col-md-12 col-sm-12' style= 'text-align: left;'";
	var area = document.createElement("div");
	area.className = "categories";
	var area_text = document.createTextNode(data[1] + ":");

	var title = document.createElement("div");
	title.className = "col-md-12 col-sm-12 complain_title";
	var title_text = document.createTextNode(data[2]);

	var comment = document.createElement("div");
	comment.className = "col-md-12 col-sm-12 comment";
	var comment_text = document.createTextNode(data[3]);

	var submitted = document.createElement("div");
	submitted.className = "col-md-12 col-sm-12 submit_by";
	var submit_text = document.createTextNode("submitted by " + data[4] + " " + data[5] +" ago");

	submitted.appendChild(submit_text);
	comment.appendChild(comment_text);
	title.appendChild(title_text);

	area.appendChild(area_text);
	areaCategory.appendChild(area);

	rightSection.appendChild(areaCategory);
	rightSection.appendChild(document.createElement("br"));
	rightSection.appendChild(title);
	rightSection.appendChild(document.createElement("br"));
	rightSection.appendChild(document.createElement("br"));
	rightSection.appendChild(comment);
	rightSection.appendChild(document.createElement("br"));
	rightSection.appendChild(document.createElement("br"));
	rightSection.appendChild(document.createElement("br"));
	rightSection.appendChild(document.createElement("br"));
	rightSection.appendChild(submitted);


	return rightSection;

}

$(document).ready(function() {
	var newsFeed = document.getElementById("newsfeed-head");
	for (var i = 0; i < data.length; i++) {
		post = makePost(data[i]);
		newsFeed.appendChild(post);
		newsFeed.appendChild(document.createElement("hr"));
	}
})




