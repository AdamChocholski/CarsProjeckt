# CarsProjeckt
## Overview
This project is a basic API built using Python and Flask. It provides a simple interface for interacting with a database of cars and brands.

## Installation
1. Clone the repository
    `git clone https://github.com/AdamChocholski/CarsProjeckt`

2. Install the required packages
    `pip install -r requirements.txt`
    
3.Run the application
        `python carlib.py`

## Usage
The API should have the following endpoints (only get was succesfully executed):

 -GET /cars Retrieves a list of all items in the database
 
 -GET /cars/ Retrieves a specific item by its id
 
 -POST /cars Creates a new item in the database The request body should be in the following format:
 
<code>
{
"id": "id",
"brand": "brand-name",
"name": "name"
}</code>

DELETE /cars/ Deletes an existing item by its id
