using System;
public class Solution {
    public int[] RunningSum(int[] nums)  {
        
        int n = nums.Length;
        int[] ans = new int[n];
        int sum = 0;
        for (int i = 0; i < n; i++)
        {   
            sum += nums[i];
            ans[i] = sum;
        }
        return ans;     
    }
}