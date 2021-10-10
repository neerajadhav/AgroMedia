
# AgroMedia
A social media platform for agriculture sector 

## Features 
 - Mobile first **Modern design**
 - Users can **create**, **delete**, **edit**, **like** posts and make **comments** on them
 - **Newspaper** section, where all **agriculture** and **farmers** related news is served from various trusted sources
 -  A **Marketplace** to make it easy for farmers to **find stores** located in their area
- Friend system, **send**, **accept** friend requests
- **Weather updates** for searched location
## Tech Stack

### FrontEnd
 - HTML5
 - CSS
 - JavaScript
 - Bootstrap 5
 - Jquery 

###  Backend

 - Django Python Web Framework
 - PostgreSQL for Database
 - GitHub

## Getting started
###   Requirements
 - Python 3.6+
 - pip
 - virtualenv 

###  Installation
```bash
# Clone the repository
git clone https://github.com/neerajadhav/AgroMedia.git

# Enter into the directory
cd AgroMedia/

# Create virtual environment 
virtualenv env

# Activate virtual environment 
source env/bin/activate # for linux
source env/Source/activate # for windows

# Install the dependencies
pip install -r requirements.txt


# Check migrations.
python manage.py makemigrations

# Apply migrations.
python manage.py migrate

#Starting the application
python manage.py runserver
```
