from flask_script import Manager
from my_resume import app, db, Professor, Courses

manager = Manager(app)


# reset the database and create two professors
@manager.command
def deploy():
    db.drop_all()
    db.create_all()
    harryWang = Professor(name='Harry Wang', department='Management Information System')
    vanleer = Professor(name='Vanleer,Michael G', department='Accounting')
    coffin = Professor(name='Coffin,Roger G', department='Accounting')

    course1=Courses(num='ACCT200', title='Survey of Accounting', description='Survey of financial and managerial accounting concepts for the non-business major. Students learn about financial statements for merchandising, manufacturing, and service companies.', professor_id=2)
    course2=Courses(num='ACCT207', title='Accounting I', description='An introduction to financial accounting. Topics: the accounting cycle, merchandise accounting, accounting procedures for cash, receivables, payables, inventories, plant and equipment, stocks and bonds.', professor_id=2)
    course3=Courses(num='MISY350', title='Business Application Development II ', description='Covers concepts related to client side development, including cascading style sheets and JavaScript.', professor_id=1)
    course4=Courses(num='ACCT350', title='Business Law I', description='Formation, use and performance of contracts, including both Common Law and the Uniform Commercial Code (Article 2, Sales). Other topics covered include product liability, negotiable instruments and accountants legal liability.', professor_id=3)

    db.session.add(harryWang)
    db.session.add(vanleer)
    db.session.add(coffin)
    db.session.add(course1)
    db.session.add(course2)
    db.session.add(course3)
    db.session.add(course4)
    db.session.commit()


if __name__ == "__main__":
    manager.run()
