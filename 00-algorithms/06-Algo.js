/* 
Given a non-empty array of odd length containing ints where every int but one
belongs to a pair (the int is duplicated once)
return the only int that has no matching pair.
*/

const nums1 = [1];
const expectd1 = 1;

const nums2 = [5, 4, 5];
const expectd2 = 4;

const nums3 = [5, 4, 3, 4, 3, 4, 5];
const expectd3 = 4; // there is a pair of 4s but one 4 has no pair.

const nums4 = [5, 2, 6, 2, 3, 1, 6, 3, 2, 5, 2];
const expectd4 = 1;

function oddOccurrencesInArray(nums) {
    freqTAble = makeFrequencyTable(nums)
    for(var key in freqTAble){
        if (freqTAble[key] %2 == 0){
            return freqTable[key]
        }
    }

    }

    var user = {username:"John", age:35}

    // console.log(user.hasOwnProperty('age'));
    // console.log(user.hasOwnProperty('email'));
    
    const arr1 = ["a", "a", "a"];
    const expected1 = {
    a: 3,
    };
    
    const arr2 = ["a", "b", "a", "c", "B", "c", "c", "d"];
    const expected2 = {
    a: 2,
    b: 1,
    c: 3,
    B: 1,
    d: 1,
    };
    
    const arr3 = [];
    const expected3 = {};
    
    function makeFrequencyTable(arr) {
    var expected = {}
    for(var  i=0; i< arr.length;i++){
        // if(expected.hasOwnProperty(arr[i])){
          // expected['a'] --> 3 --> true
          // expected['j'] --> undefined --> false
        if(expected[arr[i]]){
        expected[arr[i]]+=1
          // 
        } else{
        expected[arr[i]] = 1
          // expected['a'] = 1
        }
    }
    console.log(expected);
    return expected
    }
    
    makeFrequencyTable(arr1)
    makeFrequencyTable(arr2)
    makeFrequencyTable(arr3)




console.log(oddOccurrencesInArray(nums1), "should equal", expected1);
console.log(oddOccurrencesInArray(nums2), "should equal", expected2);
console.log(oddOccurrencesInArray(nums3), "should equal", expected3);
console.log(oddOccurrencesInArray(nums4), "should equal", expected4);


