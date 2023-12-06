/*
Longest Substring Without Repeating Characters
Given a string s, find the longest substring without repeating characters.

Input: String
Output: String
Example
Input: abcabcbb      =>	Output: abc
Input: bbbbb	 	=>	Output: b
Input: pwwkew		=>	Output: wke
*/

function longestSubstringWithoutRepeating1(s) {
  let left = 0;
  let charSet = new Set();
  let charMap = new Map();
  let result = "";

  for (let right = 0; right < s.length; right++) {
    // If contraction is needed, do it here until
    // the condition is satisfied.
    while (charSet.has(s[right])) {
      charSet.delete(s[left]);
      left++;
    }
    charSet.add(s[right]);
    charMap[s[right]] = right;

    if (right - left + 1 > result.length) {
      result = s.substring(left, right + 1);
    }
  }
  return result;
}

// console.log(longestSubstringWithoutRepeating("abcabcbb"));
// console.log(longestSubstringWithoutRepeating("bbbbb"));
// console.log(longestSubstringWithoutRepeating("pwwkew"));

// As an optimization, we could just store the left and right index
// for the result instead of copying it.

function longestSubstringWithoutRepeating(s) {
  let left = 0;
  let charMap = new Map();
  let result = "";

  for (let right = 0; right < s.length; right++) {
    // If contraction is needed, do it here until
    // the condition is satisfied.
    if (charMap.has(s[right]) && charMap.get(s[right]) >= left) {
      left = charMap.get(s[right]) + 1;
    }

    charMap.set(s[right], right);

    if (right - left + 1 > result.length) {
      result = s.substring(left, right + 1);
    }
  }
  return result;
}

console.log(longestSubstringWithoutRepeating("abcabcbb"));
console.log(longestSubstringWithoutRepeating("bbbbb"));
console.log(longestSubstringWithoutRepeating("pwwkew"));
