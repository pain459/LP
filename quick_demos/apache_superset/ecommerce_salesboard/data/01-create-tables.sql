CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  name TEXT,
  signup_date DATE,
  region TEXT
);

CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name TEXT,
  category TEXT
);

CREATE TABLE orders (
  order_id INT PRIMARY KEY,
  customer_id INT,
  product_id INT,
  amount NUMERIC,
  order_date DATE
);

COPY customers FROM '/docker-entrypoint-initdb.d/customers.csv' DELIMITER ',' CSV HEADER;
COPY products FROM '/docker-entrypoint-initdb.d/products.csv' DELIMITER ',' CSV HEADER;
COPY orders FROM '/docker-entrypoint-initdb.d/orders.csv' DELIMITER ',' CSV HEADER;
