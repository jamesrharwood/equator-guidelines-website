DIRECTORY = $(dir $(wildcard ./guideline_repos/))

test:
	python -m unittest discover
create:
	python -m build.create_resources $(guideline)
	
