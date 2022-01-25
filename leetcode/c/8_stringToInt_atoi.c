#include <assert.h>
#include <string.h>
#include <math.h>
#include <stdio.h>

int myAtoi(char *s);

int main()
{
    const int MAX = 2147483647;
    const int MIN = -2147483648;

    int result = myAtoi("1234");
    printf("%d <= \"1234\"\n", result);
    assert(result == 1234);

    result = myAtoi("42");
    printf("%d <= \"42\"\n", result);
    assert(result == 42);

    result = myAtoi("   -42");
    printf("%d <= \"   -42\"\n", result);
    assert(result == -42);

    result = myAtoi("4193 with words");
    printf("%d <= \"4193 with words\"\n", result);
    assert(result == 4193);

    result = myAtoi("avasdva 13143");
    printf("%d <= \"avasdva 13143\"\n", result);
    assert(result == 0);

    result = myAtoi("91283472332");
    assert(result == MAX);
    printf("%d\n", result);

    result = myAtoi("-91283472332");
    printf("%d\n", result);
    assert(result == MIN);

    result = myAtoi("  0000000000012345678");
    assert(result == 12345678);

    result = myAtoi("21474836460");
    assert(result == MAX);

    result = myAtoi("2147483646");
    assert(result == 2147483646);
    printf("%d\n", result);

    result = myAtoi("-2147483648");
    printf("j %d\n", result);
    assert(result == -2147483648);

    result = myAtoi("2147483800");
    assert(result == MAX);
    printf("%d\n", result);

    result = myAtoi("-91283472332");
    assert(result == MIN);
    printf("%d\n", result);

    return 0;
}

#define ASCII_PLUS 43
#define ASCII_MINUS 45
#define ASCII_ZERO 48
#define ASCII_NINE 57
#define ASCII_SPACE 32

void pp(char c)
{
    printf("%c %d\n", c, c);
}

int myAtoi(char *s)
{
    int n = 0;
    int len = strlen(s);
    int neg = 1;
    const int MAX = 2147483647;
    const int MIN = -2147483648;

    int start = 0;
    while (start < len && s[start] == ASCII_SPACE)
    {
        start++;
    }

    if (s[start] == ASCII_MINUS || s[start] == ASCII_PLUS)
    {
        if (s[start] == ASCII_MINUS)
            neg = -1;
        start++;
    }

    if (s[start] < ASCII_ZERO || s[start] > ASCII_NINE)
        return 0;

    while (start < len && s[start] == ASCII_ZERO)
    {
        start++;
    }

    int end = start;

    while (end < len)
    {
        if (s[end] < ASCII_ZERO || s[end] > ASCII_NINE)
        {
            break;
        }
        end++;
    }

    if (end - start > 10 || (end - start == 10 && s[start] > ASCII_ZERO + 2))
    {
        if (neg == -1)
        {
            return MIN;
        }
        else
        {
            return MAX;
        }
    }

    int max = MAX;
    int overflow = 0;
    int d;
    for (; start < end; start++)
    {
        d = (s[start] - ASCII_ZERO) * pow(10, end - start - 1);
        if (d > max)
        {
            overflow = 1;
            break;
        }
        max -= d;
        n += d;
    }

    if (overflow)
    {
        if (neg == 1)
        {
            return MAX;
        }

        if (d >= 8)
            return MIN;

        return -1 * (n + d);
    }

    return n * neg;
}