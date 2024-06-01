from flask import Flask, render_template, request, redirect, url_for
from models import db, Recipe

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        recipes = Recipe.query.all()
        return render_template('index.html', recipes=recipes)

    @app.route('/add', methods=['GET', 'POST'])
    def add_recipe():
        if request.method == 'POST':
            title = request.form['title']
            ingredients = request.form['ingredients']
            instructions = request.form['instructions']
            new_recipe = Recipe(title=title, ingredients=ingredients, instructions=instructions)
            db.session.add(new_recipe)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('add_recipe.html')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555)
