from flask import*
from routes import index,ourservices

app = Flask(__name__)


@app.route("/")
def a():
    return render_template("index.html")



app.add_url_rule("/index",view_func=index.index)

if __name__ == "__main__":
    app.run(debug=True)
