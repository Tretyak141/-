#include "stack.h"

void push(int* st, int* num, int c)
{ st[(*num)++] = c; }

int pop(int* st, int* num)
{ return st[--(*num)]; }

int isempty(int num)
{ return !num; }
