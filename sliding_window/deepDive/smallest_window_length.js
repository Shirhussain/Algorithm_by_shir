/*
Given a string str, your task is to find the smallest window length that contains all 
the characters of the given string at least one time.


Input: str = "aabcbcdbca"
Output: 4
Explanation: Sub-string -> "dbca"

Input: str = "aaab"
Output: 2
Explanation: Sub-string -> "ab"

[a,b]

Set s = new Set
s.add('a')
s.add('b')
s.add('a')

['a' => 1, 'b' => 43]

Brute Force:
Time = O(n^2)
Space = O(1)
*/

function findSubstring(str) {
  let n = str.length
  
  let answer = n
  
  // Store all distinct chars
  let chars = new Array(26).fill(false)
  for (let i = 0; i < n; i++) {
    chars[str.charCodeAt(i) - 97] = true
  }
  // [a,b,c,d]
  
  for (let i = 0; i < n; i++) {
    let substr = new Array(26).fill(false)
    
    for (let j = i; j < n; j++) {
      substr[str.charcodeAt(j) - 97] = true
    }
    
    for(let i = 0; i < chars.length; i++) {
      if (chars[i] && !substr[i]) {
        break
      }
    }
    answer = Math.min(answer, j - i + 1)
  }
  
}


/*

"aabcbcdbca"
        ^ start
          ^ end
 [a,b,c,d] - chars array
 [a=>1,b=>1,c=>1,d=>0] - substr map
 answer = 4

1.) Expanding phase
 - If not all the distinct chars are in our current window
2.) Contracting phase
 - If all the distinct chars are in our current window
*/




function findSubstring(str) {
  let n = str.length
  
  let answer = n
  
  // Store all distinct chars
  let chars = new Array(26).fill(false)
  for (let i = 0; i < n; i++) {
    chars[str.charCodeAt(i) - 97] = true
    
  }
  
  let dist = chars.length
  
  // [a,b,c,d]
  
  start = 0
  count = 0
  let substr = new Array(26).fill(0)
  
  // Expanding
  for (let i = 0; i < n; i++) {
    substr[str.charCodeAt(i) - 97]++
    
    if (substr[str.charCodeAt(i) - 97] == 1) {
      count++
    }
    
    // Contracting
    while (count == dist) {
      answer = Math.min(answer, i - start + 1)
      substr[str.charCodeAt(start) - 97]--
      if (substr[str.charCodeAt(i) - 97] == 0) {
        count--
      }
    }
  }
  
  return answer
}


/*
 *  Time: O(n)
 *  Space: O(1)
 * /    