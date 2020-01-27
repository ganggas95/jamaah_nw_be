import os
from dotenv import load_dotenv, find_dotenv
from jamaah import app as app_instance

dotenv_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path)


if __name__ == "__main__":
    app_instance.run(
        os.getenv("HOST"),
        port=os.getenv("PORT"),
        debug=app_instance.config.get("DEBUG"),
    )
