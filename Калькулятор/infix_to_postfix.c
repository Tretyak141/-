#include <stdio.h>
#include "stack.h"
#define N 256




int priority(int k){
    switch (k)
    {
        case '+':
        case '-':
            return 1;
        case '*':
            return 2;
        case '-'+256:
            return 3;
        case '(':
            return -1;
        case ')':
            return -2;
        default:
            return 0;
    }
}


int main(void)
{
    int st[N];
    int top = 0, c = 0, last = '+';
    int out[N];
    int pointer = 0;
    int counter = 0;
    while (((c=getchar())!='=')&&(c!='\n')&&(c!=EOF))
    {
        if (c== ' '){
            continue;
        }
        if ((priority(last)&&(c=='-'))||(last=='"')&&(c=='-')){
            c = '-'+256;
            out[pointer] = '0';
            pointer++;
        }
        if (priority(c)>0){
            while ((priority(st[top-1])>priority(c))&&(!isempty(top))){
                out[pointer] = ' ';
                pointer++;
                out[pointer] = pop(st,&top);
                pointer++;
            }
            if ((priority(last)>0)&&(c!=('-'+256))){
                fprintf(stderr,"Знак после знака, ожидался операнд!\n");
                return -1;
            }
            push(st,&top,c);
            out[pointer] = ' ';
            pointer++;
        }
        if (c=='('){
            if (!priority(last)){
                fprintf(stderr,"Скобка после оператора!\n");
                return -1;
            }
            counter++;
            push(st,&top,c);
        }
        if (c==')'){
            if (counter==0){
                fprintf(stderr,"Закрывающаяся скобка без открытой скобки!\n");
                return -1;
            }
            else{
                    while (st[top-1]!='('){
                        out[pointer] = ' ';
                        pointer++;
                        out[pointer] = pop(st,&top);
                        pointer++;
                    }
                    counter--;
                    pop(st,&top);
                }
        }
        if (!priority(c)){
            out[pointer] = c;
            pointer++;
        }
        last = c;
    }

    if (counter!=0){
        fprintf(stderr,"Не все скобки закрыты!\n");
        return -1;
    }
    while (top>0){
        out[pointer] = ' ';
        pointer++;
        out[pointer] = pop(st,&top);
        pointer++;
    }
    out[pointer] = ' ';
    pointer++;
    for (int i=0;i<pointer;i++){
        printf("%c",out[i]);
    }
    putchar('\n');
    return 0;
}