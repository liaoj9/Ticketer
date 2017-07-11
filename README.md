# Ticketer 
Ticketer is a ticket management system using [Python Flask](http://flask.pocoo.org "Takes all the work out of the backend") for the backend and [Foundation 6](http://foundation.zurb.com "Not bootstrap") for the frontend.

### Wanna see what it looks like?
Well, I just started this project so right now you'll need to do the following:
1) Clone the project
2) Install python, pip, virtualenv if you don't have them
3) Navigate to your local project folder and create a virtual environment
```
$ virtualenv venv
```
4) Activate the virtual environment
    * Linux
    ```
    $ venv/bin/activate
    ```
    * windows
    ```
    $ venv\Scripts\activate
    ```

Then install the requirements found in requirements.txt

```
$ pip install -r requirements.txt
```
5) Set the FLASK_APP variable in your command prompt or shell
    * Linux
    ```
    $ export FLASK_APP=app.py
    ```
    * windows
    ```
    $ set FLASK_APP=app.py
    ```
6) Run the app!
```
flask run
```
Then navigate to the url shown in the shell.
