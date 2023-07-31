/* 
  Given a string that may have extra spaces at the start and the end,
  return a new string that has the extra spaces at the start and the end trimmed (removed)
  do not remove any other spaces.
*/

const str1 = "----hello world----";
const expected1 = "hello world";


function trim(str) {
    result = ""
    for (i=0; i< str.length ; i++){
        
        result += str[i]
    }
    return result
}


console.log(trim(str1))
