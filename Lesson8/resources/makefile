SRCS = $(wildcard *.c)
PROGS = $(patsubst %.c,%,$(SRCS))

CC = gcc
CFLAGS = -lpthread


all: $(PROGS)
%: %.c
	$(CC) $< $(CFLAGS)  -o $@ 
clean: 
	rm -f $(PROGS)
