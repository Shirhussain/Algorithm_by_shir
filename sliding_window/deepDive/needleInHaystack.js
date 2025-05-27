/*
function int[]/list grep(string haystack, string needle)
haystack = "aaabcdddbbddddabcdefghi"
needle = "abc"
[2,14]

haystack = "" =? []
needle = "" =? []

"aaabcdddbbddddabcdefghi"
  ^ i
  ^ i + j
"abc"
 ^ j

"aaa"
   ^
"aaa"
 ^

 
*/

const { log } = require("console");
const { arrayBuffer } = require("stream/consumers");

function grep(haystack, needle) {
  arr = [];
  if (haystack === "" || needle === "") {
    return [];
  }

  for (let i = 0; i <= haystack.length - needle.length; i++) {
    let j = 0;
    for (; j < needle.length; j++) {
      if (haystack[i + j] !== needle[j]) break;
    }

    if (j === needle.length) {
      arr.push(i);
    }
  }

  return arr;
}

haystack = "aaaa";
needle = "";
console.log(grep(haystack, needle));

/*
Time: O(hn)
Space: O(1)

haystack = "aaabcdddbbddddabcdefghi"
needle = "abc"

"abc" === "abc" ?
O(n)

234 === 234 
O(1)

"abc" => int

a => 97
b => 98
c => 99
d => 100

XXXXXXXX XXXXXXXX XXXXXXXX XXXXXXXX
a        b        c        d

00000000
00000001
00000010
00000011
00000100
00000101
...
11111111 256

"1345" => 1345

1*10**3 + 3*10**2 + 4*10**1 + 5*10**0 = 1345

"abcd" => 97*256**3 + 98*256**2 + 99*256**1 + 100*256**0
2**8 = 256
*/
/*
console.log(97*256**3 + 98*256**2 + 99*256**1 + 100*256**0) //abcd

console.log(97*256**3 + 98*256**2 + 99*256**1 + 101*256**0) //abce

console.log(98*256**3 + 98*256**2 + 99*256**1 + 101*256**0) //bbce
*/

/*
haystack = "aaabcdddbbddddabcdefghi"
needle = "abc"

"aaa" = 97*256**2 + 97*256**1 + 97*256**0
"abc" = 97*256**2 + 98*256**1 + 99*256**0

Calculating "aab" (next window)
(int("aaa") - 97*256**2) * 256 + 98*256**0
 prev win     first char  shift   addding new char
*/

aaa = 97 * 256 ** 2 + 97 * 256 ** 1 + 97 * 256 ** 0; //aaa
console.log(aaa);

aab = aaa - 97 * 256 ** 2;
console.log(aab);
aa = 97 * 256 ** 1 + 97 * 256 ** 0;
console.log(aa);

aab = aab * 256;
console.log(aab);
aa_ = 97 * 256 ** 2 + 97 * 256 ** 1;
console.log(aa_);

aab = aab + 98 * 256 ** 0;
console.log(aab);

// Time: O(h)
