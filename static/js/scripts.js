$( document ).ready(function() {

    $( "#fecha" ).datepicker({
        dateFormat: "yy-mm-dd"
    });

    $('#trabajo_creator').click(function (e) {
        var $inputs = $('#trabajo_form :input');

        // not sure if you wanted this, but I thought I'd add it.
        // get an associative array of just the values.
        var trabajo = {};
        $inputs.each(function() {
            trabajo[this.name] = $(this).val();
        });

        $.ajax({
            url:"/api/crear_trabajo",
            type:"POST",
            data:trabajo,
            dataType:"text",
            success:function(data){
                close_modal()
                console.log(data);
                agregar_a_tabla(trabajo)
            },
            error: function (data) {
                console.log("Hubo un error")
                console.log(data)
            }
        });
    })

    function close_modal(){
        $('#crearTrabajo').modal('toggle');
    }

    function agregar_a_tabla(trabajo){
        var keys = [], k, i;
        var sorted = {};

        for (k in trabajo) {
            if (trabajo.hasOwnProperty(k)) {
                keys.push(k);
            }
        }

        keys.sort();

        for (i = 0; i < keys.length; i++) {
            k = keys[i];
            sorted[k] = trabajo[k]
        }

        var row = "";
        $.each(sorted, function (key, value) {
            row += "<td>"+value+"</td>"
        });
        var $tr = $('<tr>').append( row );
        $(".tabla_listado").append($tr);
    }
});