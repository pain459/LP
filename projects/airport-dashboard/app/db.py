import os
import aiomysql
from fastapi import Depends

async def connect_to_db():
    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER", "user")
    password = os.getenv("DB_PASSWORD", "user_password")
    db_name = os.getenv("DB_NAME", "airport_db")
    
    # Establish a connection
    connection = await aiomysql.connect(
        host=host,
        user=user,
        password=password,
        db=db_name
    )
    return connection
