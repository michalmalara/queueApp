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
3. Run command `pip install -r requirements.txt` in the root directory
4. Run command `npm i` in frontend_scr/queueApp directory to install frontend dependencies
5. Run command `npm run build` in frontend_scr/queueApp directory to build frontend
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

### Managing users and cases

Cases that customers might be interested and in and users can be managed in admin panel. To access admin panel, go to
url http://0.0.0.0:8080/admin/ and log in with admin credentials.

### Signing in to queues

To sign in to a queue, send POST request to url http://localhost:8080/api/queue/ with json body containing case id.
Example:

```json
{
  "case": 1
}
```

Customer can subscribe to his case via websockets. To do so, connect to url ws://0.0.0.0:8080/ws/queue/{queue_id}/
where queue_id is the id of the queue that customer wants to subscribe to. After connecting, customer will receive a
message with new statue every time someone is called to the counter.

### Calling customers to counters

To call customers to counters, you must be logged in as an employee. You can call a customer by send POST request to
url http://localhost:8080/api/queue/call-next/ with empty body.

## Testing

run command `docker-compose exec web pytest` in the root directory