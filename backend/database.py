import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

import os
from sqlalchemy import create_engine

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("CRITICAL: The DATABASE_URL environment variable is missing!")

# If your database string starts with 'postgres://', SQLAlchemy 1.4+ requires 'postgresql://'
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)



