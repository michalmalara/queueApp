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
3. The application can be reached on url http://localhost:8080/

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

### Swagger

Application has swagger documentation. To access it, go to url http://localhost:8080/api/swagger/
First, use endpoint /api/token/ with credentials mentioned above, to get access token. Then, click on Authorize button
and enter the token in the dialog box, like so:

`Bearer <access_token>`

After that, you can use all endpoints as a chosen user.

### Managing users and cases

Cases that customers might be interested and in and users can be managed in admin panel. To access admin panel, go to
url http://localhost:8080/admin/ and log in with admin credentials.

### Signing in to queues

To sign in to a queue, send POST request to url http://localhost:8080/api/queue/ with json body containing case id.
Example:

```json
{
  "case": 1
}
```

Customer can subscribe to his case via websockets. To do so, connect to url ws://localhost:8080/ws/queue/{queue_id}/
where queue_id is the id of the queue that customer wants to subscribe to. After connecting, customer will receive a
message with new statue every time someone is called to the counter.

### Calling customers to counters

To call customers to counters, you must be logged in as an employee. You can call a customer by send POST request to
url http://localhost:8080/api/queue/call-next/ with empty body.

## Testing

run command `docker-compose exec web pytest` in the root directory

## Frontend

The frontend is available on http://localhost:8080/

### Worker view

You can log in as a worker with credentials mentioned above using url http://localhost:8080/login
After that, you need to choose on which station you are working. You can do that by choosing it from a dropdown menu.
To call a customer, click on the button "Call next customer". It will display details of your customers case. If there
is no customer in the queue, you will get a popup message.

As a customer, you can use http://localhost:8080/kiosk view (log in as kiosk user). This view is meant to be used on a
touch screen placed in a waiting room in kiosk mode. Customer can choose a case they came and receive a number, under
which they will be called.

Next views in progress...