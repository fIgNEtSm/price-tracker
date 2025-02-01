from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.secret_key = "vishwaisgreat"

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        url = request.form['url']
        price = request.form['price']
        email = request.form['email']
        if not url or not price or not email:
            flash("All fields are required", "danger")
        else:
            flash("Tracking started successfully", "success")
            print(url, price, email)
    return render_template("main_page.html")

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')