# Dev Onboarding

## fresh repo

First, make super user.

```bash
python3 manage.py createsuperuser
```

Then initialize the database

```bash
make migrate
```

Then run the application

```bash
make run
```

There are a few useful access points

```
localhost:8000
localhost:8000/admin/
localhost:8000/docs/
```

## test

```
make test
```

## deploy
