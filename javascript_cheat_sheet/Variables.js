// This is a comment.
/* This is another comment. */

/* There a 6 types of variables/values in JavaScript.
Numbers, Strings, Boolean, Functions, Objects, and Undefined values */


// Numbers
// JS uses 64-bit numbers
// There is not different syntax or different kinds of numbers
// All numbers are signed
a = 11
b = 10.0

// Arithmetic in JS uses PEMDAS
c = a + b // 21
c = a * b // 110
c = a - b // 1
c = a / b // 1.1
c = a % b // 1

// Special numbers
// Infinity and -Infinity represent positive and negative infinities
// NaN is not a number but has a value of number type
// Any numeric calculation that doesn't yeild a precise result will result in NaN

// Strings are used to represent text and can be enclosed in single ('') or double ("") quotes
sentence = 'The quick brown fox jumps over the lazy dog.'
// Plus operator (+) can be used for string concatenation

// Unary operator
// typeof operator returns the type of variable it is given as an operand
typeof sentence // String

// Boolean type in JS has two values true and false
isValid = true

// Operators in JS are the same as operators in other standard languages.
// One of the things to notice is that NaN is a special value and returns false when compared to itself.
NaN == NaN // false

// Logical operators such as &&, ||, ! can be used to reason conditions
isMonday = true
isRaining = false
isMonday && isRaining

// Ternary operators work as well.
a = 3
b = 4
a > b ? a : b // selects b

// JS allows you to do some pretty odd things using 'coercion'
// which is a set of its own rules to deal with unusual situations
console.log(8 * null) // → 0 Treating null as 0
console.log("5" - 1) // → 4 Implicitly converting 5 to number and performing operations
console.log("5" + 1) // → 51 Converting 1 to string and concatenating
console.log("five" * 2) // → NaN Invalid operation
console.log(false == 0) // → true Treating false as 0 and comparing with number 0
console.log(null == undefined); // → true Only true when both sides are null or Undefined

// All these examples indicate automatic type conversions
// But what is you do not want type convetsons? What if you strictly need to compare the actual values?
// JS has === and !== operators to do This
console.log("" == false) // true
console.log("" === false); // false
