window.onload = function() {
    var gallery = document.getElementById('gallery')
    var dropi = document.getElementById('dropi')

    gallery.onmouseover = function() {
        console.log("gal on");
        appear();
    }
    gallery.onmouseout = function() {
        console.log("gal out");
        countdown = setTimeout(function() {
            disappear();
        }, 2000);
    }
    dropi.onmouseover = function() {
        console.log("drop on");
        clearTimeout(countdown);
    }
    dropi.onmouseout = function () {
        console.log("drop out");
        disappear();
    }
}

function appear() {
    dropi.style.top = "50px";
    dropi.style.opacity = 1;
}

function disappear() {
    dropi.style.opacity = 0;
    setTimeout(function() {
        dropi.style.top = "-500px";
    }, 2000)
}
