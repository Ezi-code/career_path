# CAREER PATH HELP DESK

### INSTALLATION
This project is built with the flsk framework and all the packages required are in the requirements.txt file. Run the following command to install

```pip install -r requirements.txt```
Please make sure that you have python 3.x installed on your system before installing the packages as they require python to work.

### DESCRIPTION
This project is built targetting students of AAMUSTED espcially I.T students. It is built to containt various career paths in the filed of technology and providing mentorship to students that wish to get mentorship from their fellow students who already have an upper hand in such fields. This will also promote peer learning. The application have two sections. The first is the user section where the availabel careers are shown and students who wish to apply for mentorship can also apply to be metored by their collegues. The admin section on the other hand allows you to add,remove,or delete a career from the app. It also allows you to view the number of people that have applied for metorship. The database is build using sqlalchemy and the admin password is is hardcoded into the datbase since there is no register page for admins. to use this app, you have to set the username and password for the admins yourself. Don't worry about the database, it will be created on app execution. The following commands can be used to set the admin username and password. For windows users:

```set FLASK_APP=main```
For mac and linux users, replace the ```set``` with ```export```.

lunch python from your terminal and execute the following commands to set up the admin username and password. It works on all OS(mac, linux and windows)
```
>>> from main import models 
>>> from main.models import db
>>> admin = AdminUser(username="USERNAME", password="PASSWORD")
>>> db.session.add(admin)
>>> db.session.sommit()
>>> exit()
```

The name of the databse model is AdminUser.
You can replarce USERNAME and PASSWORD with your desired username and password. Afterwards, you can lunch the app by:

python main.py
The admin pannel can be acessed through a get request by typing ```localhost:5000/admin``` into the seach bar of your browser and everything else will be made available.

NOTE: ignore the >>> from the above commands. They are a representaion of the python prompt

### CONTRIBUTIONS
This project is opened to contributions and of you desire to contribute to this project, fork the project and afer adding ypur contributions, push the changes throug a new feature branch.

### CREDIT
EziCodes
