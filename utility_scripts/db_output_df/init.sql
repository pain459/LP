-- Create a new table
CREATE TABLE your_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    email VARCHAR(50)
);

-- Insert some fake data
INSERT INTO your_table (name, age, email) VALUES ('John Doe', 30, 'john.doe@example.com');
INSERT INTO your_table (name, age, email) VALUES ('Jane Smith', 25, 'jane.smith@example.com');
INSERT INTO your_table (name, age, email) VALUES ('Alice Johnson', 28, 'alice.johnson@example.com');
INSERT INTO your_table (name, age, email) VALUES ('Bob Brown', 35, 'bob.brown@example.com');
