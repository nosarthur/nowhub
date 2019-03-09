from google.cloud import firestore

# from django.core.cache import cache


class FSClient:
    def __init__(self):
        self.db = firestore.Client()
        self.cache = {}

    def get(self, property):
        if property not in self.cache:
            config = self.db.collection('config').document(
                'django').get().to_dict()
            self.cache[property] = config[property]
        return self.cache[property]
