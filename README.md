## m8buy Assignment | Aman Saraf

A simple API to crate a metro Line for Sydney Metro. The endpoint is `/metro/line`. 

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


