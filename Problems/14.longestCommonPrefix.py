class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        
        if "" in strs:
            return ''
        
        prefix = ''
        
        for i in range(max(len(s) for s in strs)):
            try:
                if len(set(s[i] for s in strs)) == 1:
                    prefix += strs[0][i]
                else:
                    break
            except IndexError:
                break

        return prefix
    

if __name__ == '__main__':
    strs = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(strs)) # "fl"

    strs = ["dog","racecar","car"]
    print(Solution().longestCommonPrefix(strs)) # ""

    strs = ["", "b"]
    print(Solution().longestCommonPrefix(strs)) # ""