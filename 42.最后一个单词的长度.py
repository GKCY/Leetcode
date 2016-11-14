
#给定一个字符串， 包含大小写字母、空格' '，请返回其最后一个单词的长度。

#如果不存在最后一个单词，请返回 0 。


class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        # Write your code here
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        
        res = s.split(' ')
        if '' in res:
            res.remove('')
        res = len(res[-1])
        
        return res
