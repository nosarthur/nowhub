.PHONY: test shell migrate run upload deploy

# Use the correct python call for specific OS
ifeq ($(OS),Windows_NT)
PY=py
else
PY=python3
endif

# local dev
run:
	$(PY) manage.py runserver
test:
	$(PY) manage.py test --parallel
shell:
	$(PY) manage.py shell
migrate:
	$(PY) manage.py makemigrations
	$(PY) manage.py migrate
collectstatic:
	$(PY) manage.py collectstatic

# remote
upload:
	#gcloud compute scp db.sqlite3 instance-1:~nos/ckc00.us
	gsutil cp ../docs/projects/*.md gs://nowhub/projects/
deploy:
	ln -fs production.yaml app.yaml
	gcloud app deploy app.yaml --project nowhub
stage:
	ln -fs staging.yaml app.yaml
	gcloud app deploy app.yaml --project stagehub
log:
	gcloud app logs tail
