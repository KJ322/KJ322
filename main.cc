#include <stdio.h>

int highLow(int, int);
int countPairs(int);
void printDashOct(int);

int main(void)
{
    int p1 = 0x045F3E47;
    int p2 = 0xAB001F23;
    printf("highLow(0x%08x, 0x%08x) returned 0x%08X\n", p1, p2, highLow(0x045F3E47, 0xAB001F23));
    
    p1 = 0xD8000000;
    printf("countpairs(0x%08X) returned %d\n", p1, countPairs(p1));

    p1 = 0xC0000000;
    printf("printDashOct(0x%08X) printed \n", p1);
    printDashOct(p1);

    return 0;
}