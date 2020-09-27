# About the application
This is a Django based URL shortener app which  shortens the URL and still redirects to the required page.

## Installing and executing the app

```
> git clone https://github.com/nidhisha-shetty/django-url-shortner-app
> cd django-url-shortner-app
> python manage.py runserver
```

## Description
This app has three endpoints:
1. `/api/post`: Add a unique long URL which returns a shorter URL with the help of a token. \
Sample endpoint: `POST` (http://127.0.0.1:8000/api/post)

2. `/api/delete`: Delete the long URL for which the shorter url has been generated. \
Sample endpoint: `DELETE` (http://127.0.0.1:8000/api/delete)

3. `/goto/{token}`: Redirects to the original long URL. \
Sample endpoint: `GET` (http://127.0.0.1:8000/goto/{token})

