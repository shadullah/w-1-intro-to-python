#include <stdio.h>

int main()
{
    int i = 1;
    int ans = (-5 > -7) ? 0 : 1;
    char name[20] = "bangladesh";
    printf("**%10.6s**\n", name);
    // printf("%d", ans);
    int _regi;
    if (--i)
    {
        printf("%d\n", i++);
        printf("%d\n", (i & 1));
        printf("if= %d\n", i * 2);
    }
    else
    {
        printf(" %d\n", ++i);
        printf(" %d\n", i | 1);
        printf("else= %d\n", i /= 2);
    }
    return 0;
}