// import static org.junit.jupiter.api.Assertions.assertEquals;

// import org.junit.jupiter.api.Test;

/**
Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.

Return any possible rearrangement of s or return "" if not possible.



Example 1:

Input: s = "aab"
Output: "aba"

 1 count freq
 {'a':2, b:1}
Example 2:

Input: s = "aaab"  ab  a   a
Output: ""

1 count freq
 {'a':2, b:1}
First iteration
temp = 'a'  remove a and b from heap and we update ma


1- Count the frequency of each char
2- User our heap to sort the char by freq
3- as long as the heap > 1 
   we remove the 1st and 2st most freq char
   add to temp
   decrease the value in the map


   







 

*/
import java.util.*;

class Main {
  public static void main(String[] args) {
    System.out.println(reorg("aaab"));
  }

  public static String reorg(String s){

  HashMap<Character , Integer> map = new HashMap<>();
    for(char c : s.toCharArray())
      map.put(c, map.getOrDefault(c,0)+1);

    PriorityQueue<Character> qq = new PriorityQueue((n1, n2)-> map.get(n2) - map.get(n1));
    qq.addAll(map.keySet());

    StringBuilder sb = new StringBuilder();

    while(qq.size()>1){
      char c1 = qq.remove();
      char c2 = qq.remove();
      sb.append(c1);
      sb.append(c2);

      map.put(c1, map.get(c1)-1);
      map.put(c2, map.get(c2)-1);

      if(map.get(c1)> 0)
        qq.add(c1);
      if(map.get(c2)> 0)
        qq.add(c2);
    }

    if (!qq.isEmpty()){
      char cn = qq.remove();
      if (map.get(cn)>1)
        return "";
      sb.append(cn);
    }
    return sb.toString();
  }
}