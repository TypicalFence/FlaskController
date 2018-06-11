# Flask Controller

This is a small library I wrote for having comfy controller classes in Flask.

The existing options have some weird quirks, which is why I wrote this.


# Usage

The Usage is pretty simple, just write a class that inherits from FlaskController and use the route decorator how you would use Flask.route. Then create an instance of your class and register it via the register method to a flask instance.

```python
from flask import Flask
from flask_controller import FlaskController, route

app = Flask(__name__)

class MyController(FlaskController):
    @route("/")
    def index(self):
        return "Hello World"

    @route("/hello/<name>")
    def hello(self, name):
        return "hello " + name

MyController().register(app)

app.run()
```
