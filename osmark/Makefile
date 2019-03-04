.PHONY: test shell migrate run upload

test:
	python3 manage.py test --parallel
shell:
	python3 manage.py shell
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
run:
	python3 manage.py runserver
upload:
	#gcloud compute scp db.sqlite3 instance-1:~nos/ckc00.us
build:
	sudo docker build -t nosa/osmark:latest .
push:
	sudo docker push nosa/osmark:latest
