
import os
import pathlib
import dotenv
from django.core.wsgi import get_wsgi_application

CURRENT_DIR = pathlib.Path(__file__).resolve().parent
BASES_DIR = CURRENT_DIR.parent
ENV_FILE_PATH = BASES_DIR / ".env"

dotenv.read_dotenv(str(ENV_FILE_PATH))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ticketingSystem.settings')

application = get_wsgi_application()
