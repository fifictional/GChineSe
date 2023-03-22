//$(document).ready(function(){
//  $('.flashcard-container').slick({
//    infinite: true,
//    slidesToShow: 1,
//    slidesToScroll: 1,
//    dots: true,
//    arrows: true,
////    autoplay: true,
//    autoplaySpeed: 2000,
//  });
//});


/*$(document).ready(function(){
  $('.flashcard-container').slick({
    infinite: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    dots: true,
    arrows: true,
    // autoplay: true,
    autoplaySpeed: 2000,
  });

  $('.flashcard-container').css('top', '100px');
});*/

$(document).ready(function(){
  var swiper = new Swiper('.swiper-container', {
    slidesPerView: 1,
    spaceBetween: 100,
    loop: true,
    pagination: {
      el: '.swiper-pagination',
      clickable: true,
    },
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
});


$(document).ready(function () {
    $("#mylist li").has("ul").children("a").on("click", function (e) {
        e.preventDefault();
        $(this).parent().toggleClass("active");
        $(this).siblings("ul").toggleClass("active");
    });
});
