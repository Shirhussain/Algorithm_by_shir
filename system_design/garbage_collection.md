Design a Garbage Collector

[g(),h(),,,,,,]

new int[6]

              root (1)
                    g()(1)    h() (1)   i() (0)
      
      
      mem of f() (0)
    i (0)

function f() {
  int i = 100

}
for( i = 0 to 10000) {
  f()
 
}
int j = 101

int[] arr = new int[4]
arr[0] = 102
arr[1] = 103


1.) Search for objects that are no longer referenced
2.) Release these unreferenced objects from memory

1.) Performance
2.) Reliable
3.) Efficient use of memory


Mark and Sweep
--
Mark phase
- Loop around all the roots and you mark every object to true (1)

Sweep phase
- Traverse the entire heap and every object that is marked 0 you clear from memory

Compaction phase
- Traverse the entire heap and start moving objects around so that they all are at the beginning memory locations of the heap
- Set the mark false (0)
--
Between Mark -> Compaction you need to halt execution of the app


Reference Counting


execute (0) -> c (0)
kill (0) -> c (0)

class Game {
  public execute() {
    Character c = new Character("enemy")
    this.kill(c)
    ...
    ...
    
  }

  public void kill(Character c) {
  
  }
  
}

class Character {

}


To optimize Performance
--
The older an object is, the more likely it will survive even longer.
The newer an object is, the more likely that it will not be needed

Generational Garbage Collection

Young Generation

----------------------
|                  |
|                  |
|                  |
--------------------

Old Generation

----------------------
|   obj1           |
|                  |
|                  |
--------------------

Permanent Generation

----------------------
|                  |
|                  |
|                  |
--------------------
