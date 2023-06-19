# Train_System_OOP_Python
This project aims to develop a train system application using Python that adheres to the principles of object-oriented programming (OOP) and SOLID principles. The application will simulate a train system, allowing users to manage trains, stations, and routes.

#Features
The train system application will include the following features:

Train Management: Users can create, update, and delete train objects. Each train will have attributes such as train number, capacity, and current status (e.g., in transit, arrived).

Station Management: Users can manage stations by creating, updating, and deleting station objects. Stations will have attributes such as a unique station ID, name, and geographical location.

Route Planning: The application will allow users to plan routes by specifying the source and destination stations. It will calculate the optimal route based on various factors, such as distance, availability, and time constraints.

Passenger Management: Users can manage passenger information, including creating passenger profiles, assigning passengers to trains, and generating passenger manifests for each train.

Ticketing System: The application will implement a ticketing system to allow users to book, cancel, and modify tickets. It will handle seat availability, fare calculation, and ticket validation.

#Technologies Used
The project will be developed using the following technologies:

Python: The main programming language for implementing the train system application and applying OOP principles.

Object-Oriented Programming (OOP): The project will utilize OOP concepts such as classes, objects, inheritance, and encapsulation to design modular and maintainable code.

SOLID Principles: The SOLID principles (Single Responsibility, Open-Closed, Liskov Substitution, Interface Segregation, Dependency Inversion) will guide the design and architecture of the application, promoting flexibility, extensibility, and easy maintenance.

Project Structure
The project will be organized using the following structure:

css
#Copy code
train_system/
├── src/
│   ├── train.py
│   ├── station.py
│   ├── route.py
│   ├── passenger.py
│   ├── ticket.py
│   └── main.py
├── tests/
│   ├── test_train.py
│   ├── test_station.py
│   ├── test_route.py
│   ├── test_passenger.py
│   └── test_ticket.py
└── README.md
The src/ directory will contain the source code files for the train system application, including individual classes for train, station, route, passenger, ticket, and a main entry point file (main.py) to run the application.

The tests/ directory will contain unit tests for each class, ensuring proper functionality and adherence to OOP and SOLID principles.

Usage
To use the train system application, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/your-username/train-system.git
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python src/main.py
Follow the prompts and instructions provided by the application to manage trains, stations, routes, passengers, and tickets.

Contributing
Contributions to this project are welcome. If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request on the project repository.
