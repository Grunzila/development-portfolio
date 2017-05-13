function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max + 1);
  return Math.floor(Math.random() * (max - min)) + min;
}

var parent = document.querySelector(".blurb");
var children = document.querySelectorAll("#words");
children.length;
parent.removeChild(children[getRandomInt(0, children.length)]);