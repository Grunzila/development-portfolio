function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min)) + min;
}

var parent = document.getElementsByClassName("blurb");
var children = document.getElementsByClassName(".words");
children.length;
children[0] = 'Hangry';
parent.removeChild.children[getRandomInt(0, children.length)];