$(document).ready(function() {
    $('.js--wish_list_btn').click(function() {
        var mob_i=$('js--wish_list ion-icon').attr('name');
        if (mob_i=='heart-outline'){
            $('#aka').attr('name','heart');
        }else {
            $('#aka').attr('name','heart-outline');
        }
    })
});