# MovieHub2 

## MovieHub2 TMDB Movie Web app using Django

A Movie Webs App to provide information and news about All Movies, TV Series and People.

## MovieHub2 Content
- [TMDB Movie Web app using Django](#)
    - [Contents](#contents)
    - [Platform](#platform)
    - [Dependencies](#dependencies)
    - [Usage](#usage)
        - [Install Dependencies](#install-dependencies)
        - [Run](#run)
    - [Live Demo](#live-demo)

## Platform

```
    python: 3.8.1
    vs code: 1.25.1
    
```

## Dependencies

- **`Django`**: A high-level Python web framework.
- **`python-decouple`**: .
- **`gunicorn`**: A Python WSGI HTTP Server for UNIX, used to host the webiste on Heroku.

## Usage

Dependencies must be set up in an enviroment before using the project. Follow the following instructions for setting up the environment:

### Install Dependencies

- **For pip:**
  ```
    python3 -m virtualenv <environment name>
    source <environment name>/bin/activate
    pip install -r requirements.txt
  ```
- **For Anaconda:**
  ```
    conda env create -f environment.yml
    source activate django-tmdb
    pip install -r requirements.txt
  ```

### Run
    ```
        python manage.py runserver
        OR
        gunicorn pytmdb.wsgi:application --log-file -
    ```