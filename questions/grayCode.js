/*
Reflected Binary / Gray code

110110
101101


0 000 -> 000
1 001 -> 001
2 010 -> 011
3 011 -> 010
4 100 -> 110
5 101 -> 111
6 110 -> 101
7 111 -> 100

5 XOR 6
101
110
---
011

"5"
101
111

101 >> 1 = 10

01101
01011

001101
01101
-------
01011



XOR
A   B   V
0   0   0
0   1   1
1   0   1
1   1   0

*/

let binary = "01001"; // RB - 01101
let rb = binaryToRb(binary);
console.log(rb);
console.log(rbToBinary(rb));

function binaryToRb(binary) {
  let rb = "";

  rb += binary[0];

  for (let i = 1; i < binary.length; i++) {
    rb += compareBits(binary[i - 1], binary[i]);
  }

  return rb;
}

function rbToBinary(rb) {
  let binary = "";

  binary = rb[0];

  for (let i = 1; i < rb.length; i++) {
    if (rb[i] === "0") {
      binary += binary[i - 1];
    } else {
      binary += flip(binary[i - 1]);
    }
  }
  return binary;
}

function compareBits(x, y) {
  return x == y ? "0" : "1";
}

function flip(b) {
  return b === "0" ? "1" : "0";
}

/*
binaryToRbRecursive(binary)
  let curr, prev
  if binary == 0 return 0

  if (last two bits are opposing each other)
    return 1 + 10 * binaryToRbRecursive(binary / 10)
  else 
    return 0 + 10 * binaryToRbRecursive(binary / 10)


^ -> XOR
*/

console.log(binaryToRbRecursive(11001)); // rb: 10101

function binaryToRbRecursive(binary) {
  let curr, prev;

  if (binary === 0) return 0;

  curr = binary % 10;
  binary = Math.floor(binary / 10);
  prev = binary % 10;

  if (curr == prev) {
    return 10 * binaryToRbRecursive(binary);
  } else {
    return 1 + 10 * binaryToRbRecursive(binary);
  }
}

console.log(binaryToRbBW(5));

function binaryToRbBW(num) {
  return num ^ (num >> 1);
}

// HW
function rbToBinaryRecursive(rb) {
  // Implement this
}

function rbToBinaryBW(rb) {
  // Implement this
}
