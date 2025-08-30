DIRECTORY = $(dir $(wildcard ./guideline_repos/))

test:
	python -m unittest discover
create:
	python -m build.create_resources $(guideline)
preview:
	cp -a _guidelines_manual/. guidelines/
	quarto preview
publish:
	cp -a _guidelines_manual/. guidelines/
	quarto publish gh-pages --no-render
render: 
	quarto render
create-from-import:
	python -m build.resources.web.import_from_old_website
create_all:
	make create guideline=prisma
	make create guideline=strobe
	make create guideline=srqr
	make create guideline=arrive
	make create guideline=stard
	make create guideline=care
	make create guideline=squire
	make create guideline=consort

	# make create guideline=prisma-p
	# make create guideline=spirit
	# make create guideline=tripod




