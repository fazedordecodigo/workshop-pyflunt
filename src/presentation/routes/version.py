from flask import Blueprint, jsonify
from src import __version__

version_bp = Blueprint('version', __name__)

@version_bp.route('/version', methods=['GET'])
def get_version():
    return jsonify({"version": __version__})
