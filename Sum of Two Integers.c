int getSum(int a, int b) {
    if(a==0)
        return b;
    int sum = a^b;
    int count = (a&b)<<1;
    return getSum(count,sum);
}
