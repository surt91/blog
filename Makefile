PY?=python3
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(CURDIR)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

DEBUG ?= 0
ifeq ($(DEBUG), 1)
	PELICANOPTS += -D
endif

RELATIVE ?= 0
ifeq ($(RELATIVE), 1)
	PELICANOPTS += --relative-urls
endif

help:
	@echo 'Makefile for a pelican Web site                                           '
	@echo '                                                                          '
	@echo 'Usage:                                                                    '
	@echo '   make html                           (re)generate the web site          '
	@echo '   make clean                          remove the generated files         '
	@echo '   make devserver [PORT=8000]          start/restart develop_server.sh    '
	@echo '   make stopserver                     stop local server                  '
	@echo '   make regenerate                     regenerate files upon modification '
	@echo '   make publish                        generate using production settings '
	@echo '                                                                          '
	@echo 'Set the DEBUG variable to 1 to enable debugging, e.g. make DEBUG=1 html   '
	@echo 'Set the RELATIVE variable to 1 to enable relative urls                    '
	@echo '                                                                          '

html:
	# the following line avoids an issue of the assest and i18n_subsites plugins
	mkdir -p output/theme/
	cp -r themes/purepelican/static/* output/theme/
	(cd output/theme/; python -c "import sass; sass.compile(dirname=('sass', 'css'), output_style='compressed')")
	# remove as soon as fixed

	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish:
	# the following line avoids an issue of the assest and i18n_subsites plugins
	mkdir -p output/theme/
	cp -r themes/purepelican/static/* output/theme/
	(cd output/theme/; python -c "import sass; sass.compile(dirname=('sass', 'css'), output_style='compressed')")
	# remove as soon as fixed

	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

	echo "blog.schawe.me" > output/CNAME

	# replace the quotation marks in the German files. I have no Idea how to do this properly via typogrify.
	( \
		cd output ; \
		find -name "*.html" -not -path "./en/*" -exec sed -i 's/“/„/g;s/”/“/g' {} + \
	)

clean:
	[ ! -d $(OUTPUTDIR) ] || rm -rf $(OUTPUTDIR)

regenerate:
	$(PELICAN) -r $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

devserver:
ifdef PORT
	$(BASEDIR)/develop_server.sh restart $(PORT)
else
	$(BASEDIR)/develop_server.sh restart
endif

stopserver:
	$(BASEDIR)/develop_server.sh stop
	@echo 'Stopped Pelican and SimpleHTTPServer processes running in background.'


.PHONY: html help clean regenerate publish ssh_upload rsync_upload dropbox_upload ftp_upload s3_upload cf_upload github
