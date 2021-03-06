from flask import Flask, render_template, request

app = Flask("StyledDemoApp")

@app.route("/")
def say_hello():
    """Example showing how to return an HTML template with a form, which
    sends data back to this Flask app using a POST request."""

    return render_template("index.html", title="Home page")


@app.route("/feedback", methods=["POST"])
def gather_feedback():
    """Example showing how to retrieve data from POST requests.
    By default, when writing @app.route(...) on top of a function,
    it can only handle GET requests. As such, we need to explicitly
    specify that we want the function to handle POST requests with
    `method=["POST"]` bit."""

    # a neat way for accessing data for both GET and POST requests!
    data = request.values

    return render_template("feedback.html", form_data=data, title="Feedback response")

@app.route("/<name>")
def say_hello_to(name):
    """Example showing how to take URL parameter and capture its value, as
    well as how to return a string back to the user's browser."""

    return f"Hello {name}"

@app.route("/hello/<name>")
def show_hello_template(name):
    """Example showing to return and render an HTML template file back
    to the user's browser."""

    return render_template("hello.html", person=name, title="Greetings")

# "debug=True" causes Flask to automatically refresh upon any changes you
# make to this file.
app.run(debug=True)
