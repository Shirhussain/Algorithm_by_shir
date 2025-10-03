/*

function int[]/list grep(string haystack, string needle)
haystack = "aaabcdddbadddabcdefghi"
           "zyxw"
needle = "abc"

[2,14]

"aaaaa"
"aaa"
[0,1,2]

""
[]

needle = ""
[]

Time: O(h*n) -> O(h)
Space: O(1)
*/

function grep(haystack: string, needle: string) {
  if (haystack.length == 0 || needle.length == 0) {
    return [];
  }

  let result: number[] = [];

  for (let i = 0; i <= haystack.length - needle.length; i++) {
    let j = 0;
    for (; j < needle.length; j++) {
      if (haystack[i + j] != needle[j]) {
        break;
      }
    }

    if (j == needle.length) {
      result.push(i);
    }
  }
  return result;
}

console.log(grep("aaaaa", "aaa"));
console.log(grep("aaabcdddbadddabcdefghi", "abc"));

const grep2 = (haystack: string, needle: string): number[] => {
  if (haystack.length == 0 || needle.length == 0) {
    return [];
  }

  let result: number[] = [];

  for (let i = 0; i <= haystack.length - needle.length; i++) {
    if (haystack.substring(i, i + needle.length) == needle) {
      result.push(i);
    }
  }
  return result;
};

console.log(grep2("aaaaa", "aaa"));
console.log(grep2("aaabcdddbadddabcdefghi", "abc"));

/*
  haystack = "aaaaa"
                i
                  i+j
  needle = "aaa"
              j
  result = [0,1,2]
  
  "abc" == "abc"
  O(n)
  
  123 == 123
  O(1)
  
  
  "abc" => 97*256**2 + 98*256**1 + 99*256**0 
  
  "aaa" => 97*256**2 + 97*256**1 + 97*256**0
  =>
  "aab" => (hash("aaa") - 97*256**2) * 256 + 98*256**0
  
  "zyx" => 'z'*256**2 + 'y'*256**1 + 'x'*256**0
  =>
  "yxw" => (hash('zyx') - 'z'*256**2)*256 + 'w'*256**0
  
  XXXXXXXX XXXXXXXX XXXXXXXX XXXXXXXX
              a0       a1         a2
              a1      a2        b
              z.      y.        x
              y.      x.        w
  
                   'a'.charCodeAt() => 97
           'b'.charCodeAt() => 98
           'c'.charCodeAt() => 99
  
  
  0,1,2,3,4,5,6,7,8,9 => 10
  '123' => 1*10**2 + 2*10**1 + 3*10**0 => 123
  
  */
