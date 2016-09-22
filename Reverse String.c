//Write a function that takes a string as input and returns the string reversed.

//Example:
//Given s = "hello", return "olleh".


char* reverseString(char* s) {
    char *result = malloc(sizeof(char)*(strlen(s)+1));
    memset(result,'\0',sizeof(char)*(strlen(s)+1));
    result += strlen(s)-1;
    while(*s != '\0')
        *(result--)=*(s++);
    result += 1;
    return result;
}
