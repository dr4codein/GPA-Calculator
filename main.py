from flask import Flask, render_template, request

app = Flask(__name__)

# Define the grading scale
grading_scale = {
    "O": 10,
    "A+": 9,
    "A": 8,
    "B+": 7,
    "B": 6,
    "C": 5,
    "RA": 0
}

# Define the courses and their credits
courses = {
    "Maths": 4,
    "Tamil": 1,
    "Analog": 3,
    "DLC": 3,
    "EMT": 3,
    "MI": 3,
    "ECA": 3,
    "Analog Lab": 2,
    "DLC Lab": 2
}

@app.route('/')
def index():
    return render_template('index.html', courses=courses, grading_scale=grading_scale)

@app.route('/calculate', methods=['POST'])
def calculate_gpa():
    total_grade_points = 0
    total_credits = 0
    for course, credits in courses.items():
        grade = request.form[course]
        total_grade_points += grading_scale[grade] * credits
        total_credits += credits
    gpa = total_grade_points / total_credits
    return f"Overall GPA: {round(gpa, 2)}"

if __name__ == '__main__':
    app.run(debug=True)
