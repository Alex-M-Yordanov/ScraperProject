
var display =0;
function toggleAbout() {
    var aboutText = document.getElementById("aboutText");
    if (display == 0) {
        aboutText.style.display = "block";
        display =1;
    } else {
         aboutText.style.display = "none";
         display =0;
     }
}