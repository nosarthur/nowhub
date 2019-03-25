.PHONY: test shell migrate run upload deploy

# local dev
run:
	python3 manage.py runserver
test:
	python3 manage.py test --parallel
shell:
	python3 manage.py shell
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
collectstatic:
	python3 manage.py collectstatic

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
