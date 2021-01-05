# ImageRepository

This is an image repository where users can log in and upload images and make them private and public. 
Private uploads can only be seen by that particular user. Public uploads can be seen by all users.


## To run the project locally

1. Register on aws and create a new account.
2. Setup an aws s3 bucket.
3. create a aws user giving access permissions.
4. Clone the project and make a local copy
5. replace the ```AWS_SECRET_KEY``` and ```AWS_ACCESS_ID```.set emailid,password ```EMAIL_HOST_USER```, ```EMAIL_HOST_PASSWORD``` for verification email
6. installing required packages:
    ``` pip install django==2.2 django-storages django-crispy-forms boto3 ```
7. open cmd in the directory/folder and run:
    ``` python manage.py runserver```
    This runs the project on local host on port 8000.
    
## Website is live at (https://imgrepository.herokuapp.com/)
