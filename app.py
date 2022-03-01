from flask import Flask
import sys

app = Flask(__name__)


@app.route("/")
def healthCheck():
    return "Main page"


@app.route("/api/health")
def healthCheck():
    return ""


if __name__ == '__main__':
    print('Starting application', file=sys.stdout)
    app.run(debug=True)
