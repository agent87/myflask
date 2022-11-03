from flask import Flask, request
from datetime import datetime

app = Flask('MY First Application')

@app.route('/')
def index():
    return """
    <h1>Arnaud Website</h1>
    <p>My name is Arnaud</p>
    """

@app.route('/nyandikira')
def contact_page():
    return "Contact me at arnauldkayonga1@gmail.com or 078xxxxxxxx"

@app.route('/date')
def date_page():
    date = str(datetime.now())
    return f'Today is {date}'

@app.route('/birthyear', methods=['POST', 'GET'])
def calc_birthyear():
    if request.method == 'POST': #USER IS POSTING or SUBMITING HIS/HER INFORMATION
        return f"""
        <form action="/birthyear" method="POST">
            <input type="number" name="birthyear" placeholder="Birthyear e.g 2020">
            <input type="submit" value="Submit">
        </form>
        From your submition your age is {2022 -  int(request.form.get('birthyear'))}
        """

    elif request.method == 'GET': #USER IS ASKING FOR THIS PAGE
        return """
        <form action="/birthyear" method="POST">
            <input type="number" name="birthyear" placeholder="Birthyear e.g 2020">
            <input type="submit" value="Submit">
        </form>
        """



if __name__ == '__main__':
    app.run()