DIRECTORY = $(dir $(wildcard ./guideline_repos/))

preview: 
	quarto preview
publish: render
	quarto publish gh-pages --no-render
render: create-from-import create-hosted-rgs
	PRODUCTION=1 quarto render
test:
	echo "Running unit tests"
	python -m unittest discover
create-from-import:
	echo "Creating database pages"
	python -m build.resources.web.import_from_old_website
create-hosted-rgs:
	echo "Creating resources for hosted RGs"
	make create guideline=prisma
	make create guideline=strobe
	make create guideline=srqr
	make create guideline=arrive
	make create guideline=stard
	make create guideline=care
	make create guideline=squire
	make create guideline=consort
create:
	python -m build.create_resources $(guideline)



