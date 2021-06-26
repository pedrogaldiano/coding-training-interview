# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        while r >= l:
            print(l, r)
            mid = (r - l) // 2 + l

            if isBadVersion(mid):
                r = mid -1
            else:
                l = mid + 1
        return l
    