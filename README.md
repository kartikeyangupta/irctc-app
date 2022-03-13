## Welcome

Agent-Chanda is a Software as a Service(SaaS) which provides a user awnsers to MCQ questions.

## Project Structure

```sh
├── README.md
├── app.py
├── config.py
├── error.log
├── forms.py
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
        ├── placeholder.about.html
        └── placeholder.home.html
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

## API Endpoints.

1. Add User (ADMIN ONLY)

```
URL Path : /add/user?name=<name>&password=<>&isAdmin=<>

The API is for admin only, admin can add users and make him admin or not.
```
