lint:
	find . -name '*.py' | xargs flake8 --ignore=E501,W601

test:
	(cd testing; python manage.py test)
