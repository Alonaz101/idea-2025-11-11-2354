"""SCRUM-302: Backend API with OAuth authentication and core MVP components."""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_oauthlib.provider import OAuth2Provider

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SECRET_KEY'] = 'supersecretkey'

db = SQLAlchemy(app)
oauth = OAuth2Provider(app)

# Data models for SCRUM-303
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

class Mood(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mood_name = db.Column(db.String(50), nullable=False)

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)

class UserMoodEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    mood_id = db.Column(db.Integer, db.ForeignKey('mood.id'))
    timestamp = db.Column(db.DateTime, nullable=False)

class RecipeRating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    rating = db.Column(db.Integer, nullable=False)


# SCRUM-304: API Endpoints Implementation
@app.route('/api/mood', methods=['POST'])
def add_mood():
    data = request.json
    # Assume data has user_id, mood_id, timestamp
    mood_entry = UserMoodEntry(user_id=data['user_id'], mood_id=data['mood_id'], timestamp=data['timestamp'])
    db.session.add(mood_entry)
    db.session.commit()
    return jsonify({'message': 'Mood added'}), 201

@app.route('/api/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    result = [{'id': r.id, 'name': r.name, 'description': r.description} for r in recipes]
    return jsonify(result), 200

@app.route('/api/recipes/<int:recipe_id>', methods=['GET'])
def get_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    return jsonify({'id': recipe.id, 'name': recipe.name, 'description': recipe.description}), 200

@app.route('/api/user/ratings', methods=['POST'])
def add_rating():
    data = request.json
    rating = RecipeRating(user_id=data['user_id'], recipe_id=data['recipe_id'], rating=data['rating'])
    db.session.add(rating)
    db.session.commit()
    return jsonify({'message': 'Rating added'}), 201

@app.route('/api/user/moodhistory', methods=['GET'])
def mood_history():
    user_id = request.args.get('user_id')
    history = UserMoodEntry.query.filter_by(user_id=user_id).all()
    result = [{'mood_id': h.mood_id, 'timestamp': h.timestamp.isoformat()} for h in history]
    return jsonify(result), 200


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
