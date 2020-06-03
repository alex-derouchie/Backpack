# Backpack

Backpack is a free, simple inventory management system for small businesses and individuals.

## Docker
bellow are example commands to build and run the application using a docker container. 
```bash
docker build --tag backpack:latest .
docker run --publish 8000:8000 -ti --rm --detach -v ~/Backpack:/backpack --name backpack-test backpack:latest
```

## Installation

Clone the repository to your directory of choice. Within that directory, run in the command line:

```bash
py manage.py runserver
```

To  run the development server.

note that current versions of Python, Django, and Pillow are required. To install Django and Pillow:

```bash
pip install django
pip install pillow
```

## Usage

Once the development server is running, navigate to:

```bash
localhost:8000
```
to preview the project. From there, you can begin developing!
This project does not yet have a final release.

