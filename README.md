## Welcome

This application was developed for Zepto Hacker-Earth Test "Zepto Software Engineer Hiring Challenge".

## Project Structure

```
├── README.md
├── app.py
├── config.py
├── error.log
├── models.py
├── requirements.txt
├── static
│   ├── css
│   │   ├── bootstrap-3.0.0.min.css
│   │   ├── bootstrap-theme-3.0.0.css
│   │   ├── bootstrap-theme-3.0.0.min.css
│   │   ├── font-awesome-3.2.1.min.css
│   │   ├── layout.forms.css
│   │   ├── layout.main.css
│   │   ├── main.css
│   │   ├── main.quickfix.css
│   │   └── main.responsive.css
│   ├── font
│   │   ├── FontAwesome.otf
│   │   ├── fontawesome-webfont.eot
│   │   ├── fontawesome-webfont.svg
│   │   ├── fontawesome-webfont.ttf
│   │   └── fontawesome-webfont.woff
│   ├── ico
│   │   ├── apple-touch-icon-114-precomposed.png
│   │   ├── apple-touch-icon-144-precomposed.png
│   │   ├── apple-touch-icon-57-precomposed.png
│   │   ├── apple-touch-icon-72-precomposed.png
│   │   └── favicon.png
│   ├── img
│   └── js
│       ├── libs
│       │   ├── bootstrap-3.0.0.min.js
│       │   ├── jquery-1.10.2.min.js
│       │   ├── modernizr-2.6.2.min.js
│       │   └── respond-1.3.0.min.js
│       ├── plugins.js
│       └── script.js
└── templates
    ├── errors
    │   ├── 404.html
    │   └── 500.html
    ├── forms
    │   ├── forgot.html
    │   ├── login.html
    │   └── register.html
    ├── layouts
    │   ├── form.html
    │   └── main.html
    └── pages
```

### Quick Start

1. Clone the repo

```
$ git clone
$ cd agent-chanda
```

2. Initialize and activate a virtualenv:

```
# use python3.6 this application is made for python3.6
$ python3 -m venv env
$ source env/bin/activate
```

3. Install the dependencies:

```
$ pip install -r requirements.txt
```

5. Run the development server:

```
$ python app.py
```

6. Navigate to [http://localhost:5000](http://localhost:5000)

## Application is available on Github:

https://github.com/kartikeyangupta/irctc-app

## Application is Deployed to VM in Digital Ocean.

http://peerconnected.com:8000/get/booking/

## API Endpoints.

1. Add User (ADMIN ONLY)

```
URL Path : /add/user/
The API is for admin only, admin can add users and make him admin or not.
```

2.

```
URL PATH : /add/train/
Usercase : Add a train in Database
       Roles: AdminOnly
       Method: Post
       Params : name
```

3.

```
URL PATH : /add/train_coach/
Usercase : Add a Coach for a specific train in Database
       Roles: AdminOnly
       Method: Post
       Params : TrainName, CoachName
```

4.

```
URL PATH: /remove/train_coach/
 Usercase : Remove a Coach for a specfic train in Database
       Roles: AdminOnly
       Method: Delete
       Params : id<Integer>
```

5.

```
URL PATH : /add/booking/
 Usercase : Add a booking in Database
       Roles: all
       Method: Post
       Params : TrainName, CoachName, username
```

6.

```
URL PATH : /get/booking/
Usercase : Get all booking in Database
       Roles: all
       Method: Get
       Params : None
```
