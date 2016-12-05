//Write a method to replace all spaces in a string with %20. The string is given in a characters array, you can assume it 
//has enough space for replacement and you are given the true length of the string.

//You code should also return the new length of the string after replacement.


public class Solution {
    /**
     * @param string: An array of Char
     * @param length: The true length of the string
     * @return: The true length of new string
     */
    public int replaceBlank(char[] string, int length) {
        // Write your code here
        if(length == 0)
            return 0;
        int num = 0;
        for (int i = 0; i < length; i++)
        {
            if(string[i] == ' ')
                num++;
        }
        int newLen = length + num * 2;
        int j = 1;
        for(int i = length - 1;i >= 0; i--)
        {
            if(string[i] != ' ')
            {
                string[newLen - j] = string[i];
                j++;
            }
            else
            {
                string[newLen - j] = '0';
                j++;
                string[newLen - j] = '2';
                j++;
                string[newLen - j] = '%';
                j++;
            }
        }
        return newLen;
        
    }
}
