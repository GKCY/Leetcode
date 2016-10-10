//Given an integer, write a function to determine if it is a power of three.

//常规做法不列出，这里给出一个取巧的做法。

class Solution {
public:
    bool isPowerOfThree(int n) {
        return n > 0 && (1162261467 % n == 0);
    }
};
