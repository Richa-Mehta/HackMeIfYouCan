from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = sqlite3.connect("users.db")
        c = conn.cursor()

        # Secure version using parameterized queries
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        c.execute(query, (username, password))

        result = c.fetchone()
        conn.close()

        if result:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            return "<h3>Invalid login!</h3>"

    # GET request (show form)
    return render_template_string(open("login.html").read())

@app.route("/")
def home():
    return '<a href="/login">Go to Login Page</a>'

if __name__ == "__main__":
    app.run(debug=True)
