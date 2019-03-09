.PHONY: test shell migrate run upload

run:
	python3 manage.py runserver
test:
	python3 manage.py test --parallel
shell:
	python3 manage.py shell
migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

upload:
	#gcloud compute scp db.sqlite3 instance-1:~nos/ckc00.us
