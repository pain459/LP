async def create_db_and_tables():
    host = os.getenv("DB_HOST", "localhost")
    user = os.getenv("DB_USER", "user")
    password = os.getenv("DB_PASSWORD", "user_password")
    db_name = os.getenv("DB_NAME", "airport_db")
    
    connection = await aiomysql.connect(
        host=host,
        user=user,
        password=password
    )
    async with connection.cursor() as cursor:
        await cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        await cursor.execute(f"USE {db_name}")
        await cursor.execute("""
        CREATE TABLE IF NOT EXISTS flights (
            id INT AUTO_INCREMENT PRIMARY KEY,
            flight_number VARCHAR(10) NOT NULL,
            from_location VARCHAR(50) NOT NULL,
            to_location VARCHAR(50) NOT NULL,
            status VARCHAR(20) NOT NULL,
            next_update VARCHAR(4) NOT NULL  -- Store time as HHMM format (4 characters)
        );
        """)
    await connection.commit()
    await connection.ensure_closed()
