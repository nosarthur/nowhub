BASEDIR=$(CURDIR)
DOCSDIR=$(BASEDIR)/docs

serve:
	$(MAKE) link
	mkdocs serve

deploy:
	$(MAKE) link
	mkdocs gh-deploy --clean

link:
	ln -sf $(BASEDIR)/README.md $(DOCSDIR)/index.md

install:
	pip install -r requirements.txt
