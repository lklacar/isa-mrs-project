
$(document).ready(function () {
    
    var id = 0;

    $("#add-table-btn").click(function () {
        $("#table-container").append('<div data-id="' + id++ + '" class="ui-widget-content draggable "> <p>Seats: ' + $("#number-of-seats-input").val() + '</p></div>');
        $(".draggable").draggable();
        $("#number-of-seats-input").val("");

    });


});