""" 
Minimum Window Substring

Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


""" 

public class Solution {
    public string MinWindow(string s, string t) {
        var mapT = new Dictionary<char,int>();
        var mapS = new Dictionary<char,int>();
        //precompute T
        foreach(var c in t)
            if(mapT.ContainsKey(c))
                mapT[c]++;
            else
                mapT.Add(c,1);
        
        var left = 0;
        var startIndex = -1;
        var endIndex = -1;
        var globalMin = Int32.MaxValue;
        for(var i=0;i<s.Length;i++)
        {
            var c = s[i];
            if(mapS.ContainsKey(c))
                mapS[c]++;
            else
                mapS.Add(c,1);
            
            while(left <= i && AllTinS(mapT,mapS))
            {
                mapS[s[left]]--;
                left++;
                Console.WriteLine(left);
            }

            if (left > 0)
            {
                if(i-left + 2 < globalMin)
                {
                    globalMin = i-left + 2;
                    startIndex = left - 1;
                    endIndex = i;
                }
            }
        }
        return globalMin == Int32.MaxValue ? "" : s.Substring(startIndex, endIndex - startIndex+1);
    }

    private bool AllTinS(Dictionary<char,int> mapT, Dictionary<char,int> mapS)
    {
        foreach(var item in mapT)
        {
            if(!mapS.ContainsKey(item.Key)) return false;
            if(item.Value > mapS[item.Key]) return false;
        }
            
        return true;
    }
}