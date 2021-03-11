// Transition banniere
document.addEventListener('readystatechange', event => {

    if (event.target.readyState === "complete") {
        if (location.pathname == '/') {
            setTimeout(() => {
                var max = document.getElementsByClassName("banniere")[0].height;
                let i = 0;
                function slowScroll() {
                    setTimeout(function () {
                        window.scrollTo(0, i);
                        i += 5;
                        if (i < max) {
                            slowScroll();
                        }
                    }, 1)
                }
                slowScroll()
            }, 500);
        } else {
            var max = document.getElementsByClassName("banniere")[0].height;
            window.scrollTo(0, max);
        }
    }
});

// Slider Age
function updateAge(val) {
    document.getElementById('age').value = val;
}
function updateSlide(val) {
    document.getElementById('range').value = val;
}

// Bouton aléatoire
function random() {
    document.getElementById('name').value = "Dan"; // Nom
    document.getElementById('role').value = 't-homme'; // Role
    document.getElementById('datalist').value = 'Maître Suprême'; // Type
    document.getElementById('etoile3').click(); // Difficulté
    document.getElementById('age').value = "19"; // Age
    document.getElementById('range').value = "19"; // Slider
    document.getElementById('pouvoirSpecial').value = 'GameReset'; // Pouvoir Special
    document.getElementById('phraseAccroche').value = 'Ça passe ou ça casse !'; // Phrase d'accroche
    // Change image
    document.getElementById('maitre').style.opacity = "1";
    document.getElementById('characterImg').style.opacity = "0";
}
