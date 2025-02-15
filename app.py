from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/deepfake-checker", methods=["GET", "POST"])
def deepfake_checker():
    if request.method == "POST":
        # File upload handling will be implemented here
        pass
    return render_template("deepfake_checker.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)
