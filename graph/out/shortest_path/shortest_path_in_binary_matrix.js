/*
Given an MxN matrix with binary values, find the shortest path between a start and destination.

[[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
[ 1, 0, 1, 0, 1, 1, 1, 0, 1, 1 ],
[ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
[ 0, 0, 0, 0, 1, 0, 0, 0, 0, 1 ],
[ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
[ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
[ 1, 0, 0, 0, 0, 0, 0, 0, 0, 1 ],
[ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
[ 1, 1, 0, 0, 0, 0, 1, 0, 0, 1 ]]

start = {0,0}
destination = {3,4}
11

const ROW = 9
const COL = 10

class Coord {
  constructor(x, y) {
    this.x = x
    this.y = y
  }

  function getX() {
    return this.x
  }

function getY() {
  return this.y
}
}

class CoordDist {
  constructor (coord, dist) {
    this.coord = coord
    this.dist = dist
  }

  function getCoord() {
    return this.coord
  }

  function getDist() {
  return this.dist
}
}

function isValidCoord(coord, visited, m) {
  return (coord.getX() >= 0 && coord.getX() < ROW && coord.getY() >= 0 && coord.getY() < COL && !visited[coord.getX()][coord.getY()] && m[coord.getX()][coord.getY()] == 1)
}

function bfs(m, start, dest) {
  // validation
  if (m[start.getX()][start.getY()] != 1 || m[dest.getX()][dest.getY()] != 1 || start.getX() < 0 || dest.getX() < 0 || start.getX() >= ROW || dest.getX() >= ROW || start.getY() < 0 || dest.getY() < 0 || start.getY() >= COL || dest.getY() >= COL) {
    return false
  }

  let visited = new Array(ROW).fill(false).map(() => new Array(COL).fill(false))

  let q = []

  let coord = new CoordDist(start, 0)
  q.push(coord)
  visited[start.getX()][start.getY()] = true

  while (q) {
    // Check are you at destination
    let currentCD = q.shift()
    let currentCoord = currentCD.getCoord()

    if (currentCoord.getX() == dest.getX() && currentCoord.getY() == dest.getY()) {
      return currentCD.getDist()
    }
    
    // up, left, right, down added to the queue as long as they haven't been visited
    let rowDiff = [-1, 0, 1, 0]
    let colDiff = [0, 1, 0, -1]
    for (let i = 0; i < 4; i++) {
      let newX = currentCoord.getX() + rowDiff[i]
      let newY = currentCoord.getY() + colDiff[i]

      let newCoord = new Coord(newX, newY)

      if (isValidCoord(newCoord, visited, m)) {
        visited[newCoord.getX()][newCoord.getY()] = true
        q.push(new CoordDist(newCoord, currentCD.getDist() + 1))
      }
    }
  }

  return false
}

*/

const ROW = 9;
const COL = 10;

class Coord {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  getX() {
    return this.x;
  }

  getY() {
    return this.y;
  }
}

class CoordDist {
  constructor(coord, dist) {
    this.coord = coord;
    this.dist = dist;
  }

  getCoord() {
    return this.coord;
  }

  getDist() {
    return this.dist;
  }
}

function isValidCoord(coord, visited, m) {
  return (
    coord.getX() >= 0 &&
    coord.getX() < ROW &&
    coord.getY() >= 0 &&
    coord.getY() < COL &&
    !visited[coord.getX()][coord.getY()] &&
    m[coord.getX()][coord.getY()] == 1
  );
}

function bfs(m, start, dest) {
  // validation
  if (
    m[start.getX()][start.getY()] != 1 ||
    m[dest.getX()][dest.getY()] != 1 ||
    start.getX() < 0 ||
    dest.getX() < 0 ||
    start.getX() >= ROW ||
    dest.getX() >= ROW ||
    start.getY() < 0 ||
    dest.getY() < 0 ||
    start.getY() >= COL ||
    dest.getY() >= COL
  ) {
    return false;
  }

  let visited = new Array(ROW)
    .fill(false)
    .map(() => new Array(COL).fill(false));

  let q = [];

  let coord = new CoordDist(start, 0);
  q.push(coord);
  visited[start.getX()][start.getY()] = true;

  while (q.length > 0) {
    // Check are you at destination
    let currentCD = q.shift();

    let currentCoord = currentCD.getCoord();

    if (
      currentCoord.getX() == dest.getX() &&
      currentCoord.getY() == dest.getY()
    ) {
      return currentCD.getDist();
    }

    // up, left, right, down added to the queue as long as they haven't been visited
    let rowDiff = [-1, 0, 1, 0];
    let colDiff = [0, 1, 0, -1];
    for (let i = 0; i < 4; i++) {
      let newX = currentCoord.getX() + rowDiff[i];
      let newY = currentCoord.getY() + colDiff[i];

      let newCoord = new Coord(newX, newY);

      if (isValidCoord(newCoord, visited, m)) {
        visited[newCoord.getX()][newCoord.getY()] = true;
        q.push(new CoordDist(newCoord, currentCD.getDist() + 1));
      }
    }
  }

  return false;
}

m = [
  [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 0, 1, 0, 1],
  [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
  [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
  [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
  [1, 1, 0, 0, 0, 0, 1, 0, 0, 1],
];

start = new Coord(0, 0);
dest = new Coord(0, 0);

console.log(bfs(m, start, dest));
