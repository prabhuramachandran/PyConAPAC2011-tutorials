.PHONY: all cleanall basic advanced clean

all: basic advanced 

basic: 
	cd basic; make

advanced:
	cd advanced; make

cleanall:
	cd basic; make cleanall
	cd advanced; make cleanall

clean:
	cd basic; make clean
	cd advanced; make clean



