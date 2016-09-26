//Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

//Example:
//Given a = 1 and b = 2, return 3.
int getSum(int a, int b) {
    if(a==0)
        return b;
    int sum = a^b;
    int count = (a&b)<<1;
    return getSum(count,sum);
}
