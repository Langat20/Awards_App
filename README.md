# Awards-App

## Author
Kipkurui Evans

# Description
A web application to post websites and other web projects as well as review posted projects. You can visit the live site on 


## User Story

* A user can view posted projects and their details.  
* A user can post a project to be rated/reviewed. 
* A user can rate/ review other users' projects.  
* Search for projects.  
* View projects overall score.
* A user can view their profile page.   

### Cloning
* In your terminal:
        
        $ git clone https://github.com/Langat20/Awards_App

## Running the Application
* Install virtual environment using `$ python3 -m venv --without-pip virtual`

* Activate virtual environment using `$ source virtual/bin/activate`

* Download pip in our environment using `$ curl https://bootstrap.pypa.io/get-pip.py | python`

* Install all the dependencies from the requirements.txt file by running `python3.6 pip install -r requirements.txt`

* Create a database and edit the database configurations in `settings.py` to your own credentials.
* Make migrations

        $ python manage.py makemigrations awwardsapp
        $ python3 manage.py migrate 

* To run the application, in your terminal:

        $ python3 manage.py runserver
        
## Testing the Application
* To run the tests :

        $ python3 manage.py test 


## Technology used

* Python3
* Django
* Heroku


## Known Bugs
* There is no known bugs but incase you find out please contact me.

## License
[MIT LICENSE](./license)