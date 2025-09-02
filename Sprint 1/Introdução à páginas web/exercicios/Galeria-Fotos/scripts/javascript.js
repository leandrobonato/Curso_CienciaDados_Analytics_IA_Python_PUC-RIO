const TEMPO = 3000;

var imgIndex = 0;
var timerCarroussel;

onload = inicia;

function inicia() {
    var btnPause = document.getElementById('btnPause');
    btnPause.addEventListener('click', pausa);
    
    var btnPlay = document.getElementById('btnPlay');
    btnPlay.addEventListener('click', play);

    var btnRight = document.getElementById('btnRight');
    btnRight.addEventListener('click', nextImage);

    var btnLeft = document.getElementById('btnLeft');
    btnLeft.addEventListener('click', voltar);
    
    images = [
        'Whac-A-Mole.jpg',
        'arrow-down.png'
    ];
    imagesDescription = [
        'Whac-A-Mole',
        'arrow-down'
    ];

     timerCarroussel = setTimeout(nextImage, TEMPO);
}

function nextImage(){
    imgIndex = imgIndex + 1;
    if (imgIndex >= images.length) imgIndex = 0;
    changeImage(imgIndex);
    clearTimeout(timerCarroussel);
    timerCarroussel = setTimeout(nextImage, TEMPO);
}

function changeImage(imageNumber){
    var image = document.getElementById('photo');
    image.src = 'images/fotos/' + images[imageNumber];
    image.alt = imagesDescription[imageNumber];
    var description = document.getElementById('description');
    description.innerHTML = imagesDescription[imageNumber];
}

function pausa(){
   clearTimeout(timerCarroussel);
}

function play(){
    timerCarroussel = setTimeout(nextImage, TEMPO);
}

function voltar(){
    imgIndex = (imgIndex - 1 + images.length) % images.length;
    changeImage(imgIndex);
    timerCarroussel = setTimeout(nextImage, TEMPO);
} 