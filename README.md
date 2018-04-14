### Todo-List API

#### Description
It is an API that enables CRUD methods for creating a todo list and items within each todo list.
### Development

Clone the repository: 

```git clone https://github.com/wanjiku-carol/opensaturdays_blog.git```

Navigate to the cloned repo. 

Ensure you have the following:

```
1. postgres
2. python3 & a virtualenv
3. Flask
4. Postman
```

Create a virtualenv and activate it. [Refer here](https://docs.python.org/3/tutorial/venv.html)

### Dependencies
- Install the project dependencies:
> $ pip install -r requirements.txt

### Set up Database
- Create a database:
> $ createdb todos

- Run migrations:
> $ python manage.py db upgrade

After setting up the above. Run:

```python run.py```

Test the endpoints registered on `run.py` on Postman/curl on the port the app is running on. 

#### Contribution
Fork the repo, create a PR to this repository's develop.
