/*
Shortest Substring With 3 Unique Characters
Given a string, return the shortest substring that has 3 unique characters, or false if there is no such string

Input: String
Output: String or Boolean
Example
Input: aabaca => Output: bac
Input: abaacc => Output: baac
Input: abc => Output: abc
Input: aabb => Output: False
*/

//     R
// aabaca
//    L
function shortestSubstringWith3UniqueChars(s) {
  let left = 0;
  let charFrequencyMap = new Map();
  let minSubstring = "";
  let minLength = s.length + 1;

  for (let right = 0; right < s.length; right++) {
    let rightChar = s[right];
    // Increment the fequency of rightChar in the map.
    charFrequencyMap.set(rightChar, (charFrequencyMap.get(rightChar) || 0) + 1);

    while (charFrequencyMap.size === 3) {
      // Take a snapshot of the window and keep the minimum one.
      if (right - left + 1 < minLength) {
        minLength = right - left + 1;
        minSubstring = s.substring(left, right + 1);
      }

      // Move the left pointer to the right and update the frequency map.
      let leftChar = s[left];
      // Decrement the fequency of leftChar in the map.
      charFrequencyMap.set(leftChar, charFrequencyMap.get(leftChar) - 1);
      // If the frequency is 0, remove the key from the map.
      if (charFrequencyMap.get(leftChar) === 0) {
        charFrequencyMap.delete(leftChar);
      }
      left++;
    }
  }
  return minSubstring.length >= 3 ? minSubstring : false;
}

console.log(shortestSubstringWith3UniqueChars("aabaca"));
console.log(shortestSubstringWith3UniqueChars("abaacc"));
console.log(shortestSubstringWith3UniqueChars("abc"));
console.log(shortestSubstringWith3UniqueChars("aabb"));
console.log(shortestSubstringWith3UniqueChars("a"));
console.log(shortestSubstringWith3UniqueChars(""));