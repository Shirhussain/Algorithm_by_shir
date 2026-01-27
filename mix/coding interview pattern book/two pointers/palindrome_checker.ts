/*
125. Valid Palindrome
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


*/

function isPalindrome(s: string): boolean {
  let l = 0;
  let r = s.length - 1;

  //   or if you want you can check with the ASCI character code as will in this function
  const isAlphaNum = (c: string) => /^[a-zA-Z0-9]/.test(c);

  while (l < r) {
    if (!isAlphaNum(s[l])) {
      l += 1;
      continue;
    } else if (!isAlphaNum(s[r])) {
      r -= 1;
      continue;
    } else if (s[l].toLowerCase() !== s[r].toLowerCase()) {
      return false;
    }
    l += 1;
    r -= 1;
  }

  return true;
}

const s = "A man, a plan, a canal: Panama";
console.log(isPalindrome(s));
