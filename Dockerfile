

FROM mcr.microsoft.com/playwright:v1.17.0-focal

WORKDIR /LIHKGmining_v1

COPY . /LIHKGmining_v1

# RUN apt-get install -y python3-pip
#RUN set -xe \
#    && apt-get update \
#    && apt-get install -y python3-pip

RUN pip install -r requirements.txt

RUN playwright install-deps

RUN playwright install

# For Heroku deployment, specify explicitly the port to be 0.0.0.0:$PORT
# It is because Heroku randomly assigns a port to each deployment
# 0.0.0.0 here is needed to indicate that it binds to any port
CMD gunicorn -b 0.0.0.0:$PORT 'mining:app'

# For local deployment, simply use a fixed port ($PORT=5000) is fine
# CMD gunicorn -b 0.0.0.0:5000 'mining:app'

# Deployment using waitress is not recommended.
# Waitress has a known issue where it will duplicate logging messages
# CMD waitress-serve --call --host="0.0.0.0" --port=5000 'mining:create_app' &> /dev/null