/*
230 - Non-Consecutive Ones
Given a positive integer n, return an array of all the binary strings of length n that DO NOT contain consecutive 1s.

Input: n (Integer)
Output: [Str] (Array of Strings)
Example
Input: 2
Output: ["00", "01", "10"]

Input: 3
Output: ["000", "001", "010", "100", "101"]

Understand
--
How big can n be? - 10
Can n be 0 or negative? - No


Diagram

n = 3

                                  ""
                "0"                                    "1"
      "00"              "01"                  "10"            
  "000"    "001"     "010"                 "100"   "101"

...
32

2^32
2^31

Pseudocode

function recurse(...) {
  []  // Optional

  helper(...) {
    // Base case
    if(...) {
      ...
      return ...
    }

    // Recursive case
    else or if () {
      helper(...) 
      helper(...)    // optional
      ...
      // computation
    }
  
  }
 
  helper(...)
  return ...
}


function nonconsectiveOnes(n) {
  result = []

  function helper(string) {
    // Base case
    if (string.length === n) {
      result.push(string)
      return
    }

    helper(string + '0')
    if (string[string.length - 1] !== "1")
      helper(string + '1')
  
  }

  helper("")
  return result

}

Code


                            ""
          "0"                                    "1"
"00"              "01"                  "10"   

result = ["00", "01", "10"]
*/

function nonconsectiveOnes(n) {
  result = [];

  function helper(string) {
    // Base case
    if (string.length === n) {
      result.push(string);
      return;
    }

    helper(string + "0");
    if (string[string.length - 1] !== "1") helper(string + "1");
  }

  helper("");
  return result;
}

//console.log(nonconsectiveOnes(100))

/*
Time complexity: O(2**n)
Space complexity: O(2**n)
*/

/*
Fibonacci Sequence
Find the nth fibonacci number

0,1,1,2,3,5,8,13,21...

function fib(n) {
  let num1 = 0, num2 = 1, num3, i

  if (n === 0) {
    return num1
  }

  for (i = 2; i <= n; i++) {
    num3 = num1 + num2
    num1 = num2
    num2 = num3
  }

  return num2
}

Diagram

                0,1,1,2,3,5,8,13,21

                        x
                          
              

Pseudocode

function fibR(n) {
  function helper(i) {
    // Base case
    if (i <= 1) {
      return i
    } 
    return fibR(i - 1) + fibR(i - 2)
  }

  return helper(n)
}

Code


*/

function fibR(n) {
  function helper(i) {
    // Base case
    if (i <= 1) {
      return i;
    }
    return helper(i - 1) + helper(i - 2);
  }

  return helper(n);
}

console.log(fibR(20));
