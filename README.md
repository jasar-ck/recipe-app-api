# recipe-app-api
Source code for Recipe API app

# Steps
1. Create a git repository - Lisence , .gitIgnore(python)
2. Clone project
3. Create Docker File
4. docker build .
5. docker-compose build
6. create a django project
          docker-compose run app sh -c "django-admin.py startproject app ."
7. requirements.txt to enter the packages
7. https://travis-ci.org/ - Logged in using github account and sybnch
8. created .travis.yml File - Continuos Integration
9. created flake8 File



# Creating Django custom user model

1. docker-compose run app sh -c "python manage.py startapp core" -> it will create a core app .
2. removed view and test
3. create a folder and file test/__init__.py
4. Add 'core' in settings.py 'INSTALLED_APPS' list
5. Create a new test file in test folder
6. Created a Model [User and UserManager] - Added email as USERNAME_FIELD
7. Migrated - docker-compose run app sh -c "python manage.py makemigrations core"
8. Run test 



# New Technologies

1. docker
2. docker-compose
3. django , djangorestframework
4. travis-ci
5. flake8
