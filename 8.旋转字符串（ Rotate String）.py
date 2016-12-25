'''
Given a string and an offset, rotate string by offset. (rotate from left to right)

Given "abcdefg".

offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"
'''

class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def change(self,s):
        s.insert(0, s.pop())
        
    def rotateString(self, s, offset):
	    # write you code here
	    if not s:
	        return
	    l = len(s)
	    for i in range(offset % l):
	        self.change(s)
	        
	   
	    
