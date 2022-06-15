# Awards-App

## Author
Kipkurui Evans

# Description
A web application to post websites and other web projects as well as review posted projects. You can visit the live site on https://awards-evslg.herokuapp.com/


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

* Install all the dependencies from the requirements.txt file by running `python3 pip install -r requirements.txt`

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

## Deployment

With all environment variables changed to suit your local copy of this repository, deploy the application to [Heroku] to see it live or simply run it locally
  (virtual) $ python3.8 manage.py runserver


## License

This project is licensed under the MIT License  [LICENSE.md](LICENSE.md) Copyright 2022  Kipkurui Evans.
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.