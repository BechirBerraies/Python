
const str1 = "abcABC";
const expected1 = "abcABC";

const str2 = "helloo";
const expected2 = "helo";

const str3 = "";
const expected3 = "";

const str4 = "aa";
const expected4 = "a";

function stringDedupe(str) {
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
    
stringDedupe(str1)