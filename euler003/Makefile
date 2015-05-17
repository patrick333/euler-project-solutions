# include ../common_m/makefile
CC=clang


OBJ=solution.o ../common_m/prime.o

CFLAGS=-fobjc-arc

solution: $(OBJ)
	$(CC) -o $@ $^ $(CFLAGS)

%.o: %.m
	$(CC) -c -o $@ $< $(CFLAGS)

.PHONY : clean
clean:
	rm solution *.o
