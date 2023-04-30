import pandas as pd
from flask import Flask
from flask import render_template, request
from flask import redirect, url_for

app = Flask(__name__)

df = pd.DataFrame([], columns=['username', 'password', 'score'])

question_answer_list = [
    {'question': '2023年資工之夜的主題是什麼?', 'choice': ['subconsCiouS', 'SubContract', 'subConScious', 'subWaY'] ,'answer': 'subConScious'},
    {'question': '以下何者不是交大資工系友?', 'choice': ['蘇家永', '吳銘雄', '蔡士傑', '謝仁謙'] ,'answer': '謝仁謙'},
    {'question': '以下誰沒有在交大學餐打工?', 'choice': ['周彤瑾', '王俊閔', '陳柏安', '丁宇洋'] ,'answer': '陳柏安'},
    {'question': '誰不是五月的壽星?', 'choice': ['林芷瑩', '游建峰', '涂圓緣', '李宇婕'] ,'answer': '李宇婕'},
    {'question': '以下何者所代表的數字最大?', 'choice': ['張可晴的身高', '郭冠德的體重', '陳柏安的學分數', '陳宥安的年齡*6'] ,'answer': '張可晴的身高'},
    {'question': '下列何者距離最近?', 'choice': ['女二舍、工程三館', '工程三館、阿根早點', '交映樓、二餐', '綜合一館、西區烤肉場'] ,'answer': '女二舍、工程三館'},
    {'question': '國曆生日2月6日的張可晴屬什麼?', 'choice': ['龍', '蛇', '馬', '羊'] ,'answer': '蛇'},
    {'question': '天晟燒臘的老闆叫什麼?', 'choice': ['馮翠埤', '黃小泰', '蔡三高', '陳天晟'] ,'answer': '黃小泰'},
    {'question': '以下哪隻寵物沒有自己的寵物帳?', 'choice': ['肉包', '林小荳', '大胖熊', ' 醬波'] ,'answer': '林小荳'},
    {'question': '以下哪個人沒有畫畫帳?', 'choice': ['林宇柔', '陳秀琴', '梁詠晴', '陳虹蓓'] ,'answer': '林宇柔'},
    {'question': '以下誰不是南友會的成員?', 'choice': ['楊富祥', '郭晉維', '周彤瑾', '吳念蓉'] ,'answer': '周彤瑾'},
    {'question': '人體透過呼吸運動吸進體內的氣體，其最主要成分為何？', 'choice': ['氧氣', '二氧化碳', '氮氣', '水氣'] ,'answer': '氮氣'},
    {'question': '林一平教授曾經在報導中請記者小姐吃過什麼水果?', 'choice': ['麝香葡萄', '白草莓', '香水椰子', '西洋梨'] ,'answer': '白草莓'},
    {'question': '陳柏庭喜歡幫張可晴做什麼?', 'choice': ['挖鼻孔', '刷牙', '寫程式', '畫眉毛'] ,'answer': '挖鼻孔'},
    {'question': '涂圓緣去極麵道都吃什麼?', 'choice': ['養生魚肉鍋燒意麵', '炸醬麵', '豚骨拉麵', '韭菜水餃'] ,'answer': '韭菜水餃'},
    {'question': '以下誰不是新竹人?', 'choice': ['Alison', 'Bill Wu', 'drawccc', 'circle'] ,'answer': 'circle'},
    {'question': '福原愛如果得了老年癡呆會說什麼?', 'choice': ['哇沙咪', '養樂多', '撞球桌', '福原愛'] ,'answer': '福原愛'},
    {'question': '資工女舞跳過以下哪首歌?', 'choice': ['Not Shy', 'Perfume', 'I AM', 'Catch'] ,'answer': 'Not Shy'},
    {'question': '以下誰沒有女朋友?', 'choice': ['戚維凌', '丁宇洋', '杜峯', '楊卓敏'] ,'answer': '杜峯'},
    {'question': '以下何者不是指周彤瑾?', 'choice': ['交大 9m88', '交大 Jolin', '交大 Jisoo', '交大吳卓源'] ,'answer': '交大 Jisoo'},
    {'question': '以下誰不是臉頰肉軍團的成員?', 'choice': ['梁詠晴', '邵筱庭', '莊婕妤', '陳存佩'] ,'answer': '梁詠晴'},
    {'question': '謝翔丞沒有在清交二手大拍賣XD上發生過什麼事?', 'choice': ['尋找 iphone 的失主', '賣情趣用品', '跟室友的合照被管理員刪掉', '徵友'] ,'answer': '徵友'},
    {'question': '以下誰現在不是 Intel 實習生?', 'choice': ['陳伯庭', '黃則維', '高靖', '陳暐誠'] ,'answer': '高靖'},
    {'question': '田馥甄是以下哪個教授的綽號?', 'choice': ['彭文志', '李奇育', '黃俊龍', '陳添福'] ,'answer': '陳添福'},
    {'question': '下一屆系學會長是誰?', 'choice': ['戚維凌', '葉家蓁', '林宇柔', '張維成'] ,'answer': '戚維凌'}
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
    app.run('0.0.0.0', debug=True)
