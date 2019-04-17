`$brew install python`

first off... you must have python installed(its better if you install the latest version because in python 3.7 many tkinter methods were deprecated). To know how to install brew <a href="https://brew.sh/">click here</a>.

`$python -m pip install pymongo`

if you are using pycharm IDE then make sure to add the pymongo package to you python interpreter. (I recommend using <a href="https://pypi.org/project/pip/">pip</a> to install pymongo).

after that...

database base part

`$brew install mongodb`
`$mkdir -p /data/db`
`$sudo chown -R `id -un` /data/db`

after installing mongoDB run the mongo demon (on port 27017... it run on this port by default)

`$mongod`

you dont need to create any database to this project as when the database is empty then this application will create the database and insert some sample sample along with user login.

you should be good to go.

![Screenshot](https://raw.githubusercontent.com/ZapySolo/sem4-mini-project-osl/master/asset/readmeIMG/Screenshot%202019-04-12%20at%207.24.48%20PM.png)

![Screenshot](https://raw.githubusercontent.com/ZapySolo/sem4-mini-project-osl/master/asset/readmeIMG/Screenshot%202019-04-12%20at%207.25.30%20PM.png)
