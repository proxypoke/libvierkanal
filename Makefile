.PHONY: doc
doc:
	rst2html README.rst README.html	

.PHONY: clean
clean:
	rm -rf *.html
