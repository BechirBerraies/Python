var strA1 = "ABC";
var strB1 = "abc";
var expected = false;

var strA2 = "ABC";
var strB2 = "abd";
var expected = false;

var strA3 = "ABC";
var strB3 = "bc";
var expected = false;

function caseInsensitiveStringCompare(strA, strB) {
  
}



console.log(caseInsensitiveStringCompare(strA1, strB1))
console.log(caseInsensitiveStringCompare(strA2, strB2))
console.log(caseInsensitiveStringCompare(strA3, strB3))