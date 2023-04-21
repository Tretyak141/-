lib: stack.h stack.c
	gcc -c stack.c -o lib.o

inf: stack.c infix_to_postfix.c
	gcc stack.c infix_to_postfix.c -o inf

calc: stack.c calculator.c
	gcc calculator.c stack.c -o res

run: inf res
	 ./inf|./res