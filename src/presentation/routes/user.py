from flask import Blueprint, request, jsonify
from src.application.services.user_service import UserService
from src.presentation.dto.user_dto import CreateUserDTO

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    dto = CreateUserDTO.from_dict(data)
    result = UserService.create_user(dto)
    
    if isinstance(result, list):
        # Handle validation errors (list of Notifications)
        return jsonify({'errors': [str(notification) for notification in result]}), 400
    
    return CreateUserDTO.to_json(result)