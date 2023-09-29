// Auto saved at 15:28:26
#include <stdio.h>
#include <ctype.h>
int main()
{
    char lower, upper;
    printf("enter lowercase: ");
    scanf("&c", lower);
    upper = toupper(lower);
    printf("uppercase= %c", upper);
}