# Rojesty
 Django web application for project managements

For Windows:

Open your terminal
Start by cloning the project using this commande

```

git clone https://github.com/leriaetnasta/Rojesty.git
```

Go to your cloned project 
```

cd Rojesty
```

Download the latest version of python from this link 
```

https://www.python.org/downloads/
```

run the following commande to make sur python is installed
```

python (insert version e.g 3.10.2)
```


install the virtual environment wrapper for windows with this commande
```

py -m pip install --user virtualenv
```

create your virtual environment 
```

py -m venv (name e.g myproject)
```

activate your virtual environment
```

(name e.g myproject)\Scripts\activate
```

install Django

```
py -m pip install django
```


Now you need to install the dependencies:

install crispy modules:

```
pip install django-crispy-forms
```

install mysqlclient:

```
pip install pymysqlclient
```

install matplotlib

```
pip install matplotlib
```

install plotly

```
pip install plotly
```
install pandas

```
pip install pandas
```

now go to phpmyadmin 

```
http://localhost/phpmyadmin/
```
create your database


to synchronise your database run this commmande

```
Python manage.py makemigrations
```

then to create tables run 

```
Python manage.py migrate
```


to install pillow run 

```
pip install pillow
```

now to test your app

Go to management using the commande 

```
cd management
```

run the commande 

```
python manage.pc runserver
```

And you're all set :+1:



