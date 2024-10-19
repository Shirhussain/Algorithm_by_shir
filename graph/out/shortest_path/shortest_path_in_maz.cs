
     * Complete the function below.
     */
    static int[][] find_shortest_path(string[] grid) {
        //find starting point
        //do BFS and store parent child path
        //navigate the path
        
        var startPoint = FindStartPoint(grid);
        var visited = new HashSet<(int y,int x,int keyRing)>();
        var parents = new Dictionary<(int y, int x, int keyRing),(int y,int x, int keyRing)>();
        var q = new Queue<(int y,int x,int keyRing)>();
        q.Enqueue(startPoint);
        visited.Add(startPoint);
        
        (int y, int x, int keyRing) endPoint = (0,0,0);
        while(q.Count > 0)
        {
            var cell = q.Dequeue();
            //check if it's end point
            if(grid[cell.y][cell.x] == '+')
            {
                endPoint = (cell.y, cell.x, cell.keyRing);
                break;
            }
            foreach(var neighbor in GetNeighbors(grid, cell))
            {
                if(visited.Contains(neighbor)) continue;
                visited.Add(neighbor);
                q.Enqueue(neighbor);
                parents.Add(neighbor, cell);
            }
        }
        
        //get the path
        var result = new List<int[]>();
        var current = endPoint;
        while(true)
        {
            result.Add(new int[]{current.y, current.x});
            current = parents[current];
            if (current.CompareTo(startPoint) == 0) break;
        }
         result.Add(new int[]{current.y, current.x});
         result.Reverse();
         return result.ToArray();
    }
    
    static (int y, int x, int keyRing) FindStartPoint(string[] grid)
    {
        for(int y = 0; y< grid.Length;y++)
         for(int x = 0;x < grid[0].Length;x++)
            if(grid[y][x] == '@') return (y,x,0);
        
        return (0,0,0);
    }
    
    static List<(int y, int x, int keyRing)> GetNeighbors(string[] grid, (int y, int x, int keyRing) current)
    {
        var result = new List<(int y,int x, int keyRing)>();
        var directions = new List<(int y,int x)>{
            {(1,0)},{(-1,0)},{(0,1)},{(0,-1)}
        };
        foreach(var direction in directions)
        {
            var y = current.y + direction.y;
            var x = current.x + direction.x;
            var keyRing = current.keyRing;
            
            if(y > grid.Length - 1 || y < 0 || x > grid[0].Length-1 || x < 0 || grid[y][x] == '#') continue;
            //if it's door, need to check key
            var cell = grid[y][x];
            if("ABCDEFGHIJKLMNOPQRSTUVWXYZ".Contains(cell))
            {
                var keyExist = keyRing & (1 << (cell - 'A'));
                if(keyExist == 0) continue;
            }
            
            //if it's the key, need to add to keyRIng
            if("abcdefghijklmnopqrstuvwxyz".Contains(cell))
            {
                keyRing = keyRing | (1 << (cell - 'A'));
            }
            
            result.Add((y,x,keyRing));
        }
        
        return result;
    }