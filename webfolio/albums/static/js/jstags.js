function tagForm() {
    blur("main");
    disp("creator");
}

function cancelForm(x) {
    blur("main");
    disp(x);
}

function tagRem(value) {
    valueArr = value.split(',');
    blur("main");
    disp("remover");
    var tName = valueArr[1];
    document.getElementById("comfirMes").innerHTML = "Remove the tag '" + tName + "'?";
    var obj = valueArr[0];
    document.getElementById("comfir").action = "tacr/delete/" + obj + "/";
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
