# Newsfeed portal
Personalized newsfeed portal. Fetch news from an API. Personalized feed for a user, which he 
can modify based on profile settings.
___
### List of features:
1. User create.
2. Token base authentication.
3. Password reset.
4. User profile.
5. Logout.
6. Personalized newsfeed.
7. Email notification.
8. News scheduler.
9. Full feature web UI.

## APIs List
1. ***Create user endpoint*** : http://127.0.0.1:8000/api/user/create/
```python
HTTP 201 Created
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "email": "rakib@gmail.com",
    "name": "Rakib"
}
```
2. ***Generate token endpoint*** : http://127.0.0.1:8000/api/user/token/
```python
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "token": "ac1d9998d2d15b674812729f7484d2f720344c6c"
}
```
3. ***Password reset endpoint*** : http://127.0.0.1:8000/api/user/password-reset/
```python
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "Success": "We have sent you a link to reset your password"
}
```
4. ***User profile endpoint*** : http://127.0.0.1:8000/api/user/user-profile/
```python
HTTP 200 OK
Allow: GET, PUT, PATCH, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "country_tag": "us",
    "source_tag": "CNN",
    "keyword_tag": "phone"
}
```
5. ***Logout endpoint*** : http://127.0.0.1:8000/api/user/password-reset/
```python
HTTP 204 No Content
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

"Success"
```
6. ***News api endpoint*** : http://127.0.0.1:8000/api/news/?page=1
```python
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
{
    "news": [
        'list of news'
    ]
}
```
7. For invalid token:
```python
HTTP 401 Unauthorized
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept
WWW-Authenticate: Token

{
    "detail": "Invalid token."
}
```
## Web endpoints:
1. User login: http://127.0.0.1:8000/login/
2. User registration: http://127.0.0.1:8000/login/
3. Password reset: http://127.0.0.1:8000/password-reset/
4. User profile: http://127.0.0.1:8000/profile/
5. News feed: http://127.0.0.1:8000/


## Setup Process
> ❗Make sure You have python3 and pip installed on your machine.

### Step 1

1. Create a folder where you want to clone the project.
   - I am creating a folder named ‘example’ in desktop

2. Now navigate to "example" via cmd or terminal

(Linux)

```bash
cd desktop/example
```

### Step 2

> It️ *Optional but better to use a virtual environment for every project.*

If don’t have any virtual environment manager installed in your machine.


1. Now clone the project and navigate to newsfeed-portal

```bash
git clone https://github.com/rakibulislam01/newsfeed-portal.git
cd newsfeed-portal
```

2. Install all the dependencies for the project.


```bash
pip install -r requirements.txt
```

### Step 3

1. Create a .env file in the project directory where setting.py file located, 
   open it with your favorite text editor and paste the bellow lines

>❗I share it for testing purposes. It will be deleted soon.
```.env
NEWS_API_KEY = ec6c9a7b6ea049099a62487b2c8987c4

SECRET_KEY = *@jqu&dhs+q%4n%g1dpuc61flcy7zcny)%d(x+pc21)_$dx

DEBUG = True

ALLOWED_HOSTS=.localhost, 127.0.0.1

EMAIL_HOST = smtp.sendgrid.net
EMAIL_HOST_USER = apikey
EMAIL_HOST_PASSWORD = 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

FORM_EMAIL = allinoner7@gmail.com
```

> If you want to set up sendgrid now then go to this [section](https://sendgrid.com/)

2. You are all setup, let’s migrate now.

```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create a superuser to rule the site 😎 [email user]

```bash
python manage.py createsuperuser

```

> *follow the instructions*

4. Hahh! Long wait. Let’s visit the site now

```bash
python manage.py runserver
```

Visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and rock 🤘
After all okay, Then you need to registration for new user. Then login and update
user setting for getting news.

---
## For live view: 
- url: https://news-portal-st.herokuapp.com/
- mail: rakib1@gmail.com
- password: test123456
---




