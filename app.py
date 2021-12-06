from flask import Flask, render_template

#create flask instance
app = Flask(__name__)

#route of website

@app.route('/home/')
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
