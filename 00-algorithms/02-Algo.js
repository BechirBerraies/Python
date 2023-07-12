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
first = strA.split('')
second = strB.split('') 
    if (strA.length == strB.length){
        for(i=0; i<strA.length; i++){
          if(first[i] == second[i].toUpperCase()){
            return true
          }
        }
        
    }
console.log(expected)
    // compare strings 
}
console.log(caseInsensitiveStringCompare(strA1, strB1))
console.log(caseInsensitiveStringCompare(strA2, strB2))
console.log(caseInsensitiveStringCompare(strA3, strB3))