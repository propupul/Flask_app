from flask import Flask, render_template, session, redirect, url_for
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from da_location import location


app = Flask(__name__)
#app.config['SECRET_KEY'] = 'some hard to guess string lol'
app.config.from_pyfile('flaskapp.cfg')

manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(Form):
    name = StringField('What is the SKU ID?', validators=[Required()])
    submit = SubmitField('Submit')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    name = form.name.data
    
    
    try:
        da_locs = location(name)
    except:
        da_locs = ""
    #if form.validate_on_submit():
        
        #session['name'] = name
        #return redirect(url_for('index'))
    
    return render_template('index.html', form=form, name=da_locs)#name=session.get('name'))


if __name__ == '__main__':
    app.run(debug=True)
