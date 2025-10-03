# app.py
import os
import logging
from flask import Flask, jsonify
from config import DevConfig, ProdConfig

def create_app():
    env = os.getenv("APP_ENV", "dev").lower()  # dev (default) or prod
    cfg = DevConfig() if env == "dev" else ProdConfig()

    app = Flask(__name__)
    app.config.from_object(cfg)

    # ---- logging setup (console + file) ----
    logger = app.logger
    logger.setLevel(app.config["LOG_LEVEL"])
    logger.handlers.clear()  # avoid duplicate logs on reload

    fmt = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    )

    ch = logging.StreamHandler()
    ch.setLevel(app.config["LOG_LEVEL"])
    ch.setFormatter(fmt)
    logger.addHandler(ch)

    fh = logging.FileHandler(app.config["LOG_FILE"])
    fh.setLevel(app.config["LOG_LEVEL"])
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    # ----------------------------------------

    @app.route("/")
    def root():
        logger.info("Root endpoint hit")
        return jsonify(
            env=env,
            debug=app.config["DEBUG"],
            message=app.config["MESSAGE"]
        )

    @app.route("/log-demo")
    def log_demo():
        logger.debug("This is DEBUG")
        logger.info("This is INFO")
        logger.warning("This is WARNING")
        logger.error("This is ERROR")
        return jsonify(status="wrote debug/info/warning/error to console & file")

    return app

app = create_app()

if __name__ == "__main__":
    # run with python app.py (no FLASK_APP needed)
    app.run(host="127.0.0.1", port=5000, debug=app.config["DEBUG"])
