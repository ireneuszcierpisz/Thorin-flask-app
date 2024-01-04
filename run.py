import os

# import the Flask class
from flask import Flask, render_template

# creates an instance of Flask class and storing it in a variable called 'app'
# in Flask, the convention is that variable is called 'app'.
app = Flask(__name__)
# The first argument of the Flask class, is the name of the application's module - our package.
# Since we're just using a single module, we can use __name__ which is a built-in Python variable.

# the 'route' decorator tells Flask what URL should trigger the function that follows
# a decorator is a way of wrapping functions and all functions are objects and can be passed around.


@app.route("/")
def index():   # # create a function called "index"
    return render_template("index.html")

# When we try to browse to the root directory (as indicated by the "/"),
# then Flask triggers the index function underneath.
# Flask expects the index.html to be at directory called templates at the same level as run.py file


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        # using the os module from the standard library to get the 'IP' environment variable if it exists
        # but set a default value of "0.0.0.0" if it's not found
        port=int(os.environ.get("PORT", "5000")),
        # "5000" is a common port used by Flask
        debug=True)
    # we should never have "debug=True" in a production application
    # having debug=True can allow arbitrary code to be run, and this is a security flaw.
    # we should only have debug=True while testing an application in development mode,
