class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        strs.sort(key=lambda x:len(x))
        if len(strs[0]) != len(strs[-1]):
            return len(strs[-1])
        else:
            target = strs[0]
            for i in range(1, len(strs)):
                if strs[i] != target:
                    return len(target)
            return -1
