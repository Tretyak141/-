#include <stdio.h>
#include <stdlib.h>
#include "stack.h"
#define N 100
int main()
{
    int stack[N];
    int top = 0;
    int k, p, q, sum, razn, pro, c, res;
    int i = 10;
    while (((c = getchar()) != '\n') && (c != EOF))
    {
        if (c == ' ')
            continue;
        if ((c != '*') && (c != '+') && (c != '-'))
        {
            k = c-'0';
            while (((c = getchar()) != ' '))
                k = k*i + c-'0';                   
             
            if ((k < 32767) && (k > -32768))
                push(stack, &top, k);
            else 
            {
                printf("Операнд вышел за границы типа Short\n");
                exit(1);

            }
        }
        else 
        {               
            switch (c)
            {
                case '+':
                    p = pop(stack, &top);
                    q = pop(stack, &top);
                    sum = q + p;
                    push (stack, &top, sum); 
                    break;
                case '-':
                    p = pop(stack, &top);
                    q = pop(stack, &top);
                    razn = q - p;
                    push (stack, &top, razn); 
                    break;
                case '*':
                    p = pop(stack, &top);
                    q = pop(stack, &top);
                    pro = q * p;
                    push (stack, &top, pro); 
                    break;
                
                default:
                    break;
            }
        }                     
    }    
    res = pop(stack, &top);
    if ((res < 32767) && (res > -32768))
        printf("%d\n", res);
    else 
        {
            printf("Результат вышел за границы типа Short\n");
            exit(1);
        }
    return 0;
}
