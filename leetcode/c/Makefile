CC=gcc
CFLAGS=-Wall

SOURCES := $(wildcard *.c)
TARGETS := $(patsubst %.c, %.exe, $(SOURCES))

.PHONY: all
all: $(TARGETS)

%.exe: %.c
	$(CC) $(CFLAGS) $< -o $@ -lm

run:
	$(CC) $(CFLAGS) $(p).c -o $(p).o -lm
	@ ./$(p).o

clean:
	rm -f *.o *.out $(TARGETS)
