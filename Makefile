BASEDIR=$(CURDIR)
DOCDIR=$(BASEDIR)/docs

serve:
	$(MAKE) link
	mkdocs serve

deploy:
	$(MAKE) link
	mkdocs gh-deploy --clean

link:
	ln -sf $(BASEDIR)/README.md $(DOCDIR)/index.md
	ln -sf $(BASEDIR)/projects $(DOCDIR)/projects
