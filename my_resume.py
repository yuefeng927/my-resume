from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Courses')
def show_all_courses():
    courses = [
        'MISY350',
        'ACCT315',
        'HIST103'
    ]
    return render_template('courses-all.html', courses=courses)


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
