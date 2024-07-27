/*
0) Given a 2D screen arr[][] where each arr[i][j] is an integer representing the color of that pixel, also given the location of a pixel (X, Y) and a color C, the task is to replace the color of the given pixel and all the adjacent same-colored pixels with the given color.

Example: 

Input: 
arr[][] = { 
{1, 1, 1, 1, 1, 1, 1, 1}, 
{1, 1, 1, 1, 1, 1, 0, 0}, 
{1, 0, 0, 1, 1, 0, 1, 1}, 
{1, 2, 2, 2, 2, 0, 1, 0}, 
{1, 1, 1, 2, 2, 0, 1, 0}, 
{1, 1, 1, 2, 2, 2, 2, 0}, 
{1, 1, 1, 1, 1, 2, 1, 1}, 
{1, 1, 1, 1, 1, 2, 2, 1}} 
X = 4, Y = 4, C = 3 
Output: 
1 1 1 1 1 1 1 1 
1 1 1 1 1 1 0 0 
1 0 0 1 1 0 1 1 
1 3 3 3 3 0 1 0 
1 1 1 3 3 0 1 0 
1 1 1 3 3 3 3 0 
1 1 1 1 1 3 1 1 
1 1 1 1 1 3 3 1 


{1, 1, 1, 1, 1, 1, 1, 1}, 
{1, 1, 1, 1, 1, 1, 0, 0}, 
{1, 0, 0, 1, 1, 0, 1, 1}, 
{1, 3, 3, 3, 3, 0, 1, 0}, 
{1, 1, 1, 3, 3, 0, 1, 0}, 
{1, 1, 1, 3, 3, 3, 3, 0}, 
{1, 1, 1, 1, 1, 3, 1, 1}, 
{1, 1, 1, 1, 1, 3, 3, 1}} 

function isValidPixel(screen, x, y, currC) {
  if (screen[x][y] !== currC ||
      x < 0 || x >= screen.length ||
      y < 0 || y >= screen[x].length)
      return false

  return true
}

function floodFill(screen, x, y, c) {
  let q = []
  q.push([x, y])

  let currC = screen[x][y]
  screen[x][y] = c

  while(q.length > 0) {
    let [currX, currY] = q.shift()

    // Top
    if (isValidPixel(screen, currX - 1, currY, currC)) {
      screen[currX - 1][currY] = c
      q.push([currX - 1][currY])
    }
    // Bottom
    if (isValidPixel(screen, currX + 1, currY, currC)) {
      screen[currX + 1][currY] = c
      q.push([currX + 1][currY])
    }

    // Left
    if (isValidPixel(screen, currX, currY - 1, currC)) {
      screen[currX][currY - 1] = c
      q.push([currX][currY - 1])
    }
    // Right
    if (isValidPixel(screen, currX, currY + 1, currC)) {
      screen[currX][currY + 1] = c
      q.push([currX][currY + 1])
    }
  }
}

*/

function isValidPixel(screen, x, y, currC) {
  if (
    x < 0 ||
    x >= screen.length ||
    y < 0 ||
    y >= screen[x].length ||
    screen[x][y] !== currC
  )
    return false;

  return true;
}

function floodFill(screen, x, y, c) {
  let q = [];
  q.push([x, y]);

  let currC = screen[x][y];
  screen[x][y] = c;

  while (q.length > 0) {
    let pair = q.shift();

    let currX = pair[0];

    let currY = pair[1];

    // Top
    if (isValidPixel(screen, currX - 1, currY, currC)) {
      screen[currX - 1][currY] = c;
      q.push([currX - 1, currY]);
    }
    // Bottom
    if (isValidPixel(screen, currX + 1, currY, currC)) {
      screen[currX + 1][currY] = c;
      q.push([currX + 1, currY]);
    }

    // Left
    if (isValidPixel(screen, currX, currY - 1, currC)) {
      screen[currX][currY - 1] = c;
      q.push([currX, currY - 1]);
    }
    // Right
    if (isValidPixel(screen, currX, currY + 1, currC)) {
      screen[currX][currY + 1] = c;
      q.push([currX, currY + 1]);
    }
  }
}

let screen = [
  [1, 1, 1, 1, 1, 1, 1, 1],
  [1, 1, 1, 1, 1, 1, 0, 0],
  [1, 0, 0, 1, 1, 0, 1, 1],
  [1, 2, 2, 2, 2, 0, 1, 0],
  [1, 1, 1, 2, 2, 0, 1, 0],
  [1, 2, 1, 2, 2, 2, 2, 0],
  [1, 2, 1, 1, 1, 2, 1, 1],
  [2, 1, 1, 1, 1, 2, 2, 1],
];

X = 4;
Y = 4;
C = 3;

floodFill(screen, X, Y, C);

console.log(screen);

/*
  1.) X, Y are no longer available. floodFill(screen, prevC, C)
  
  2.) You now have N islands
  
  3.) Problem 0 and 1 with DFS
  
  4.) Swap all gradients of the same color to the corresponding gradient new color
  */
