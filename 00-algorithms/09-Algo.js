/* 
Parens Valid

Given an str that has parenthesis in it
return whether the parenthesis are valid

Determines whether the parenthesis in the given string are valid.
 * Each opening parenthesis must have exactly one closing parenthesis.
*/

const str1 = "Y(3(p)p(3)r)s";
const expected1 = true;

const str2 = "N(0(p)3";
const expected2 = false;
// Explanation: not every parenthesis is closed.

const str3 = "N(0)t ) 0(k";
const expected3 = false;
// Explanation: because the second ")" is premature: there is nothing open for it to close.

const str4 = "a(b))(c";
const expected4 = false;
// Explanation: same number of opens and closes but the 2nd closing closes nothing.

function closing(str){
    counter= 0
    counter2 = 0
    for (i= 0; i<str.length; i++){
        if (str[i] == "(" ){
            counter += 1 
        }
        if (str[i] ==")"){
            counter2 += 1 
        }
    }
    
    if (counter == counter2 ){
        return true
    }
    if (counter != counter2){
        return false
    }
    console.log(counter);
    console.log(counter2);
}

console.log(closing(str1));
console.log(closing(str2));
console.log(closing(str3));
console.log(closing(str4));
