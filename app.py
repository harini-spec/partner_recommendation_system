# Import necessary modules
from flask import Flask, render_template, request, jsonify

# Local import
import final_model as simi

app = Flask(__name__)

@app.route('/')
def start_html():
    return render_template('index.html')

'''
    Possible urls:
        http://0.0.0.0:3012/result
'''
@app.route('/result', methods = ['POST'])
def home_html():

    learner         = request.form.get('learner')
    similar_learner,job = simi.find_similar_student(learner)

    result_dict = {
        'learner'  : learner,
        'learners' : similar_learner,
        'job' : job
    }

    # Testing
    # return jsonify(result_dict)

    return render_template('result.html', result = result_dict)

if __name__ == "__main__":
    app.run(
        debug = True,
        host  = '0.0.0.0',
        port  = 3012
    )