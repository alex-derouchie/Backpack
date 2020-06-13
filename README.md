# Backpack

Backpack is a free, simple inventory management system for small businesses and individuals. It allows users to create and share Inventories of Items on backpack-inv.com. This system provides features such as secure User registration and authentication, profile and item image support, and a number of other helpful features.

## Docker
bellow are example commands to build and run the application using a docker container. 
```bash
docker build --tag backpack:latest .
docker run --publish 8000:8000 -ti --rm --detach -v ~/Backpack:/backpack --name backpack-test backpack:latest
```

## Live Build

This project is now deployed! Visit backpack-inv.com to use today, or backpack-inv.herokuapp.com for HTTPS access.

## Usage

Feel free to tinker with the website, stress test it under load, and submit issue or feature requests to the repository. I'd be happy to improve this project!


This project was created in 2020 by Alex Derouchie using the Django Python framework.

