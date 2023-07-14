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

//LeetCode challenge 1 Two Sum
//Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice.
//need to iterate through the array, starting with the first one adding up then checking if it is equal to the target number, if not, try the next one until it's reached, then print out an array with the indices
var twoSum = function(nums, target) {
  let output = []
  for (let i=0; i<nums.length; i++) {
      let testNum = nums[i]
      for (let j=1; j<nums.length; j++) {
          if (testNum + nums[j] === target && !output.includes(i) && i !== j) {
              output.push(i,j)
          }
      }
  } return output
};

//outcome
//Runtime: 280 ms, faster than 7.66% of JavaScript online submissions for Two Sum.
// Memory Usage: 42.1 MB, less than 92.21% of JavaScript online submissions for Two Sum.
// ^ this is so sad..... here is a good explanation https://www.code-recipe.com/post/two-sum

//here is another solution that makes so much more sense, instead of using two loops just make j = i+1 to avoid the repeat
let twoSum1 = function(nums, target) {
  let final=[];
  for(let i=0;i<nums.length;i++){
      let j=i+1;
      console.log(j,'j');
      while(j<nums.length){
          if(nums[i]+nums[j]===target){
              final.push(i);
              final.push(j);
              return final;
          }
          j++;
      }
  }
};

//and I need to learn hashmap:
var twoSumHashmap = function(nums, target) {
  let matchMap = {};
  for(let i = 0; i < nums.length; i++){
  let compliment = target - nums[i];
      if(compliment in matchMap){
          return [i, matchMap[compliment]]
      }
      matchMap[nums[i]] = i;
  }
};

//Palindrome integer
var isPalindrome = function(x) {
  if (Number.isInteger(x)) {
    if (x.toString().split("").reverse().join("") === x.toString()) {
        return true
    } else return false
  } else return false
};

//Runtime: 204 ms, faster than 80.06% of JavaScript online submissions for Palindrome Number. Memory Usage: 51.5 MB, less than 22.77% of JavaScript online submissions for Palindrome Number.

//Check Uppercase
String.prototype.isUpperCase = function() {
  return String(this) === this.toUpperCase();
}

//running sum
//Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]). Return the running sum of nums.
var runningSum = function(nums) {
  let theSums = [nums[0]]
  for (let i = 1; i < nums.length; i++) {
      theSums.push(nums[i]+theSums[i-1])
  }
  return theSums
}

var runningSumReduce = function(nums) {
  nums.reduce((acc, curr, i, arr) => arr[i] += acc)
  return nums
}

//In progress - pivotIndex
var pivotIndex = function(nums) {
    let toLeft = [];
    let toRight = [];
    let pivIdx = -1;
    for (let i=0; i < nums.length; i++) {
        //left first
        for (let j=i-1; j >= 0; j--) {
            toLeft.push(nums[j])
        }
        for (let k=i+1; k < nums.length; k++) {
            toRight.push(nums[k])
        }
        console.log(toLeft, toRight)
        if (toLeft.reduce((prev, curr) => prev + curr, 0) === toRight.reduce((prev, curr) => prev + curr, 0)) {
            pivIdx = i
            break
        } else {
            toLeft = []
            toRight = []
        }
    } return pivIdx
};

//cat mouse codewars challenge
function catMouse(x){
  let steps = 0
  for (let i = 0; i < x.length; i++){
    if (x.charAt(i) == '.'){
      steps += 1
    }
  }
  if (steps % 3 == 0){
    return 'Escaped!'
  }
  else {
    return 'Caught!'
  }
}