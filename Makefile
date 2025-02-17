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
create_all:
	make create guideline=prisma
	make create guideline=strobe-cohort
	make create guideline=strobe-case-control
	make create guideline=strobe-cross-sectional
	make create guideline=srqr


