from flask import Blueprint, jsonify, request
from authenticate.model.models import User, db





bp = Blueprint('bp', __name__)




@bp.route('/')
def main():
    return jsonify({"status" : "Failed"}), 400



@bp.route('/register', methods=['POST'])
def register_user():
    request_data = request.get_json()

    try:
        username = request_data["username"]
        password = request_data["password"]
    except KeyError:
        return jsonify({"Error" : "Username or Password is empty"}), 401


    user = User.query.filter_by(username=username).first()

    if not user:
        try:
            user = User(username=username, password=password)
            db.session.add(user)
            db.session.commit()
            return jsonify({"status" : "OK"}), 200

       
        except Exception:

            return jsonify({"status" : "Failed", "Error" : "Register failed"}), 500
    else:
        return jsonify({"status" : "User already exist"}), 401



@bp.route('/login', methods=['POST'])
def login_user():
    
    request_data = request.get_json()
    try:
        username = request_data["username"]
        password = request_data["password"]
    except KeyError:
        return jsonify({"Error" : "Username or Password is empty"}), 401
    
    user = User.query.filter_by(username=username).first()
    
    if user and user.check_password(password):
        return jsonify({"Status" : "Login was successful!"}), 200
    
    return jsonify({"Status": "Login failed!"}), 400



@bp.route('/delete', methods=['POST'])
def delete_user():

    request_data = request.get_json()
    try:
        username = request_data["username"]
        password = request_data["password"]
    except KeyError:
        return jsonify({"Error" : "Username or Password is empty"}), 401
    
    user = User.query.filter_by(username=username).first()

    if user:
        try:
            db.session.delete(user)
            db.session.commit()
            return jsonify({"Status" : "User deleted successfully!"}), 200
        except Exception:
            return jsonify({"Status" : "Failed to delete user."}), 500
    else:
        return jsonify({"Status" : "There is no user with this username"}), 404