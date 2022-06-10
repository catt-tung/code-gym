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
