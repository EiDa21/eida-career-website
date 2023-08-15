from flask import Flask
from flask import render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Abuja',
  'Salary': '$15,000',
}, {
  'id': 2,
  'title': 'Data Scientist',
  'location': 'Lagos',
  'Salary': '$17,000',
}, {
  'id': 3,
  'title': 'Software Engineer',
  'location': 'Abuja',
  'Salary': '$35,000',
}, {
  'id': 4,
  'title': 'Front-end Engineer',
  'location': 'Remote',
}]


@app.route("/")
def helloWorld():
  return render_template('home.html', jobs=JOBS, company_name='Jovia')


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
