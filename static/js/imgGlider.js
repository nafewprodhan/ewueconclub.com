new Glider(document.querySelector('.glider-img'), {
    slidesToShow: 1,
    dots: '.dots',
    draggable: true,
    arrows: {
      prev: '.glider-prev',
      next: '.glider-next'
    },
    autoplay: 2000
});