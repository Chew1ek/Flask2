from flask import Flask, render_template, url_for

app = Flask(__name__)


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




if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
