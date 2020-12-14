## m8buy Assignment | Aman Saraf

A simple API to create a metro Line for Sydney Metro. The endpoint is `/metro/line`.  
The endpoint is also accessible using this endpoint : `https://pjxm5irsa8.execute-api.ap-south-1.amazonaws.com/dev/metro/line` 
with request body as:

```
{
 "code": "NWL",
 "name": "North Western Line"
}
```

## Usage

Create a virtual env

```
mkvirtualenv m8buyAssignment
```

Install dependencies

```
pip install -r requirements.txt
```

Run the Flask app locally

```
FLASK_APP=transport.py flask run
```

To deploy to AWS:

```
zappa deploy dev
```

To update a deploy:

```
zappa update dev
```

To bring down all the code:

```
zappa undeplooy dev
```


