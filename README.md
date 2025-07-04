# Welcome to my Swift Reload project

## Project info


**Use your preferred IDE**

If you want to work locally using your own IDE, you can clone this repo.

Follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone https://github.com/yulduz1007/TaskSwiftReload.git

# Step 2: Install the necessary dependencies.
pip install -r requirements.txt

# Step 3: Migrate the changes and create database tables in terminal
make mig or python manage.py makemigration
            python manage.py migrate

"!!if python did not work use python3!!"
#step 4: Create admin from terminal
python manage.py createsuperuser
admin panel: http://127.0.0.1:8001/admin only works when you run the project

#step 5: Run the project and test it
python manage.py runserver
 
#step 6: Enter the link in terminal or simply type on chrome: http://127.0.0.1:8001/api

#step 7: login from login endpoint and put the token to authenticate, now you can test it, good look
```
