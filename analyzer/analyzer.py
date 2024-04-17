
from flask import Flask
from consumer import launch_consumer, get_cache


analyzer_app = Flask(__name__)


@analyzer_app.route("/")
def analyze() -> dict[str, int]:
  return get_cache()


if __name__ == "__main__":
  launch_consumer()
  analyzer_app.run(host="0.0.0.0")
