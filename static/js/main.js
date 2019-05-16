function CurrentC(Color) {
    color = document.getElementsByClassName("CurrentColor");
    color[0].style.backgroundColor=Color;
}

function gobackto() {
    window.history.back();
}