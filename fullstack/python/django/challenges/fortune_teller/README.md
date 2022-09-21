### Start the Fortune Teller Project

To start the project, the code below is put into the terminal in order to create a Django project:
```
django-admin startproject fortuneteller
```

This will create the projects and all the folders within. After doing so, we have to enter the `fortuneteller` folder by changing directories with this code:
```
cd fortuneteller
```

Using this code afterwards will remove any errors from the server:
```
python3 manage.py migrate
```

So now we can start the development on server port `4001` (this is done through Codecademy):
```
python3 manage.py runserver 0.0.0.0:4001
```


### Create the Random Fortune App

To start building the new app `randomfortune`, we'll use the code below to do this:
