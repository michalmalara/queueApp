# Queue Application

## Description

This is a simple queue application that can br used in, for example, a bank. Users can sign in to queues, check their
status, and can be called to proper counters.

## Requirements

- Ptyhon 3.11
- viretualenv
- docker
- docker-compose

## Installation

1. Install all requirements
2. Clone the repository
3. Run `pip install -r requirements.txt` in the root directory
2. Run command `docker-compose up -d` in the root directory to run the application
3. Run command `docker-compose exec web python manage.py migrate` in the root directory to create database
4. Run command `docker-compose exec web python manage.py loaddata db.json` in the root directory to populate database
   with
   test data
3. The application can be reached on url 0.0.0.0:8080

## Usage

### Test users credentials

*Admin*
Administrator with access to admin panel

- username: admin
- password: afd#kO13S

*Employees*
Account for employees that can call users to counters

- username: employee1 - 9
- password: empl1234

*Kiosk*
Account for kiosk that can be used by customers to sign in to queues

- username: kiosk
- password: kioskpass1234

## Testing

run command `docker-compose exec web pytest` in the root directory