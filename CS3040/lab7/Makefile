OBJECTS = shell.o

FLAGS = -Wall
LDFLAGS = -o
FFLAGS = -g

all:
	gcc $(FLAGS) shell.c $(LDFLAGS) shell

c:
	rm -f $(OBJECTS) a.out shell

f:
	gcc $(FLAGS) $(FFLAGS) shell.c $(LDFLAGS) shell

w:
	vi shell.c

m: 
	valgrind --leak-check=full --show-leak-kinds=all -v ./shell

g:
	gdb ./shell
