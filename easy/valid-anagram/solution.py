class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dic = {}
        for i in s:
            if i not in s_dic:
                s_dic[i] = 1
            else:
                s_dic[i] += 1
        
        for j in t:
            if j in s_dic:
                s_dic[j] -= 1
                if s_dic[j] == 0:
                    s_dic.pop(j)
            else:
                return False

        return True 