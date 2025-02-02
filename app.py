from flask import Flask, render_template, request, flash
from database import init_db, add_tracking, tracking_exists, get_all
from message import send_msg
import os

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET")

init_db(app=app)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        url = request.form['url']
        price = request.form['price']
        email = request.form['email']
        if not url or not price or not email:
            flash("All fields are required", "danger")
        elif tracking_exists(url=url, email=email):
            flash("You are already tracking this product.", "success")
        else:
            add_tracking(url=url, price=price, email=email)
            message = f"You've Started Tracking for {url}.\n\nThankyou for using our service."
            send_msg(to_email=email, msg=message)
            flash("Tracking started successfully.", "success")
        print(get_all())
    return render_template("main_page.html")

if __name__ == "__main__":
    app.run(debug=True)