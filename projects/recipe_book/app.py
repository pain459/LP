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

    @app.route('/recipe/<int:recipe_id>')
    def recipe_detail(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        return render_template('recipe_detail.html', recipe=recipe)

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

    @app.route('/edit/<int:recipe_id>', methods=['GET', 'POST'])
    def edit_recipe(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        if request.method == 'POST':
            recipe.title = request.form['title']
            recipe.ingredients = request.form['ingredients']
            recipe.instructions = request.form['instructions']
            db.session.commit()
            return redirect(url_for('recipe_detail', recipe_id=recipe.id))
        return render_template('edit_recipe.html', recipe=recipe)

    @app.route('/delete/<int:recipe_id>', methods=['POST'])
    def delete_recipe(recipe_id):
        recipe = Recipe.query.get_or_404(recipe_id)
        db.session.delete(recipe)
        db.session.commit()
        return redirect(url_for('index'))

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5555)
