/*
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

Example 1:      [[1,2],[2,3],[3,4],[2,4]]
Input: events = [[1,2],[2,3],[3,4],[2,4]]
Input: events = [[1,2],[2,3],[[2,4],3,4]] 

1,2]  

     2
     

  |1    |2
        |2      |3
                |3       |4
        |2               |4
Output: 3

Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

1- Sort events by starting time 
2- Create minHeap 
3- Keep track of the currend time 
4- As long as we have events in the array and minHeap is not empty 
   1- set the current time to start the next events
   2- Add starting event to the minHeap, and we join the earliest ending event from the minHeap
   increment our counter base of starting > ending of previous event

*/

import java.util.*;


class Main {
  public static void main(String[] args) {

    int [][] e1 = {{1,2},{2,3},{3,4},{5,9},{6,7}};
    System.out.println(maxEvents(e1));
  }


  public static int maxEvents(int [][] events){
    int res = 0;
     if (events == null)
           return res;

      Arrays.sort(events, (e1, e2)-> Integer.compare(e1[0], e2[0]));
      PriorityQueue<Integer> pq = new PriorityQueue<>();
      int i = 0, time = 0; 
    while (i< events.length  || !pq.isEmpty()){

      if (pq.isEmpty())
        time = events[i][0];
      while(i < events.length && time == events[i][0]){
        pq.add(events[i][1]);
        i++;
      }
      pq.poll();
      res++;
      time++;
      while(!pq.isEmpty() && time > pq.peek())
         pq.poll();
      
    }
    
    
    return res;
  }

  // @Test
  // void addition() {
  //     assertEquals(2, 1 + 1);
  // }
}