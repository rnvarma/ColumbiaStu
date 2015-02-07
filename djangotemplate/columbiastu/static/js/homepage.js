var top_arr = ["recent", "popular", "ideas", "review", "progress", "completed"];
var side_arr = ["all_ideas", "academics", "athletics", "campus_events", "career_services", "dining_services", "facilities", "health_services", "housing/residential", "student_groups", "technology", "misc", "goals", "barnard", "cc", "seas", "gs", "2015", "2016", "2017", "2018"];

function topBar(){
	$(".top_bar").click(function () {
    	// $("#").toggle("display");
    	// console.log(this.id);
    	for (var i = 0; i < top_arr.length; i++){
    		var obj = document.getElementById(top_arr[i]);
    		obj.style.backgroundColor = "";
			obj.style.color = "";
    	}

    	var current = document.getElementById(this.id);
    	current.style.backgroundColor = "#0F52BA";
		current.style.color = "white";
  	});
}

function sideBar() {
	$(".side_bar").click(function () {
    	// $("#").toggle("display");
    	// console.log(this.id);
    	for (var i = 0; i < side_arr.length; i++){
    		var obj = document.getElementById(side_arr[i]);
    		obj.style.backgroundColor = "";
			obj.style.color = "";
    	}

    	var current = document.getElementById(this.id);
    	current.style.backgroundColor = "#0F52BA";
		current.style.color = "white";
  	});
}

function clickHandlers() {
	topBar();
	sideBar();
}


$(document).ready(function() {
	var recent = document.getElementById("recent");
	recent.style.backgroundColor = "#0F52BA";
	recent.style.color = "white";

	var otherRecent = document.getElementById("all_ideas");
	otherRecent.style.backgroundColor = "#0F52BA";
	otherRecent.style.color = "white";

	clickHandlers();
})




