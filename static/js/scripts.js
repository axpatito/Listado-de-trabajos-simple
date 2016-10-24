$( document ).ready(function() {
    $('#trabajo_creator').click(function (e) {
        var $inputs = $('#trabajo_form :input');

        // not sure if you wanted this, but I thought I'd add it.
        // get an associative array of just the values.
        var trabajo = {};
        $inputs.each(function() {
            trabajo[this.name] = $(this).val();
        });
        console.log(trabajo)
    })
});