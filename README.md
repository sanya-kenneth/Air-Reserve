# Air-Reserve
Air Reserve is a platform where people can reserve seats on flights departing out of Entebbe International Airport

[![Build Status](https://travis-ci.com/sanya-kenneth/Air-Reserve.svg?branch=develop)](https://travis-ci.com/sanya-kenneth/Air-Reserve)  [![Coverage Status](https://coveralls.io/repos/github/sanya-kenneth/Air-Reserve/badge.svg?branch=develop)](https://coveralls.io/github/sanya-kenneth/Air-Reserve?branch=develop)

This API is hosted on `heroku`
Link ==>  `https://air-reserve.herokuapp.com/`

### Tech Stacks
- Python
- Django
- djangorestframework
- postgresql

## Installation

### Pre-requirements.
- Install [python](https://www.python.org/downloads/)
- install [Postgresql](https://www.postgresql.org/download/)

### Installation steps.
- Clone the [repository](https://github.com/sanya-kenneth/Air-Reserve)
- Create a `.env` file. See the `.env_example` in the root directory.
- Install a [virtual environment](https://virtualenv.pypa.io/en/latest/installation/).
- Activate the virtual environment and export the environment variables.
- Run `$ pip3 install -r requirements.txt` to install dependencies.
- Run `$ python3 manage.py makemigrations` to generate migrations.
- Run `$ python3 manage.py migrate` to add database tables.
- Run `$ python3 manage.py runserver` to start the local server.

### Testing

Use `python manage.py test` command to run the tests

## Endpoints

| Endpoint        | Permission | Functionality |
| --------        | -------------- |     --------- |
| `POST api/v1/auth/signup/`| `none` | Signup user |
| `POST api/v1/auth/admin/signup/`| `none` | signup admin |
| `POST api/v1/auth/login/` | `none` | user login |
| `GET api/v1/flights/all/`| `none` | Fetch a all flights |
| `GET api/v1/flights/<fight_id>` |`none` | Fetch single flight |
| `PATCH api/v1/flights/<flight_id>/update`| `admin required` | Update flight data |
| `POST api/v1/flights/`| `admin required` | Add flight |
| `POST api/v1/flights/<flight_id>/bookings/`| `normal required` | Book flight |
| `GET api/v1/bookings/`| `normal user` | Get flight bookings |
| `GET api/v1/bookings/<booking_id>`| `normal user` | Get single flight booking |
| `PATCH api/v1/bookings/<booking_id>/cancel`| `normal user` | Cancel flight booking |


## Django admin
- To use the inbuilt django admin please first signup an admin using the endpoint in the table above and then use this endpoint `api/v1/admin/` to access the admin site

## Request body formats

#### signup user or admin

```
{
	"first_name": "ketyo",
	"last_name": "sanuis",
	"email": "sanuis@outlook.com",
	"phone_number": "07032348719",
	"password": "LuYun123"
}
```

#### login user

```
{
	"email": "sanuis@outlook.com",
	"password": "LuYun123"
}
```

#### Add flight

```
{
	"departing_from": "Palisa",
	"destination": "Kampala",
	"date_of_departure": "2020-7-27",
	"departure_time": "6:00",
	"fee": 2000
}

```
#### Edit flight data

```
{
	"departing_from": "Palisa",
	"destination": "Kampala",
	"date_of_departure": "2020-7-27",
	"departure_time": "6:00",
	"fee": 2000
}

```
