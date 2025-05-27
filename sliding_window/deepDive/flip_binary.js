/*
Give an integer n. We can flip exactly one bit. Write code to find the length of the longest sequence of 1 s you could create. 

Examples: 

Input : 1775         
Output : 8 
Binary representation of 1775 is 11011101111.   11011111111.
After flipping the highlighted bit, we get 
consecutive 8 bits. 11011111111.
Input : 12         
Output : 3 
Input : 15
Output : 5
Input : 71
Output: 4
Binary representation of 71 is 1000111.  1100111, 1010111, 1001111
After flipping the highlighted bit, we get 
consecutive 4 bits. 1001111. 


What about 0? 00000000 -> 1
What about 3? 00000011 -> 3
What about 255? 11111111 -> 8



11011101111

11111101111
  ^
 6

11011111111
      ^
      8

Time complexity: O(n^2)
Space: O(n)
01010101010



Sliding Window

flip = 1
maxlen = 8

11011101111
l
     r

111
l
  r
loop until right reaches length of the binary
  // hunting
  if binary[right] == 0 flip++

  // contracting
  loop if flip > 1
    if binary[left] == 0 flip--
    left++

  maxlen = max(maxlen, right - left + 1)
  right++

  return maxlen
*/

function findMaxOnes(n) {
  let left = 0;
  let right = 0;
  let flip = 0;
  let maxlen = 0;

  let binary = n.toString(2).padStart(32, "0");

  while (right < binary.length) {
    // expansion/hunting
    if (binary[right] === "0") {
      flip++;
    }

    // contracting/catchup
    while (flip > 1) {
      if (binary[left] === "0") {
        flip--;
      }
      left++;
    }

    maxlen = Math.max(maxlen, right - left + 1);
    right++;
  }

  return maxlen;
}

console.log(findMaxOnes(1775)); // 8
console.log(findMaxOnes(71)); // 4
console.log(findMaxOnes(0)); // 1
console.log(findMaxOnes(4294967295)); // 32
