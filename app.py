import os
import pandas as pd
from flask import Flask
from flask import render_template, request
from flask import redirect, url_for
from datetime import timedelta

app = Flask(__name__)

df = pd.DataFrame([], columns=['username', 'password', 'score'])

question_answer_list = [
    {'question': '1+2=?', 'choice': ['2', '3', '4', '5'] ,'answer': '3'},
    {'question': '2+3=?', 'choice': ['4', '5', '6', '7'] ,'answer': '5'},
    {'question': '3+4=?', 'choice': ['6', '7', '8', '9'] ,'answer': '7'},
    {'question': '4+5=?', 'choice': ['8', '9', '10', '11'] ,'answer': '9'},
    {'question': '5+6=?', 'choice': ['10', '11', '12', '13'] ,'answer': '11'},
    {'question': '6+7=?', 'choice': ['12', '13', '14', '15'] ,'answer': '13'},
    {'question': '7+8=?', 'choice': ['14', '15', '16', '17'] ,'answer': '15'},
    {'question': '8+9=?', 'choice': ['16', '17', '18', '19'] ,'answer': '17'},
    {'question': '9+10=?', 'choice': ['18', '19', '20', '21'] ,'answer': '19'},
    {'question': '10+11=?', 'choice': ['20', '21', '22', '23'] ,'answer': '21'},
    {'question': '11+12=?', 'choice': ['22', '23', '24', '25'] ,'answer': '23'},
    {'question': '12+13=?', 'choice': ['24', '25', '26', '27'] ,'answer': '25'},
    {'question': '13+14=?', 'choice': ['26', '27', '28', '29'] ,'answer': '27'},
    {'question': '14+15=?', 'choice': ['28', '29', '30', '31'] ,'answer': '29'},
    {'question': '15+16=?', 'choice': ['30', '31', '32', '33'] ,'answer': '31'},
    {'question': '16+17=?', 'choice': ['32', '33', '34', '35'] ,'answer': '33'},
    {'question': '17+18=?', 'choice': ['34', '35', '36', '37'] ,'answer': '35'},
    {'question': '18+19=?', 'choice': ['36', '37', '38', '39'] ,'answer': '37'},
    {'question': '19+20=?', 'choice': ['38', '39', '40', '41'] ,'answer': '39'},
    {'question': '20+21=?', 'choice': ['40', '41', '42', '43'] ,'answer': '41'}
]
# home page
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        error_type = 'request_error'
        return render_template('error_login.html', error=error_type)
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == '':
            error_type = 'username_error'
            return render_template('error_login.html', error=error_type)
        if password == 'cs13union':
            info = {
                'username': username,
                'password': password
            }
            global df
            if username not in df.values:
                info_df = pd.DataFrame([[username, password, 0]], columns=['username', 'password', 'score'])      
                df = pd.concat([df, info_df], ignore_index=True)
            else:
                df.loc[df['username'] == username, 'score'] = 0
                
            df.to_csv('data.csv', index=False)
            return render_template('login.html', info=info)
        else:
            error_type = 'password_error'
            return render_template('error_login.html', error=error_type)

@app.route('/question/<username>/<number>', methods=['GET'])
def question(username, number):
    if int(number) > len(question_answer_list):
        return redirect('/result/'+username)
    else:
        info = {
            'username': username,
            'number': int(number),
            'qa_list': question_answer_list
        }
        return render_template('question.html', info=info)

@app.route('/answer/<username>/<number>', methods=['POST'])
def answer(username, number):
    global df
    if request.form['answer'] == question_answer_list[int(number)-1]['answer']:
        correct = True
        df.loc[df['username'] == username, 'score'] += 1
        df.to_csv('data.csv', index=False)
    else:
        correct = False    
    info = {
        'username': username,
        'number': int(number),
        'correct': correct
    }
    return render_template('answer.html', info=info)

@app.route('/result/<username>', methods=['GET'])
def result(username):
    global df
    score = df.loc[df['username'] == username, 'score'].values[0]
    df = df.sort_values(by=['score'], ascending=False)
    info = {
        'score': score,
        'data': df,
        'length': len(df) 
    }
    return render_template('result.html', info=info)

@app.route('/logout', methods=['GET'])
def logout():
    return redirect(url_for('home'))
    

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)