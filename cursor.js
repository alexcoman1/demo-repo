fill(255, 0, 255);

draw = function() {
    background(255, 255, 255);
    ellipse(mouseX, mouseY, 3, 3); 
    var label = mouseX + "," + mouseY;
    text(label, mouseX, mouseY);
};
