'''
516. 最长回文子序列
给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

'''
SOLUTION 1:
执行用时：
576 ms
, 在所有 Python 提交中击败了
99.59%
的用户
内存消耗：
79.2 MB
, 在所有 Python 提交中击败了
5.29%
的用户
'''
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        if l==0:
            return 0
        if l==1:
            return 1
        lf=0
        rt=l-1
        m=[[0]*l for i in range(l)]
        def isleftright(a,b):
            if a>b:
                return 0
            if a==b:
                return 1
            if m[a][b]!=0:
                return m[a][b]
            if s[a]==s[b]:
                res=2+isleftright(a+1,b-1)
                m[a][b]=res
                return res
            else:
                res=max(isleftright(a+1,b),isleftright(a,b-1))
                m[a][b]=res
                return res
        return isleftright(lf,rt)

'''
SOLUTION 2:
执行用时：
944 ms
, 在所有 Python 提交中击败了
73.98%
的用户
内存消耗：
27.4 MB
, 在所有 Python 提交中击败了
84.96%
的用户
'''
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        l=len(s)
        if l==0:
            return 0
        if l==1:
            return 1
        lf=0
        rt=l-1
        m=[[0]*l for i in range(l)]
        for i in range(l):
            m[i][i]=1
        
        for i in range(l-2,-1,-1):
            for j in range(i+1,l):
                if s[i]==s[j]:
                    m[i][j]=2+m[i+1][j-1]
                else:
                    m[i][j]=max(m[i+1][j],m[i][j-1])
        return m[0][l-1]
