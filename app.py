from flask import Flask, render_template, request
import random

app = Flask(__name__)
past_results = []

@app.route('/', methods=['GET', 'POST'])
def bingo():
    if request.method == 'POST':
        
        bingo_numbers = list(range(1, 76))
        
        # 抽選した番号をリストから削除する
        for result in past_results:
            if result in bingo_numbers:
                bingo_numbers.remove(result)
        
        # 抽選結果を履歴に追加する
        selected_number = random.choice(bingo_numbers)
        past_results.append(selected_number)

        return render_template('bingo.html', selected_number=selected_number, past_results=past_results)
    else:
        return render_template('bingo.html', selected_number=None, past_results=past_results)

if __name__ == '__main__':
    app.run(debug=True)
