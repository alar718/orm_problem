from flask import Flask, render_template, request, redirect, session, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cats.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Cat(db.Model):
    __tablename__ = "cats"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(140))



@app.route('/')
def main():
    cat_list = Cat.query.all()
    print(cat_list)
    return render_template('main.html', cats = cat_list)

@app.route('/addCat', methods=['POST'])
def add_cat():
    print(request.form)
    new_cat = Cat(
        name = request.form['name'],
        description = request.form['description']
    )
    db.session.add(new_cat)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)