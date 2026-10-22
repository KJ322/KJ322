#include <stdio.h>

int highLow(int first, int second);
int countPairs(int num);
void printDashOct(int num);

int highLow(int first, int second)
{
    int upper = first & 0xFFFF0000;
    int lower = second & 0x0000FFFF;
    return upper | lower;
}

int countPairs(int num)
{
    int count = 0;
    int pairs = 0;
    while (num != 0)
    {
        if (num & 1)
        {
            count++;      
        }
        else
        {
            if (count == 2)
            {
                pairs++;
            }
            count = 0;
        }
        num >>= 1;
    }
    if (count == 2)
    {
        pairs++;
    }
    return pairs;
}

void printDashOct(int num)
{
    unsigned int digit = (num >> 30) & 0x3;
    printf("%u", digit);
    for (int i = 27; i >= 0; i -= 3)
    {
        digit = (num >> i) & 0x7;
        printf("-%u", digit);
    }
    printf("\n");
}
