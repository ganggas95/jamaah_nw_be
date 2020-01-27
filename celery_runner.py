import os
from dotenv import load_dotenv, find_dotenv
from jamaah import celery_flask, app

if __name__ == '__main__':
    dotenv_path = os.path.join(os.getcwd(), '.env')
    load_dotenv(dotenv_path)
    with app.app_context():
        celery_flask.start()
