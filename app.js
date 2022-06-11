// Codewars 6kyu Replace with Alphabet Position
//In this kata you are required to, given a string, replace every letter with its position in the alphabet. If anything in the text isn't a letter, ignore it and don't return it. "a" = 1, "b" = 2, etc.
//Uses RegEx to remove special characters - resource https://bobbyhadz.com/blog/javascript-remove-special-characters-from-string

function alphabetPosition(text) {
  //first lowercase everything
  //try to use charCodeAt
  let convertedText = text.toUpperCase().split(' ').join('').replace(/[^A-Z]/g, '')
  let arrayNum = []
  for (let i=0; i<convertedText.length; i++) {
      arrayNum.push(convertedText.charCodeAt(i) - 64)
    }
    return arrayNum.join(' ')
}

//other solutions
function alphabetPosition2(text) {
  return text
    .toUpperCase()
    .match(/[a-z]/gi)
    .map( (c) => c.charCodeAt() - 64)
    .join(' ');
}

//--------------------------

//Codewars 6kyu Array.diff
//Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result. It should remove all values from list a, which are present in list b keeping their order.

function arrayDiff(a, b) {
  if (a.length === 0 || b.length === 0) {
    return a
  } else {
    for (let i=0; i<b.length; i++) {
      a = a.filter(elem => elem !== b[i])
    }
  } return a
}

// other solutions:
function array_diff(a, b) {
  return a.filter(e => !b.includes(e));
}
function array_diff2(a, b) {
  b = new Set(b)
  return a.filter(v => !b.has(v))
}
//set??
var array_diff = (a, b) => a.filter(item => b.indexOf(item) < 0)
function array_diff3(a, b) {
  return a.filter(x => b.indexOf(x) == -1);
}
// index of negative?