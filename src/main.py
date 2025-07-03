from flask import Flask
from src.presentation.routes.version import version_bp

app = Flask(__name__)
app.register_blueprint(version_bp)

def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
