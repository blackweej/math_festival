from flask import Flask, request, jsonify
from flask_cors import CORS 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random

app = Flask(__name__)
CORS(app) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///surveyvote.db'
CORS(app, resources={r"/api/*": {"origins": "https://dynamic-platypus-ba3ecf.netlify.app"}})

db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Survey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(1000))
    answer = db.Column(db.String(2000))

@app.route('/', methods=['POST'])
def submit_survey():
    try:
        data = request.get_json()

        name = data.get('name')
        sl = data.get('sl')
        re = data.get('re')
        hu = data.get('hu')
        gr = data.get('gr')

        print('gr:', gr, 'sl:', sl, 're:', re, 'hu:', hu)

        house_list = [('sl', sl), ('re', re), ('hu', hu), ('gr', gr)]
        max_house_values = [house[1] for house in house_list]
        max_house_value = max(max_house_values)

        selected_house = [house[0] for house in house_list if house[1] == max_house_value][0]

        if max_house_values.count(max_house_value) > 1:
            selected_house = 'az'
            if random.random() < 0.03:
                selected_house = 'cs'

        survey = Survey(
            question=name,
            answer=f"selected_house:{selected_house}",
        )

        db.session.add(survey)
        db.session.commit()

        response = {
            'message': '설문조사가 성공적으로 제출되었습니다.',
        }
        return jsonify(response), 200
    except Exception as e:
        print(str(e))
        response = {'message': '설문조사 제출에 실패했습니다.'}
        return jsonify(response), 500


@app.route('/get_survey_data', methods=['GET'])
def get_survey_data():
    try:
        survey_data = Survey.query.all()

        data_list = []

        for survey in survey_data:
            data_dict = {
                'id': survey.id,
                'question': survey.question,
                'answer': survey.answer
            }
            data_list.append(data_dict)

        return jsonify({'survey_data': data_list}), 200
    except Exception as e:
        print(str(e))
        response = {'message': '데이터 조회에 실패했습니다.'}
        return jsonify(response), 500

@app.route('/get_answer', methods=['GET'])
def get_answer():
    try:
        question_value = request.args.get('question')
        survey_data = Survey.query.filter_by(question=question_value).first()

        if survey_data:
            selected_house = survey_data.answer.split(":")[1]
            response = {
                'message': 'Data retrieved successfully.',
                'selected_house': selected_house
            }
        else:
            response = {
                'message': 'No data found for the provided question.'
            }

        return jsonify(response), 200
    except Exception as e:
        print(str(e))
        response = {
            'message': 'Failed to retrieve data.'
        }
        return jsonify(response), 500

@app.route('/get_terminal_input', methods=['GET'])
def get_terminal_input():
    global terminal_input
    terminal_input=input("input :")
    if terminal_input is not None:
        input_value = terminal_input
        terminal_input = None
    else:
        input_value = "터미널 입력값이 없습니다."

    return jsonify({'terminal_input': input_value}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)