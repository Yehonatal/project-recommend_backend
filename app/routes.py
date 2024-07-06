from flask import Blueprint, jsonify

# Create a Blueprint for routes
bp = Blueprint('routes', __name__)

# Define your routes using the Blueprint object


@bp.route('/about', methods=['GET'])
def about():
    return jsonify(description="Welcome to the Readmore backend API. Readmore is your personal book recommendation system. Simply input the books you've read or found intriguing, and receive tailored suggestions for new reads based on your interests. Discover your next favorite book with Readmore!")


@bp.route('/', methods=['GET'])
@bp.route('/help', methods=['GET'])
def home():
    return """
    <h1>Welcome to Readmore Backend API!</h1>
    <p>This API serves endpoints for book recommendations and more.</p>
    <p>Available endpoints:</p>
    <ul>
        <li><strong>/about</strong>: Get information about this backend API.</li>
        <li><strong>/api/hello</strong>: Example endpoint returning 'Hello, World!'</li>
    </ul>
    """


@bp.route('/api/hello', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")
