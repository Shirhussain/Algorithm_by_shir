/*

Count all the possible paths from the top left to the bottom right of a M X N matrix with the constraints that from each cell you can either move only to the right or down

  M = 2
  N = 2
  . .
  . .
  
 (0,0) -> (1,0) -> (1,1)
 (0,0) -> (0,1) -> (1,1)

  M = 5
  N = 4
  [1,1], [3,2]
  . . . . .
  . X . . .
  . . . X .
  . . . . .

  1 1 1 1 1
  1 2 3 4 5
  1 3 6 1015
  1 4 102035

  1 3 6 10 15

function numbOfPaths(m, n) {
  var count = Array(m).fill(0).map(x => Array(n).fill(0));

  for (i = 0; i < m; i++) {
    count[i][0] = 1;
  }

  for (i = 0; i < n; i++) {
    count[0][i] = 1;
  }

  for (i = 1; i < m; i++) {
    for (j = 1; j < n; j++) }{
      count[i][j] = count[i - 1][j] + count[i][j - 1];
    }
  }
  return count[m - 1][n - 1];
}

Time: O(M*N)
Space: O(M*N)
*/

function numbOfPaths(m, n) {
    var count = Array(m).fill(0).map(x => Array(n).fill(0));
  
    for (i = 0; i < m; i++) {
      count[i][0] = 1;
    }
  
    for (i = 0; i < n; i++) {
      count[0][i] = 1;
    }
  
    for (i = 1; i < m; i++) {
      for (j = 1; j < n; j++) {
        count[i][j] = count[i - 1][j] + count[i][j - 1];
      }
    }
    return count[m - 1][n - 1];
  }
  
  
  function optimizedNumbOfPaths(m, n) {
    var count = Array.from({length: n}, (_, i) => 0);
    count[0] = 1
  
  
    for (i = 0; i < m; i++) {
      for (j = 1; j < n; j++) {
        count[j] += count[j - 1]
      }
    }
    return count[n - 1];
  }
  
  console.log(optimizedNumbOfPaths(5,4))
  
  /*
  Time: O(N*M)
  Spae: O(N)
    */