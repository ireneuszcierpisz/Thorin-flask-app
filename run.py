import os
import json
# import the Flask class and more
from flask import Flask, render_template, request, flash

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


@app.route("/about")
def about():
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route("/about/<member_name>")
# The angle brackets will pass in data from the URL path, into our view below
# whenever we look at our 'about' URL with something after it, that will be passed into this view
def about_member(member_name):
    member = {}
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    # The first 'member' below is the variable name being passed through into our html file.
    # The second 'member' is the member object we created above on line 24.
    return render_template("member.html", member=member)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # access a form's data from the backend of the site (two ways of geting a value of an input)
        print(request.form.get("name"))
        # if the form doesn't actually have a key of 'name' then 'get("name"')' would print 'None' by default
        print(request.form["email"])
        # if there isn't an 'email' key on the form, instead of returning 'None', 'form["email"]' would throw an exception
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    return render_template("careers.html", page_title="Careers")


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
