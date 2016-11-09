CREATE TYPE book_format AS ENUM ('hardcover' OR 'softcover')


CREATE TABLE Books(
	ISBN CHAR(14), 
	title TEXT,
	authors CHAR(100)[], 
	publishers CHAR(100),
	year_of_publication SMALLINT,
	stock INTEGER,
	price DECIMAL(6,2), 
	format book_format, 
	keywords CHAR(50)[], 
	subject CHAR(50),
	PRIMARY KEY (ISBN));

CREATE TABLE Customers (
	username CHAR(15), 
	password CHAR(10) NOT NULL, 
	first_name CHAR(15) NOT NULL, 
	last_name CHAR(15) NOT NULL,
	credit_card_number CHAR(20),
	address TEXT,
	phone CHAR(8),
	PRIMARY KEY (username));


CREATE TABLE reviews (
	score INTEGER NOT NULL,  
	description TEXT,
	date DATE, 
	book_ISBN CHAR(14), 
	customer_username CHAR(15),
	PRIMARY KEY (book_ISBN, customer_username),
	FOREIGN KEY(book_ISBN) REFERENCES Books, 
	FOREIGN KEY(customer_username) REFERENCES Customers,
	CHECK (score BETWEEN 0 AND 10) );

CREATE TABLE Store_Manager (
	username CHAR(15), 
	password CHAR(10),
	PRIMARY KEY (username));

CREATE TABLE book_orders (
	order_id SERIAL,  
	copies INTEGER NOT NULL,
	book_ISBN CHAR(14) NOT NULL,
	PRIMARY KEY(order_id),
	FOREIGN KEY(book_ISBN) REFERENCES Books, 
	FOREIGN KEY(order_id) REFERENCES Customer_orders); 

CREATE TABLE Customer_orders (
	order_id SERIAL,
	order_date DATE, 
	order_status CHAR(9),
	username CHAR(15),
	PRIMARY KEY (order_id),
	FOREIGN KEY (username) REFERENCES Customers);

CREATE TABLE feedback (
	customer_review CHAR(15), 
	customer_feedback CHAR(15),
	book_isbn CHAR(14), 
	rating INTEGER NOT NULL, 
	PRIMARY KEY(customer_feedback, customer_review,book_isbn), 
	FOREIGN KEY(customer_feedback) REFERENCES Customers, 
	FOREIGN KEY(book_isbn, customer_review) REFERENCES reviews,
	CHECK (customer_review <> customer_feedback),
	CHECK (rating BETWEEN 0 AND 2) );






