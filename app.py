import pandas as pd
from flask import Flask
from flask import render_template, request
from flask import redirect, url_for
from bank import qa_list

app = Flask(__name__)
df = pd.DataFrame([], columns=['username', 'password', 'score'])

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
    if int(number) > len(qa_list):
        return redirect('/result/'+username)
    else:
        info = {
            'username': username,
            'number': int(number),
            'qa_list': qa_list
        }
        return render_template('question.html', info=info)

@app.route('/answer/<username>/<number>', methods=['POST'])
def answer(username, number):
    global df
    if request.form['answer'] == qa_list[int(number)-1]['answer']:
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
    df = df.reset_index(drop=True)
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
    app.run('0.0.0.0', debug=False)
