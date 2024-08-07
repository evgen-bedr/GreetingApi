# Greeting API

To run the Docker image, use the following commands:

```sh
docker pull redrif48/greeting-api
docker run -e PORT=5000 -p 5000:5000 redrif48/greeting-api
```
# Using curl
GET request:
```sh
curl -X GET http://localhost:5000/api/greeting
```

POST request:
```sh
curl -X POST http://localhost:5000/api/greeting -H "Content-Type: application/json" -d '{"greeting": "Aloha !"}'
```

# Using Postman

GET request:
Set the URL to http://localhost:5000/api/greeting

POST request:
Set the URL to http://localhost:5000/api/greeting
1. Go to the Body tab.
2. Select raw and choose JSON from the dropdown.
3. Enter the following JSON in the text area:

```sh
{
  "greeting": "Aloha !"
}
```