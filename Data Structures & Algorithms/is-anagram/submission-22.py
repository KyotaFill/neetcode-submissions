class Solution:
    def isAnagram(self,s, t):
        if len(s)!=len(t):return False
        b=set(t)
        s_fre={}
        t_fre={}
        for i in s:
            if i in t:
                if i not in s_fre:
                    s_fre[i]=1
                else:
                    s_fre[i]+=1
            else:return False
        for i in t:
            if i not in t_fre:
                t_fre[i]=1
            else:
                t_fre[i]+=1
        for key in s_fre:
            if s_fre[key]!=t_fre[key]:return False
        return True