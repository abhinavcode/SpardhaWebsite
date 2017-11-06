$(document).ready(function(){
    $('#inlist').change(function(){
        if(this.checked)
            $('#hidden').fadeIn('slow');
        else
            $('#hidden').fadeOut('slow');

    });
});