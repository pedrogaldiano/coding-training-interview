using System;
public class Solution 
{
    public int[] BuildArray(int[] nums) 
    {
        // int[] nums = new int[6] {5,0,1,2,3,4};
        int length = nums.Length;

        int [] ans = new int[length];

        for (int i = 0; i < length; i++)
        {
            ans[i] = nums[nums[i]];
        }

        return ans;    
        
    }
}
