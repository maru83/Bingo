from flask import Flask, render_template, request
import random

app = Flask(__name__)

num_list = random.sample(range(1, 76), k=75)
past_numbers = []
index = 0


@app.route('/', methods=['GET', 'POST'])
def bingo():
    global index
    
    if request.method == 'POST':
        if index < 75:
            selected_number = num_list[index]
            past_numbers.append(selected_number)
            index += 1
        else:
            selected_number = "終了"

        return render_template('bingo.html', selected_number=selected_number, past_numbers=past_numbers)
    else:
        return render_template('bingo.html', selected_number=None, past_numbers=past_numbers)

if __name__ == '__main__':
    app.run(debug=True)
