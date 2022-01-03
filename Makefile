reqs:
	pip install -r requirements.txt

db:
	flask db upgrade

run:
	flask run
