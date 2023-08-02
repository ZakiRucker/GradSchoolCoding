OBJECTS = mywget.o

FLAGS = -Wall
LDFLAGS = -o
FFLAGS = -g -DDEBUG

all:
	gcc $(FLAGS) mywget.c $(LDFLAGS) mywget

c:
	rm -f $(OBJECTS) a.out mywget index.html index.html.1 

f:
	gcc $(FLAGS) $(FFLAGS) mywget.c $(LDFLAGS) mywget

w:
	vi mywget.c

m: 
	valgrind --leak-check=full --show-leak-kinds=all -v ./mywget

g:
	gdb ./mywget

d:
	gcc ./wget tor.ern.nps.edu index.html
