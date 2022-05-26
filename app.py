from collections import namedtuple
from datetime import datetime

import flask_excel
from flask import Flask, render_template, request

from refactor import Hall, SeatAssigner

app = Flask(__name__)
app.config['DEBUG'] = True

flask_excel.init_excel(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    date = datetime
    data = {'a': [], 'b': []}
    hall = None
    errors = []
    selector = None
    if request.method == 'POST':

        rows = request.form['rows']
        a_course_1 = request.form['a_course_1']
        b_course_1 = request.form['b_course_1']
        a_courses_2 = request.form['a_courses_2']
        b_courses_2 = request.form['b_courses_2']
        a_course_3 = request.form['a_courses_3']
        b_course_3 = request.form['b_courses_3']
        _format = int(request.form['formation'])
        selector = {'a_course_1': [], 'b_course_1': [], 'a_courses_2': [], 'b_courses_2': [], 'a_courses_3': [],
                    'b_courses_3': []}

        all_a_s = []
        all_b_s = []
        a_students_1 = request.files['a_students_1']
        if a_students_1:
            try:
                dataset = request.get_array(field_name='a_students_1')
                prepare = namedtuple('students', [col.strip().replace(" ", "_").lower() for col in dataset[0]])
                dataset.pop(0)
                for item in dataset:
                    schema = prepare._make(item)
                    selector.get('a_course_1').append(schema)
                    all_a_s.append(schema)

            except Exception as e:
                errors.append(e.__str__())

        b_students_1 = request.files['b_students_1']
        if b_students_1:
            try:
                dataset = request.get_array(field_name='b_students_1')
                prepare = namedtuple('students', [col.strip().replace(" ", "_").lower() for col in dataset[0]])
                dataset.pop(0)
                for item in dataset:
                    schema = prepare._make(item)
                    all_b_s.append(schema)
                    selector.get('b_course_1').append(schema)
            except Exception as e:
                errors.append(e.__str__())

        a_students_2 = request.files['a_students_2']
        if a_students_2:
            try:
                dataset = request.get_array(field_name='a_students_2')
                prepare = namedtuple('students', [col.strip().replace(" ", "_").lower() for col in dataset[0]])
                dataset.pop(0)
                for item in dataset:
                    schema = prepare._make(item)
                    selector.get('a_courses_2').append(schema)
                    all_a_s.append(schema)
            except Exception as e:
                errors.append(e.__str__())

        b_students_2 = request.files['b_students_2']
        if b_students_2:
            try:
                dataset = request.get_array(field_name='b_students_2')
                prepare = namedtuple('students', [col.strip().replace(" ", "_").lower() for col in dataset[0]])
                dataset.pop(0)
                for item in dataset:
                    schema = prepare._make(item)
                    selector.get('b_courses_2').append(schema)
                    all_b_s.append(schema)
            except Exception as e:
                errors.append(e.__str__())

        a_students_3 = request.files['a_students_3']
        if a_students_3:
            try:
                dataset = request.get_array(field_name='a_students_3')
                prepare = namedtuple('students', [col.strip().replace(" ", "_").lower() for col in dataset[0]])
                dataset.pop(0)
                for item in dataset:
                    schema = prepare._make(item)
                    selector.get('a_courses_3').append(schema)
                    all_a_s.append(schema)
            except Exception as e:
                errors.append(e.__str__())

        b_students_3 = request.files['b_students_3']
        if b_students_3:
            try:
                dataset = request.get_array(field_name='b_students_3')
                prepare = namedtuple('students', [col.strip().replace(" ", "_").lower() for col in dataset[0]])
                dataset.pop(0)
                for item in dataset:
                    schema = prepare._make(item)
                    selector.get('b_courses_3').append(schema)
                    all_b_s.append(schema)
            except Exception as e:
                errors.append(e.__str__())

        hall = Hall(rows=int(rows), cols=2,
                    courses=list(filter(lambda x: x != "",
                                        [a_course_1, b_course_1, a_courses_2, b_courses_2, a_course_3, b_course_3])))
        seat_arranger = SeatAssigner(hall)
        seat_arranger.blueprint(_format)
        leftover = None
        # df = 0
        length_of_least = 0
        if len(all_a_s) > len(all_b_s):
            # df = len(all_a_s) - len(all_b_s)
            length_of_least = len(all_b_s)
            leftover = all_a_s[length_of_least:]
        if len(all_b_s) > len(all_a_s):
            length_of_least = len(all_a_s)
            # df = len(all_b_s) - len(all_a_s)
            leftover = all_b_s[length_of_least:]

        if not length_of_least:
            data.get('a').append(seat_arranger.placement("A", all_a_s))
            data.get('b').append(seat_arranger.placement("B", all_b_s))
        else:

            a = []
            b = []
            for i in range(0, len(leftover)):
                if i % 2 == 0:
                    a.append(leftover[i])
                else:
                    b.append(leftover[i])
            data.get('a').append(seat_arranger.placement("A", all_a_s[0:length_of_least] + a))
            data.get('b').append(seat_arranger.placement("B", all_b_s[0:length_of_least] + b))
            # data.get('a').append(seat_arranger.placement("A", ))
            # data.get('b').append(seat_arranger.placement("B", b))

    return render_template("index.html", data=data, halls=hall, errors=errors, date=date, selector=selector)


if __name__ == '__main__':
    app.run()
