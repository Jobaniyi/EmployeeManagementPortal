from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Employee data (mock database)
employees = [
    {"id": 1, "name": "John Doe", "position": "Manager", "status": "Active"},
    {"id": 2, "name": "Jane Smith", "position": "Developer", "status": "On Leave"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Mock authentication (replace with real authentication later)
        if username == "admin" and password == "admin":
            return redirect(url_for("dashboard"))
        return "Invalid credentials"
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", employees=employees)

if __name__ == "__main__":
    app.run(debug=True)
