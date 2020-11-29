function tagForm() {
    blur("main");
    disp("creator");
}

function cancelForm(x) {
    blur("main");
    disp(x);
}

function tagRem(value, mod) {
    valueArr = value.split(',');
    blur("main");
    disp("remover");
    var tName = valueArr[1];
    document.getElementById("comfirMes").innerHTML = "Remove the " + mod + " '" + tName + "'?";
    var obj = valueArr[0];
    if (mod == "tag") {
        var mode = "tacr"
    }
    if (mod == "image") {
        var mode = "imup"
    }
    document.getElementById("comfir").action = mode + "/delete/" + obj + "/";
}

function disp(element) {
    var divta = document.getElementById(element);
    if (divta.style.display == "none" || divta.style.display == "") {
        divta.style.display = "block";
    } else {
        divta.style.display = "none";
    }
}

function blur(div) {
    var disdiv = document.getElementById(div);
    disdiv.classList.toggle("disab");
}

window.onload = function() {
    if (document.getElementsByClassName('errorlist').length) {
        blur("main");
        disp("creator");
    }
}

function chButton(event) {
    var tarButt = event.target;
    console.log(tarButt);
    var current = document.getElementsByClassName("active");
    console.log(current);
    current[0].classList.remove("active");
    tarButt.classList.add("active");
    var dele = document.querySelectorAll(".cont");
    for (i = 0; i < dele.length; i++) {
        var style = getComputedStyle(dele[i]);
        var dp = style.display;
        if (dp !== "none") {
            dele[i].style.display = "none";
        }
    }
    var chil = tarButt.querySelector("p");
    var name = chil.innerHTML.replace(/\s/g, "").toLowerCase().substring(0, 4);
    var elem = document.getElementById(name);
    console.log(elem);
    if (name == "imag") {
        elem.style.display = "flex";
    } else {
        elem.style.display = "block";
    }
}
