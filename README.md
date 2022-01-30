# mPharma TH Python

This is the python version of this [repository](https://github.com/JuliRash/mpharma-th) built with laravel framework for PHP

## Installation

<p>To install and get this application running on your local machine follow the instructions below. </p>

Requirements 🪛:

- [Docker](https://docs.docker.com/)
- [docker-compose](https://docs.docker.com/compose/)

Clone the application

```bash
  git clone https://github.com/JuliRash/mpharma-th-python.git
```

Navigate to the directory

```bash
  cd mpharma-th-python
```

Create .env file from .env.example

```bash
  cp .env.example .env
```

Build Appliccation ⚙️:

```bash
  docker-compose up
```

Testing
make sure you have built the application

```bash
  docker-compose run django python manage.py test
```
