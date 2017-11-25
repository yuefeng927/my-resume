import os
from flask import Flask, session, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess secure key'

# setup SQLAlchemy
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
db = SQLAlchemy(app)


# define database tables
class Professor(db.Model):
    __tablename__ = 'professors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    department = db.Column(db.Text)
    courses = db.relationship('Courses', backref='professor')


class Courses(db.Model):
    __tablename__ = 'courses'
    num = db.Column(db.String(256), primary_key=True)
    title = db.Column(db.String(256))
    description = db.Column(db.Text)
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.id'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/Professors')
def show_all_professors():
    professors = Professor.query.all()
    return render_template('professor-all.html', professors = professors)


@app.route('/professor/add', methods=['GET', 'POST'])
def add_professors():
    if request.method == 'GET':
        return render_template('professor-add.html')
    if request.method == 'POST':
        # get data from the form
        name = request.form['name']
        department = request.form['department']

        # insert the data into the database
        professor = Professor(name=name, department=department)
        db.session.add(professor)
        db.session.commit()
        return redirect(url_for('show_all_professors'))


@app.route('/professor/edit/<int:id>', methods=['GET', 'POST'])
def edit_professor(id):
    professor = Professor.query.filter_by(id=id).first()
    if request.method == 'GET':
        return render_template('professor-edit.html', professor=professor)
    if request.method == 'POST':
        # update data based on the form data
        professor.name = request.form['name']
        professor.department = request.form['department']
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_professors'))




# courses-all.html adds course num to the edit button using a hidden input
@app.route('/Courses')
def show_all_courses():
    courses = Courses.query.all()
    return render_template('courses-all.html', courses=courses)


@app.route('/courses/add', methods=['GET', 'POST'])
def add_courses():
    if request.method == 'GET':
        professors = Professor.query.all()
        return render_template('courses-add.html', professors=professors)
    if request.method == 'POST':
        # get data from the form
        num = request.form['num']
        title = request.form['title']
        description = request.form['description']
        professsor_name = request.form['professor']
        professor = Professor.query.filter_by(name=Professor.name).first()
        courses = Courses(num=num, title=title, description=description, professor=professor)

        # insert the data into the database
        db.session.add(courses)
        db.session.commit()
        return redirect(url_for('show_all_courses'))


@app.route('/courses/edit/<string:num>', methods=['GET', 'POST'])
def edit_courses(num):
    courses = Courses.query.filter_by(num=num).first()
    professors = Professor.query.all()
    if request.method == 'GET':
        return render_template('courses-edit.html', courses=courses, professors=professors)
    if request.method == 'POST':
        # update data based on the form data
        courses.num = request.form['num']
        courses.title = request.form['title']
        courses.description = request.form['description']
        professor_name = request.form['professor']
        professor = Professor.query.filter_by(name=professor_name).first()
        courses.professor = professor
        # update the database
        db.session.commit()
        return redirect(url_for('show_all_professors'))



@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    # activates the debugger and the reloader during development
    # app.run(debug=True)
    app.run()

    # make the server publicly available on port 80
    # note that Ports below 1024 can be opened only by root
    # you need to use sudo for the following conmmand
    # app.run(host='0.0.0.0', port=80)
