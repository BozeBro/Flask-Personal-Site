from flask import Blueprint
from datetime import date

routes_blueprint = Blueprint('routes_blueprint', __name__)

github = 'https://github.com/BozeBro'
year = date.today().strftime("%Y")
@routes_blueprint.route('/')
@routes_blueprint.route('/index')
@routes_blueprint.route('/home')
def home():
    posts = Title.query.all()
    return render_template(
        'home.html', 
        posts=posts,
        heading='Benedict\'s Website',
        subheading='Bringing you content by Yours Truly',
        image='home-bg.jpg',
        title='Benedict Ozua',
        year=year,
        github=github
    )
