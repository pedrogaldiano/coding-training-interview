public class Solution 
{
    public int MaximumWealth(int[][] accounts) 
    {
        int richest = 0;
        for (int i = 0; i < accounts.Length; i ++)
        {
            int sum = 0;
            for (int j = 0; j < accounts[i].Length; j++)
            {
                sum += accounts[i][j];
            }
            if (sum > richest)
            {
                richest = sum;
            }
        }
        return richest;
    }
}