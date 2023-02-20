# Django-portfolio

REST API service for a portfolio publication site. Written in Python using Django REST Framework.


## Set up


```
$ source .venv/bin/activate
```

```
$ pip install -r requirements.txt
```

```
$ docker-compose up -d db
```

```
python manage.py migrate
```

```
python manage.py runserver
```

### Getting access

- create user via /api/user/register/
- get access token via /api/user/token/

## Features

- JWT authenticated
- Admin panel /admin/
- Documentation is located at /api/doc/swagger/ or api/doc/redoc/
- Managing portfolio and images
- Creating portfolio with images
- Search images by name/description/portfolio name
- Leave the comments for the picture
- Implemented Error Handler with next statuses 400, 401, 403 and 404
