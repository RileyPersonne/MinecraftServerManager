// JAVASCRIPT (jQuery)

// Trigger action when the contexmenu is about to be shown
$(document).bind("contextmenu", function (event) {

    // Avoid the real one
    event.preventDefault();

    // Show contextmenu
    $(".player-menu").finish().toggle(100).

    // In the right position (the mouse)
    css({
        top: event.pageY + "px",
        left: event.pageX + "px"
    });
});


// If the document is clicked somewhere
$(document).bind("mousedown", function (e) {

    // If the clicked element is not the menu
    if (!$(e.target).parents(".player-menu").length > 0) {

        // Hide it
        $(".player-menu").hide(100);
    }
});


// If the menu element is clicked
$(".player-menu li").click(function(){

    // This is the triggered action name
    switch($(this).attr("data-action")) {

        // A case for each action. Your actions here
        case "Ban": alert("Ban"); break;
        case "Mute": alert("Mute"); break;
        case "Kick": alert("Kick"); break;
        case "Message": alert("Message"); break;
        case "Details": alert("Details"); break;
    }

    // Hide it AFTER the action was triggered
    $(".player-menu").hide(100);
  });