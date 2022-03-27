[![Pylint](https://github.com/nicku12345/LIHKGMining_v1/actions/workflows/pylint.yml/badge.svg)](https://github.com/nicku12345/LIHKGMining_v1/actions/workflows/pylint.yml) 
[![Unit Tests](https://github.com/nicku12345/LIHKGMining_v1/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/nicku12345/LIHKGMining_v1/actions/workflows/unit-tests.yml)

# LIHKG Mining web application

Under development...

# Development mode:

```shell
source env/Scripts/activate
export FLASK_APP=mining
export FLASK_ENV=development
flask run --no-reload
```


# Running unit tests:

To me: make sure all tests have been imported to ```mining\tests\__init__.py```.

```shell
python -m unittest discover -v
```

with the ```coverage``` package:
```shell
coverage run --source=. -m unittest discover
coverage report -m
coverage html
```

# Docker

building image
```shell
docker image build -t {image_name} .
```

run the image in a container
```shell
docker run -d -p 5000:5000 --name {container_name} {image_name}
```

deploy on Heroku
```shell
heroku login
heroku container:login
heroku container:push web
heroku container:release web
```
