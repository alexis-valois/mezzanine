
DEBUG = True

# Make these unique, and don't share it with anybody.
SECRET_KEY = "a954885b-039d-42d0-a676-a15e9c56c7279fbb6d79-0376-4ee3-bcfd-5088c3881b992c440ded-b720-47b0-a99d-da743489f919"
NEVERCACHE_KEY = "b79761dd-ccbb-4806-88b0-67dc0da339c98eedd595-e534-440e-b2a6-97c1b66e0efc890687fe-34df-49c3-a780-bfe3a31f5016"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}
