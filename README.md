ISO service
===========
is microservice, that is able to take a country ISO code and a list of country names (in different languages) as an input. It will filter out just the countries that correspond to the provided ISO code and return them to the output.

## How to run
1. Clone the repository
2. Run 'docer-compose build' in the root directory
2. Run `docker-compose up` in the root directory
3. Open `http://localhost:8000/` in your browser
4. Use the service
5. Run `docker-compose down` in the root directory to stop the service

Request:

```
POST /match_country

{
	"iso": "svk",
	"countries": [
		"iran",
		"Slowakei",
		"Vatikan",
		"Slovaška",
		"Szlovákia",
		"Belgrade",
		"España",
		"Nizozemsko"
	]
}
```

Response:
```
{
	"iso": "svk",
	"match_count": 3,
	"matches": [
		"Slowakei",
		"Slovaška",
		"Szlovákia"
	]
}
```
ISO code have to be 3 characters long and can contain only letters. Country names can contain only letters and spaces. 

in case of invalid input, the service will return 400 Bad Request with a message describing the problem.

## Documentation
Documentation is available at `http://localhost:8080/docs` when the service is running.
table of used technologies:

| Technology     | Description |
|----------------| --- |
| Python 3.10    | Python is an interpreted, high-level and general-purpose programming language. |
| FastAPI        | FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints. |
| Docker         | Docker is a set of platform as a service products that use OS-level virtualization to deliver software in packages called containers. |
| Docker-compose | Compose is a tool for defining and running multi-container Docker applications. |
| Pytest         | The pytest framework makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries. |
| poetry         | Poetry is a tool for dependency management and packaging in Python. |

## Authors

* **Tomáš Neuschl**
