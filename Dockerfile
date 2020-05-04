FROM python:3
ENV PYTHONNUMBUFFERED 1
RUN mkdir /backpack
WORKDIR /backpack
RUN pip3 install django
RUN pip3 install --user django-crispy-forms
RUN pip3 install --user pillow
EXPOSE 8000
CMD ["python3", "./manage.py", "runserver", "0.0.0.0:8000"]