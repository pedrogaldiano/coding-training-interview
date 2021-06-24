class Solution:
    def firstUniqChar(self, s: str) -> int:
        s = list(s)
        count = {}
        for i in s:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1

        for k,v in count.items():
            if v == 1:
                index = s.index(k)
                return index
        return -1
        


x = Solution()
s = 'aabb'
print(x.firstUniqChar(s))