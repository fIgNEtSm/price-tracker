from flask import Flask, render_template, request, flash
from database import init_db, add_tracking, tracking_exists, get_all

app = Flask(__name__)
app.secret_key = "vishwaisgreat"

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
            flash("Tracking started successfully.", "success")
        print(get_all())
    return render_template("main_page.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')