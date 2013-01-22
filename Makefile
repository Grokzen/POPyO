help:
	@echo "Please use 'make <target>' where <target> is one of"
	@echo "  clean           remove temporary files created by build tools"
	@echo "  cleanpdf        revert uncommited PDF files"
	@echo "  cleanall        all the above + tmp files from development tools"
	@echo "  sdist           make a source distribution"
	@echo "  install         install package"

clean:
	-rm -f MANIFEST
	-rm -rf dist/*
	-rm -rf build/*

cleanmeta:
	-rm -rf lib/sweddoc/META-*

cleanall: clean cleanpdf cleandiag cleancoverage
	-find . -type f -name "*~" -exec rm -f "{}" \;
	-find . -type f -name "*.orig" -exec rm -f "{}" \;
	-find . -type f -name "*.rej" -exec rm -f "{}" \;
	-find . -type f -name "*.pyc" -exec rm -f "{}" \;
	-find . -type f -name "*.parse-index" -exec rm -f "{}" \;

sdist: cleanmeta
	python setup.py sdist

install: cleanmeta
	python setup.py install
