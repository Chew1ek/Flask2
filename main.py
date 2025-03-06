from flask import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    param = {}
    param['title'] = title
    return render_template('index.html', **param)


@app.route('/training/<prof>')
def plan(prof):
    param = {}
    param['prof'] = prof
    return render_template('content.html', **param)


@app.route('/list_prof/<how_to_list>')
def list_prof(how_to_list):
    prof_list = ['инженер', 'строитель', 'врач']
    param = {}
    param['prof_list'] = prof_list
    param['how_to_list'] = how_to_list
    return render_template('second.html', **param)


class LoginForm(FlaskForm):
    surname = StringField('Фамилия', validators=[DataRequired()])
    name = StringField('Имя', validators=[DataRequired()])
    education = StringField('Образование', validators=[DataRequired()])
    profession = StringField('Профессия', validators=[DataRequired()])
    sex = StringField('Пол', validators=[DataRequired()])
    motivation = StringField('Мотивация', validators=[DataRequired()])
    ready = BooleanField('Готовы остаться на Марсе?')
    submit = SubmitField('Записаться')


@app.route('/answer', methods=['GET', 'POST'])
@app.route('/auto_answer', methods=['GET', 'POST'])
def answer():
    form = LoginForm()
    if form.validate_on_submit():
        res = {
            "Фамилия": form.data["surname"],
            "Имя": form.data["name"],
            "Образование": form.data["education"],
            "Профессия": form.data["profession"],
            "Пол": form.data["sex"],
            "Мотивация": form.data["motivation"],
            "Готовы остаться на Марсе?": form.data["ready"],
        }
        # return "<br>".join([f"{i}: {j}" for i, j in res.items()])
        return render_template('otvet.html', data=res)
    return render_template('auto_answer.html', title='Авторизация', form=form)


@app.route('/success/<data>')
def otvet(data):
    return ""


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
