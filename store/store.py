
from flask import Flask, request
from producer import produce_data

store_app = Flask(__name__)


@store_app.route("/")
def land() -> str:
    usr_agent = request.headers.get('User-Agent')
    browser = usr_agent.split()[-1]
    produce_data(browser)
    
    return "<p>Welcome to the Store</p>"


if __name__ == "__main__":
    store_app.run(host="0.0.0.0")
