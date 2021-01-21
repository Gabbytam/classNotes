// CHALLENGE 1: REVERSE A STRING
// Return a string in reverse
// ex. reverseString('hello') === 'olleh'
function reverseString(str) {
    let rvs = []
    let len = str.length;
    for(let i = 1; i <= len; i++){
        rvs.push(str[len-i])
    }
    return rvs.join('')
    //WITH REVERSE METHOD 
    //return str.split('').reverse().join('')
}

const output = reverseString("javascript");
console.log(output);


// CHALLENGE 2: VALIDATE A PALINDROME
// Return true if palindrome and false if not
// ex. isPalindrome('racecar') === 'true', isPalindrome('hello') == false
function isPalindrome(str) {
    let rvs = str.split('').reverse().join('')
    if (rvs == str){
        return true
    } else {
        return false
    }
}

const output2 = isPalindrome('hello')
//const output2 = isPalindrome('racecar')
console.log(output2)

// CHALLENGE 3: REVERSE AN INTEGER
// Return an integer in reverse
// ex. reverseInt(521) === 125
function reverseInt(int) {
    return Number(int.toString().split('').reverse().join(''))
}

const output3 = reverseInt(521)
console.log(output3)


// CHALLENGE 4: CAPITALIZE LETTERS
// Return a string with the first letter of every word capitalized
// ex. capitalizeLetters('i love javascript') === 'I Love Javascript'
function capitalizeLetters(str) {
    str = str.split(' ')
    let newStr = []
    for(let word of str){
        let firstChar = word.charAt(0).toUpperCase();
        let arr = word.split('')
        arr.splice(0, 1, firstChar)
        newStr.push(arr.join(''))
    }
    return newStr.join(' ')

}

const output4 = capitalizeLetters('i love javascript')
console.log(output4)

// CHALLENGE 5: MAX CHARACTER
// Return the character that is most common in a string
// ex. maxCharacter('javascript') == 'a'
function maxCharacter(str) {
    let letters = {}
    //fill the letters object with letters as keys and value set to 0
    for(let letter of str.split('')){
        letters[letter] = 0;
    }
    //loop through all the letters and compare it to the key, if it matched the key, increase
    for(let letter of str.split('')){
        for(let char of Object.keys(letters)){
            if(letter == char){
                letters[letter]+=1
            }
        }
    }
    //highest is set to the highest value. Object.values returns an array of the values, sort will sort it low to high, and pop will grab the highest value
    let highest = Object.values(letters).sort().pop()
    //call .find on the array of keys to return the key where the value equal to the highest value (letters[key] is equal to the value of current key in object)
    return Object.keys(letters).find(key => letters[key] === highest)
}

//CAMERONS VERSION
// function maxCharacter(str) {
//     chars = str.split('')
//     charObj = {}
//     //loop through all the letters
//     for(char of chars) {
//         //check if the letter is a key in the object, if not, add the key
//         if (!(char in charObj)) {
//             charObj[char] = 1
//         //if the letter is a key in the object already, increase the count
//         } else if (char in charObj) {
//             charObj[char] = charObj[char] + 1
//         }
//     }
// ​    //get the key to the highest value
//     //Object.keys returns an array of all the keys, the reduce is checking through all the VALUES at given key and returning the KEY to the highest value
//     const maxChar = Object.keys(charObj).reduce((a, b) => charObj[a] > charObj[b] ? a : b)
//     return maxChar
// }

const output5 = maxCharacter('javassscript')
console.log(output5)

// CHALLENGE 6: FIZZBUZZ
// Write a program that prints all the numbers from 1 to 100. For multiples of 3, instead of the number, print "Fizz", for multiples of 5 print "Buzz". For numbers which are multiples of both 3 and 5, print "FizzBuzz".
function fizzBuzz() {
    for(let i = 1; i <= 100; i++){
        if(i % 3 == 0 && i % 5 == 0){
            console.log('FizzBuzz');
        } else if(i % 3 == 0){
            console.log('Fizz');
        } else if(i % 5 == 0){
            console.log('Buzz');
        } else {
            console.log(i)
        }
    }
}

//fizzBuzz()
// Call Function
// const output = reverseString("javascript");
// console.log(output);
