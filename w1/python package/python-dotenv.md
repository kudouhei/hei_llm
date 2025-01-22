## python-dotenv

Python-dotenv reads key-value pairs from a .env file and can set them as environment variables. 

https://github.com/theskumar/python-dotenv/blob/main/src/dotenv/main.py

### Getting Started

`pip install python-dotenv`

To help you with that, you can add Python-dotenv to your application to make it load the configuration from a .env file when it is present (e.g. in development) while remaining configurable via the environment:

```
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

```

By default, load_dotenv doesn't override existing environment variables.

To configure the development environment, add a .env in the root directory of your project:
`.env`

The syntax of .env files supported by python-dotenv is similar to that of Bash:
```
# Development settings
DOMAIN=example.org
ADMIN_EMAIL=admin@${DOMAIN}
ROOT_URL=${DOMAIN}/app
```

If you use variables in values, ensure they are surrounded with { and }, like ${DOMAIN}, as bare variables such as $DOMAIN are not expanded. You will probably want to add .env to your .gitignore, especially if it contains secrets like a password.