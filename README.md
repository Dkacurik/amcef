# AMCEF

## Requirements
Make sure you have the following packages installed:
* Docker
* Docker-compose

## Project setup
Project can be run with local environment or with docker 
### Local environment
Local environment is great, when you are using debugger tool. If you want to run local environment you have to do these steps:
1. Open setting.py file an uncomment this line of code
```
    env.read_env(env.str('ENV_PATH', '../../../dev.env'))
```
2. Setup new python interpreter
3. If you are using PyCharm Enable Django in your project
4. Set correct path for your manage.py and settings.py files in your Django project settings
5. Create Django server configuration for starting the server
```
    Host: localhost
    Port: 8000
    Environment variables: PYTHONUNBUFFERED=1;DJANGO_SETTINGS_MODULE=app.settings
```
6. Create Django server configuration for migrations
```
    Host: <empty>
    Port: <empty>
    Custom run command: migrate
```
7. Install requirements
```
    pip install -r requirements.txt
```
8. Start database in docker-compose.yml file 
9. Edit DATABASE_URL in dev.env file
```
    psql://postgres:postgres@localhost:5432/intro
```
10. Run Application
10. Run Migrate configuration

### Docker
If you want to run whole application via docker you have to do these steps:
1. Make sure, that this line in settings.py file is commented
```
    # env.read_env(env.str('ENV_PATH', '../../../dev.env')) 
```
2. Edit DATABASE_URL in dev.env file
```
psql://postgres:postgres@db:5432/intro
```
3. Run command:
```
    docker-compose up
```
3. For migrations run command:
```
    docker exec -it intro_web_1 python manage.py migrate
```

If you want to enter python docker container bash run this command
```
    docker exec -it intro_web_1 bash
```

# Documentation
Documentation is on url:
```
http://localhost:8000/api/docs/
```