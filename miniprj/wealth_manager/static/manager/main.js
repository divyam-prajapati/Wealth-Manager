const menu = document.getElementById('menu');
const nav = document.getElementById('nav');

menu.addEventListener('click', function(){
    nav.classList.toggle('visible');
});