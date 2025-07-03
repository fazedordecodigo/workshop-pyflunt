from flask import Flask
from src.presentation.routes.version import version_bp
from src.presentation.routes.user import user_bp
from src.infrastructure.logger import get_logger

app = Flask(__name__)
app.register_blueprint(version_bp)
app.register_blueprint(user_bp)

logger = get_logger()

def main():
    logger.info("Iniciando aplicação Flask...")
    app.run(debug=True)


if __name__ == "__main__":
    main()
