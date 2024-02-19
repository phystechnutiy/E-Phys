from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quantities.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
app.app_context().push()

subs = db.Table('subs',
                db.Column('formulas_id'), db.ForeignKey('formulas.id'),
                db.Column('quantities_id'), db.ForeignKey('quantities.id')
                )

class quantities(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String, nullable=False)
    subsection = db.Column(db.String, nullable=False)
    designation = db.Column(db.String, nullable=False)
    value = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'quantities({self.id}, {self.name}'


class formulas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.String, nullable=False)
    subsection = db.Column(db.String, nullable=False)
    short_name = db.Column(db.String, nullable=False)
    formula = db.Column(db.String, nullable=False)
    values = db.relationship('quantities', secondary=subs, backref=db.backref('formulas'))

    def __repr__(self):
        return f'quantities({self.id}, {self.name}'



@app.shell_context_processors
def make_shell_context():
    return {'db': db, 'Quantity': quantities, 'formula': formulas, 'subs': subs, 'create_users': create_users}

def create_users():
    _formula = formulas(chapter='Механика')
    __f = formulas(chapher='Механика')
    _quantity = quantities(сhapter='Механика')
    __q = quantities(chapter='Механика')
    _formula._



@app.route('/')
def main():
    return render_template('main_page.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

