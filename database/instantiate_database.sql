CREATE DATABASE train_system;

USE train_system;

CREATE TABLE user(
	user_id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(30),
    fullname VARCHAR(50),
    phoneNumber VARCHAR(10),
    gender INT,
    address_id INT,
    PRIMARY KEY(user_id),
    FOREIGN KEY(address_id) REFERENCES address(address_id)
);

CREATE TABLE address(
	address_id INT NOT NULL AUTO_INCREMENT,
    communce VARCHAR(30),
    distict VARCHAR(30),
    city VARCHAR(30),
    country VARCHAR(30),
    PRIMARY KEY(address_id)
);

CREATE TABLE payment (
	payment_id INT NOT NULL AUTO_INCREMENT,
    payment_date DATE,
    user_id INT, 
    cost DOUBLE,
    PRIMARY KEY(payment_id),
    FOREIGN KEY(user_id) REFERENCES user(user_id)
);

CREATE TABLE chair (
	chair_id INT NOT NULL AUTO_INCREMENT,
    wagon_id INT, 
    user_id INT,
    state VARCHAR(10),
    PRIMARY KEY(chair_id),
    chair_type VARCHAR(10),
    FOREIGN KEY(wagon_id) REFERENCES wagon(wagon_id)
);

CREATE TABLE wagon(
	wagon_id INT NOT NULL AUTO_INCREMENT,
    train_id INT,
    width DOUBLE,
    height DOUBLE,
    wagon_type VARCHAR(20),
    length DOUBLE,
	PRIMARY KEY(wagon_id),
    FOREIGN KEY(train_id) REFERENCES train(train_id)
);

CREATE TABLE train(
	train_id INT NOT NULL AUTO_INCREMENT,
    train_name VARCHAR(10),
    PRIMARY KEY(train_id)
);

select * from train;	

CREATE TABLE staff (
	staff_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(50),
    fullname VARCHAR(50),
    telephoneNumber VARCHAR(10),
    email VARCHAR(50),
    gender INT,
    address_id INT,
    PRIMARY KEY(staff_id)
);



CREATE TABLE trainworker(
	train_worker_id INT NOT NULL AUTO_INCREMENT, 
	train_id INT,
    staff_id INT,
    PRIMARY KEY(train_worker_id),
    FOREIGN KEY(staff_id) REFERENCES staff(staff_id),
    FOREIGN KEY(train_id) REFERENCES train(train_id)
);

INSERT INTO address(communce, distict, city, country) VALUES ("Vinh Loc A", "Binh Chanh", "Ho Chi Minh", "VietNam"),("Ba Diem", "Hoc Mon", "Ho Chi Minh", "VietNam");
                            
SELECT * FROM address;

INSERT INTO user(email, fullname, phoneNumber, gender, address_id) 
VALUES ("phuckhoa81@gmail.com", "nguyen khoa minh phuc", "097295038", 0, 1), 
		("dieuuyen8812012@gmail.com", "nguyen khoa dieu uyen", "097295038", 1, 1), 
        ("mphuc8671@gmail.com", "nguyen khoa minh phuc", "097295038", 0, 1), 
        ("phucnkmps24819@fpt.edu.vn", "nguyen khoa minh phuc", "097295038", 0, 1);
        
        
INSERT INTO staff(email, fullname, telephoneNumber, gender, address_id, title) 
VALUES ("phuckhoa81@gmail.com", "nguyen khoa minh phuc", "097295038", 0, 1, "driver"), 
		("dieuuyen8812012@gmail.com", "nguyen khoa dieu uyen", "097295038", 1, 1, "waiter"), 
        ("mphuc8671@gmail.com", "nguyen khoa minh phuc", "097295038", 0, 1, "co-driver"), 
        ("phucnkmps24819@fpt.edu.vn", "nguyen khoa minh phuc", "097295038", 0, 1, "waiter");

INSERT INTO train(train_name) VALUES ("MF370"),
						("MT200"),
                        ("MKH33");
                        
INSERT INTO trainworker(train_id, staff_id) VALUES (1, 1),
                                                    (1, 3),
                                                    (1, 4),
                                                    (2, 2);
                                                    
INSERT INTO wagon(train_id, width, height, length, wagon_type) VALUES (1, 20.0, 5.0, 1000.0, "passenger"), 
													(1, 10.0, 10.0, 10.0, "firsthead"),
                                                    (1, 10.0, 10.0, 10.0, "tailhead"),
                                                    (1, 4, 3, 2, "restaurant"), 
                                                    (2, 5, 5, 5, "cargo"),
                                                    (2, 5, 5, 5, "cargo"),
                                                    (2, 5, 5, 5, "cargo"),
                                                    (2, 5, 5, 5, "cargo");
                                                    
INSERT INTO chair(wagon_id, user_id, state, chair_type) VALUES (1, 1, "active", "hard"),
												(4, 2, "active", "soft"),
                                                (2, 3, "active","room"),
                                                (1, 4, "active", "hard"),
                                                (1, 0, "waiting", "hard"),
                                                (3, 0, "waiting", "soft"),
                                                (3, 0, "unactive", "soft"),
                                                (3, 0, "unactive", "soft"),
                                                (2, 0, "unactive","room");	
                                                
SELECT * FROM wagon WHERE wagon_type = passenger;
