.SUFFIXES: .tex .pdf

.PHONY: all cleanall basic advanced clean


.tex.pdf:
	pdflatex $*.tex
	pdflatex $*.tex

SLIDES= session1.pdf #session2.pdf session3.pdf session4.pdf

pdf:    all

all: 	$(SLIDES)

cleanall:
	rm -f *.dvi *.log *.bak *.aux *.bbl *.blg *.idx *.ps *.eps *.pdf *.toc *.out *~ *.vrb *.nav *.snm

clean:
	rm -f *.log *.bak *.aux *.bbl *.blg *.idx *.toc *.out *~ *.vrb *.nav *.snm



