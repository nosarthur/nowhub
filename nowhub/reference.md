# References

## Notes

Production server log

```
gcloud app logs tail
```

Right now I use `make deploy`, which is very slow.
Maybe it's faster to push from local to repo,
then pull from repo to gcloud shell, then `make deploy` there.

## Deployment

- [Beginner’s Guide to Deploying a Django + PostgreSQL project on Google Cloud’s Flexible App Engine](https://codeburst.io/beginners-guide-to-deploying-a-django-postgresql-project-on-google-cloud-s-flexible-app-engine-e3357b601b91)
- [Install Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-using-the-repository)
- [Docker Compose for Django/PostgreSQL app](https://docs.docker.com/compose/django/)
- [Jake Wright's web development vlog](https://www.youtube.com/watch?v=YFl2mCHdv24&list=PLlj9BrHKq9WKaz8UV3BjEqicn-C3qHxy4&index=6)

## Google Cloud specifics

- [Getting Started With Django](https://cloud.google.com/python/django/)
- [Choosing an App Engine environment](https://cloud.google.com/appengine/docs/the-appengine-environments)
- [App Engine Pricing](https://cloud.google.com/appengine/pricing)
- [Google Compute Engine Pricing](https://cloud.google.com/compute/pricing)

## Misc

- [Setting up an apex domain](https://help.github.com/en/articles/setting-up-an-apex-domain)
