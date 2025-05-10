/*
                          7
                    -5/    -3/    -4 \      -7\
                    2       4        3        0 
                / / \ \   / / \ \   / / \ \    / / \ \
            -3  -1 -2 -5 -1 1 0 -3 -2 0 -1 -4 -5-3 -4 -7  

*/
const canSum = (arr: number[], number: number): boolean => {
  if (number === 0) return true;
  if (number < 0) return false;
  for (let i = 0; i < arr.length; i++) {
    if (canSum(arr, number - arr[i])) return true;
  }
  return false;
};

console.log(canSum([5, 3, 4, 7], 7));

const canSumMemo = (
  arr: number[],
  number: number,
  memo: { [key: number]: boolean }
): boolean => {
  if (number === 0) return true;
  if (number < 0) return false;

  if (number in memo) return memo[number];

  for (let num of arr) {
    if (canSumMemo(arr, number - num, memo)) {
      memo[number] = true;
      return true;
    }
  }

  memo[number] = false;
  return false;
};

console.log(canSumMemo([5, 3, 4, 700], 700, {}));

const canSumPath = (arr: number[], number: number): number[][] => {
  let result: number[][] = [];

  const backtrack = (arr: number[], number: number, path: number[]) => {
    if (number === 0) {
      result.push(path);
      return null;
    }
    if (number < 0) return null;

    for (let num of arr) {
      backtrack(arr, number - num, [...path, num]);
    }
  };

  backtrack(arr, number, []);

  return result;
};

console.log(canSumPath([5, 3, 4, 7], 14));
