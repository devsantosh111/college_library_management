import os
from dotenv import load_dotenv

load_dotenv()
env = os.environ.get("DJANGO_ENV")
if env == "production":
    from .prod import *
elif env == "development":
    from .dev import *
else:
    raise ValueError(f"Invalid DJANGO_ENV value: {env}")