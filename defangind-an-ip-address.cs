using System;
public class Solution {
    static void Main() {
        string s = "255.100.50.0";
        string ans = "";
        
        foreach (char i in s)
        {   
            if (i == '.')
            {
                ans += "[.]";
            }
            else
            {
                ans += i;
            }
        }

        Console.WriteLine(ans);

        // WAAAAY FASTER (AND SMARTER)

        s.Replace('.', "[.]");

    }
}