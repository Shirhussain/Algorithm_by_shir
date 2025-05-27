//  Compute the power n>=1 of a square matrix A which is m x m.

// (A)^n

// [[1, 1], [1, 0]] * [[1, 1], [1, 0]] *... * [[1, 1], [1, 0]]

const matrix = [[1, 1], [1, 0]];


// Test 1: Power of 1
console.log(matrixPower(matrix, 1));

// Test 2: Power of 5
console.log(matrixPower(matrix, 5));

// Test 3: Power of 8
console.log(matrixPower(matrix, 8));


// matrixPower([[1, 1], [1, 0]], 1) should return [[1, 1], [1, 0]].
// matrixPower([[1, 1], [1, 0]], 5) should return [[8, 5], [5, 3]].
// matrixPower([[1, 1], [1, 0]], 10) should return [[89, 55], [55, 34]].

/*
Approach 1: 
Suppose we have a function called MatrixMultipliation(A, B). Call this function n times.

Runtime complexity: O(n m^3)

Approach 2:
Suppose you want to calculate a number 2 to the power of 8
- Naive solution requires 7 multiplications
- The recursive solution (with memoization) requires only 3 multiplications
We can write 2^8 = ((2^2)^2)^2

Total is 3 multiplications:
2*2
4*4
16*16


Simple number:
a^(2n) = (a^n) ^2
a^(2n+1) = a* (a^n) ^2


MP is matrixPower:
MP(n) = MP(n/2) * MP(n/2).  n is even
Mp(n) = matrix* MP((n-1)/2) * MP((n-1)/2).  n is odd

O(log n  m^3)
*/

function MatrixMultipliation(a, b) {
    const result = [[0, 0], [0, 0]];
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            for (let k = 0; k < 2; k++) {
                result[i][j] += a[i][k] * b[k][j];
            }
        }
    }
    return result;
}

function matrixPower(matrix, n) {
  if (n === 1) {
    return matrix;
  }

  if (n % 2 === 0) {
    const halfPower = matrixPower(matrix, n / 2);
    return MatrixMultipliation(halfPower, halfPower);
  } else {
    const halfPower = matrixPower(matrix, (n-1) / 2);
    const intermediateResult= MatrixMultipliation(halfPower, halfPower);
    return MatrixMultipliation(matrix, intermediateResult);
  }

}


