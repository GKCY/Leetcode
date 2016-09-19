char findTheDifference(char* s, char* t) {
    int a,b,i;
    a=0,b=0,i=0;
    while(s[i])
    {
        a ^= s[i];
        b ^= t[i];
        i++;
    }
    return a^b^t[i];
}
