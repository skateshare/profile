from flask import Flask, render_template, request, redirect
app = Flask(__name__)


@app.route("/")
def welcomePage():
    return render_template("index.html")


@app.route("/test.html")
def testPage():
    return render_template("test.html")


@app.route("/<string:function_name>")
def function_call(function_name):
    return render_template(function_name)


def write_fo_file(data):
    with open("database.txt", "a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]

        database.write(f"\n{email}, {subject}, {message}")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_fo_file(data)
        return redirect("thankyou.html")
    else:
        return "something went wrong"