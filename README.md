# Django App Deployment Guide
This guide will walk you through the process of launching a Django app in an environment where Python is not installed. The steps outlined here assume that you have the source code for your Django app and a `requirements.txt` file containing the necessary dependencies.

## Prerequisites
Before you begin, make sure you have the following prerequisites installed on your system:

- Python: [Install Python](https://www.python.org/downloads/)
- pip: [Install pip](https://pip.pypa.io/en/stable/installation/)
- virtualenv: Install using pip (`pip install virtualenv`)

## Step 1: Clone the Repository
Clone your Django app repository to your local machine:

git clone https://github.com/HQLoke/mh_assessment.git mindhive-app  
cd mindhive-app

## Step 2: Set up a Virtual Environment
### On Windows
python -m venv venv  
venv\Scripts\activate

### On macOS/Linux
python3 -m venv venv  
source venv/bin/activate

## Step 3: Install Dependencies
### Install the Python dependencies from the requirements.txt file:
pip install -r requirements.txt

## Step 4: Run the Django App
cd outlets  
python manage.py runserver

Your Django app should now be running and accessible at http://localhost:8000.

## API Endpoints
The Django app exposes the following API endpoints:

### Get all outlets:
Endpoint: http://localhost:8000/api/outlets  
Method: GET  
Description: Returns information about all outlets.  

### Get outlets by state:  
Endpoint: http://localhost:8000/api/outlets/<state>  
Method: GET  
Description: Returns information about outlets in a specific state. Replace <state> with one of the following: 'perlis', 'kedah', 'penang', 'kelantan', 'perak', 'terengganu', 'pahang', 'kuala-lumpur-selangor', 'negeri-sembilan', 'melaka', 'johor', 'sabah', 'sarawak'.

## List of improvements to be made:
1) Use PostgreSQL instead of SQlite database for more efficient geospatial data storing.
2) To speed up the web scraping task, could use threading if it takes too long to retrieve data
   from the network, else could use multiprocessing if processing the data takes too long.
   Currently doesn't have this bottleneck.
3) Use the scrapy framework for medium to large scale project. I'm not using this for the sake
   of simplicity, and I don't know how to use it >.<
4) Better address parsing. It's pretty difficult since the data are all jumbled up. Note: I
   switched to using google maps api instead and it's proven to be more accurate than open street maps.
5) More interactive design. I've also chosen to skip beautify my app due to the time constraint.
