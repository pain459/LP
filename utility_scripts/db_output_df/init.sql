-- -- Create a new table
-- CREATE TABLE your_table (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50),
--     age INTEGER,
--     email VARCHAR(50)
-- );

-- -- Insert some fake data
-- INSERT INTO your_table (name, age, email) VALUES ('John Doe', 30, 'john.doe@example.com');
-- INSERT INTO your_table (name, age, email) VALUES ('Jane Smith', 25, 'jane.smith@example.com');
-- INSERT INTO your_table (name, age, email) VALUES ('Alice Johnson', 28, 'alice.johnson@example.com');
-- INSERT INTO your_table (name, age, email) VALUES ('Bob Brown', 35, 'bob.brown@example.com');

-- Create users table
CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INTEGER,
    email VARCHAR(50)
);

-- Create orders table
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    user_id INTEGER,
    order_date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Insert fake data into users table
INSERT INTO users (name, age, email) VALUES 
('John Doe', 30, 'john.doe@example.com'),
('Jane Smith', 25, 'jane.smith@example.com'),
('Alice Johnson', 28, 'alice.johnson@example.com'),
('Bob Brown', 35, 'bob.brown@example.com'),
-- Add more users for complexity
('Charlie Black', 32, 'charlie.black@example.com'),
('David White', 29, 'david.white@example.com'),
('Eve Green', 26, 'eve.green@example.com'),
('Frank Blue', 31, 'frank.blue@example.com');

-- Insert fake data into orders table
INSERT INTO orders (user_id, order_date, amount) VALUES 
(1, '2024-01-10', 100.50),
(1, '2024-02-15', 200.75),
(2, '2024-03-20', 300.00),
(3, '2024-04-25', 150.25),
(4, '2024-05-30', 400.50),
-- Add more orders for complexity
(5, '2024-06-01', 250.75),
(6, '2024-06-05', 500.00),
(7, '2024-06-10', 350.25),
(8, '2024-06-15', 450.50),
(1, '2024-07-01', 150.50),
(2, '2024-07-02', 250.75),
(3, '2024-07-03', 350.00),
(4, '2024-07-04', 450.25);
