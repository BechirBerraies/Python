/* 
String Encode

You are given a string that may contain sequences of consecutive characters.
Create a function to shorten a string by including the character,
then the number of times it appears. 


If final result is not shorter (such as "bb" => "b2" ),
return the original string.
*/

const str1 = "aaaabbcddd";
const expected1 = "a4b2c1d3";

const str2 = "";
const expected2 = "";

const str3 = "a";
const expected3 = "a";

const str4 = "bbcc";
const expected4 = "bbcc";

function encodeStr(str) {
    for(i=0;i<str.length;i++){

        current = str[i]
        counter = 1 
        console.log(str[i], "*******")
        while(current == str[i]){
            counter +=1
            console.log(current,counter);
            i++
        }
    }


}
encodeStr(str1)
encodeStr(str2)
encodeStr(str3)
encodeStr(str4)