# Hello World FastAPI

## Running the project locally

### Create Python Virtual environment
- python -m venv <your_virtual_env_name>
- ./<your_virtual_env_name>/Scripts/Activate
- python -m pip install -r ./requirements.txt


### Database migrations
- alembic upgrade head
- alembic revision --autogenerate
- alembic upgrade head


### Running Server Inside Virtual environment
- ./<your_virtual_env_name>/Scripts/Activate
- uvicorn  main:app --reload

