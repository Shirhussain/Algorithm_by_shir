/* 

Given a rectangular matrix which has only two possible values 'X' and 'O'. 
The values 'X' always appear in form of rectangular islands and these islands
are always row-wise and column-wise separated by at least
one line of 'O's. Note that islands can only be diagonally adjacent. 
Count the number of islands in the given matrix. Examples: 
mat[M][N] = {{'O', 'O', 'O'}, 
             {'X', 'X', 'O'}, 
             {'X', 'X', 'O'}, 
             {'O', 'O', 'X'}, 
             {'O', 'O', 'X'}, 
             {'X', 'X', 'O'} }; 

Output: Number of islands is 3 


for finding corner top left and bottom right 
[[[1,0],[2,1]], [[3,2],[3,3]], [[5,0],[5,1]]] 


mat[M][N] = {{'X', 'O', 'O', 'O', 'O', 'O'}, 
             {'X', 'O', 'X', 'X', 'X', 'X'}, 
             {'O', 'O', 'O', 'O', 'O', 'O'}, 
             {'X', 'X', 'X', 'O', 'X', 'X'}, 
             {'X', 'X', 'X', 'O', 'X', 'X'}, 
             {'O', 'O', 'O', 'O', 'X', 'X'},}; 

Output: Number of islands is 4

*/

const matrix: ("X" | "O")[][] = [
  ["O", "O", "O"],
  ["X", "X", "O"],
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["O", "O", "X"],
  ["X", "X", "O"],
];

const matrix1: ("X" | "O")[][] = [
  ["X", "O", "O", "O", "O", "O"],
  ["X", "O", "X", "X", "X", "X"],
  ["O", "O", "O", "O", "O", "O"],
  ["X", "X", "X", "O", "X", "X"],
  ["X", "X", "X", "O", "X", "X"],
  ["O", "O", "O", "O", "X", "X"],
];

const numberRectangle = (matrix: string[][]) => {
  const m: number = matrix.length;
  const n: number = matrix[0].length;
  let count: number = 0;

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      // if I face a new "x" and the top cell and left cell are "o" then add counter
      //   except I have to handle the first row and first column

      if (
        matrix[i][j] === "X" &&
        (i === 0 || matrix[i - 1][j] === "O") &&
        (j === 0 || matrix[i][j - 1] === "O")
      ) {
        count++;
      }
    }
  }
  return count;
};

console.log(numberRectangle(matrix));
console.log(numberRectangle(matrix1));

/*
for finding corner top left and bottom right 
[[[1,0],[2,1]], [[3,2],[3,3]], [[5,0],[5,1]]] 
*/
type Cell = "X" | "O";
type Coordinate = [number, number];
type Rectangle = [Coordinate, Coordinate];

const findAllRectangle = (matrix: Cell[][]): Rectangle[] => {
  const m = matrix.length;
  const n = matrix[0].length;
  const result: Rectangle[] = [];

  for (let i = 0; i < m; i++) {
    for (let j = 0; j < n; j++) {
      if (
        matrix[i][j] === "X" &&
        (i === 0 || matrix[i - 1][j] === "O") &&
        (j === 0 || matrix[i][j - 1] === "O")
      ) {
        const bottomRight = bottomRightCorner(matrix, i, j);
        result.push([[i, j], bottomRight]);

        // skip columns already included in this rectangle
        j = bottomRight[1];
      }
    }
  }

  return result;
};

const topLeftCorner = (
  matrix: string[][],
  startRow: number,
  startCol: number,
) => {
  const m: number = matrix.length;
  const n: number = matrix[0].length;

  for (let i = startRow; i < m; i++) {
    for (let j = startCol; j < n; j++) {
      // if I face a new "x" and the top cell and left cell are "o" then add counter
      //   except I have to handle the first row and first column

      if (
        matrix[i][j] === "X" &&
        (i === 0 || matrix[i - 1][j] === "O") &&
        (j === 0 || matrix[i][j - 1] === "O")
      ) {
        return [i, j] as Coordinate;
      }
    }
  }
  return null;
};

const bottomRightCorner = (
  matrix: Cell[][],
  row: number,
  col: number,
): Coordinate => {
  const m = matrix.length;
  const n = matrix[0].length;
  let r = row;
  let c = col;

  // expand down
  while (r + 1 < m && matrix[r + 1][col] === "X") r++;

  // expand right (ensure all rows have X)
  while (c + 1 < n) {
    let valid = true;
    for (let i = row; i <= r; i++) {
      if (matrix[i][c + 1] !== "X") {
        valid = false;
        break;
      }
    }
    if (!valid) break;
    c++;
  }

  return [r, c];
};

console.log(findAllRectangle(matrix));
