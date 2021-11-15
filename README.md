# Geolocation Service
Simple app to manage service areas for providers

### Development environment steps
1. Install docker and docker compose
2. Create an `.env` file, check .env.example to see what variables are necessary to run the app
3. Run the app using docker-compose: `docker-compose up -d`
4. Now you can verify if the service is running visiting this url: http://localhost:8080

### Run test with coverage
Run test using coverage and save results in local coverage db

    docker-compose exec app coverage run --source='.' manage.py test

Create & open html report

    docker-compose exec app coverage html && open htmlcov/index.html
 
It will open a new browser tap with the details about the code coverage

### Precommit
Using pre-commit library to keep organize and clean our code 
- `pip install pre-commit`
- Execute `pre-commit install`
- pre-commit library will execute autoflake, black and flake8 libraries to validate the code
- If you want to add a new library to pre-commit hooks, check .pre-commit-config.yaml file