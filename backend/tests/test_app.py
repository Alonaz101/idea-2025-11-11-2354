"""SCRUM-307: Unit and Integration Tests for API and Recommendation Engine."""

import unittest
from backend.app import app, db, User, Mood, Recipe, UserMoodEntry, RecipeRating

class TestAPI(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = app.test_client()
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_add_mood(self):
        with app.app_context():
            user = User(username='tester', email='tester@example.com')
            mood = Mood(mood_name='Happy')
            db.session.add(user)
            db.session.add(mood)
            db.session.commit()
            response = self.client.post('/api/mood', json={'user_id': user.id, 'mood_id': mood.id, 'timestamp': '2025-11-11T00:00:00'})
            self.assertEqual(response.status_code, 201)
            self.assertIn('Mood added', response.json['message'])

    def test_get_recipes(self):
        with app.app_context():
            recipe = Recipe(name='Pasta', description='Delicious')
            db.session.add(recipe)
            db.session.commit()
            response = self.client.get('/api/recipes')
            self.assertEqual(response.status_code, 200)
            self.assertTrue(any(r['name'] == 'Pasta' for r in response.json))

if __name__ == '__main__':
    unittest.main()
