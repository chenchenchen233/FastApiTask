# URL shortening service
## Table of Contents
- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)


## Overview 
This project is a URL shortening server. The /encode endpoint takes a valid URL and returns a shortened version. The /decode endpoint takes the shortened URL and returns the original URL.
 
## Installation
install dependencies

```
pip install -r requirements.txt
```

## usage
run the server:

```
python server.py
```


test the functions
```
pytest -v test.py
```

## code-explanation

the main program performs the following steps:

1. **generate_code()**: It generates a random code which is used for the short url link

2. **encode** : Implement the /encode endpoint. When given a valid URL, it first checks if the URL has already been encoded. If it has, the existing shortened link is returned. If not, a new unique shortened link is generated and returned.
3. **decode** : Implement the /decode endpoint. When given a valid shortened URL, if it exists, the original URL is returned. If it does not exist, a message indicating that the shortened URL does not exist is returned.






