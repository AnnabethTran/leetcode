class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        subStrs = []
        for i in range(len(s)):
            subStr = s[i]
            for j in range(i+1, len(s)):
                if s[j] not in subStr:
                    subStr += s[j]
                else:
                    break
            subStrs.append(subStr)
        lenSubStr = 0
        for s in subStrs:
            if len(s) > lenSubStr:
                lenSubStr = len(s)
        return lenSubStr
