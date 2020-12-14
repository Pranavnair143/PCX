$(document).ready(function(){
    $('.js--w_heart').click(function() {
        var heart=$('.js--w_heart ion-icon')
        if (heart.attr('name')=='heart'){
            heart.attr('name','heart-outline')
        }
        else {
            heart.attr('name','heart')
        }
    });
    
});