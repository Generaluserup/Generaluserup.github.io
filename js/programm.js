menu.onclick = function myFunction() {

    let x = document.getElementById("myTopnav");

    if (x.className === "topnav"){
        x.className += " responsive";
    }else {
        x.className = "topnav";
    }
}



$(function() {
	
	$("h2").wrapInner("<span>");
	$("h2 br").before("<span class='spacer'>")
		.after("<span class='spacer'>");
});