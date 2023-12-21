from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
from numpy import number
from pandas.core.interchange import dataframe

book = pickle.load(open('book.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))
book_pivot = pickle.load(open('book_pivot.pkl', 'rb'))
book2 = pickle.load(open('book2.pkl', 'rb'))
#similarity_scores = pickle.load(open('similarity_scores.pkl', 'rb'))
recommended = pickle.load(open('recommend.pkl', 'rb'))
java = pickle.load(open('java.pkl', 'rb'))
sql = pickle.load(open('sql.pkl', 'rb'))
html = pickle.load(open('html.pkl', 'rb'))
c = pickle.load(open('c.pkl', 'rb'))
r = pickle.load(open('r.pkl', 'rb'))
python = pickle.load(open('python.pkl', 'rb'))
ip = pickle.load(open('ip.pkl', 'rb'))
cpp = pickle.load(open('cpp.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(book['Book-Title'].values),
                           author=list(book['Book-Author'].values),
                           img=list(book['Image-URL-M'].values)
                           )


@app.route('/recommend')
def recommend_ui():
    return render_template('recommend.html')


@app.route('/recommend_books', methods=['post'])
def recommend():
    place = request.form.get('place')
    # place = place.lower()
    if (place == "java") or (place == "Java"):  # in list(recommended['genre'].unique()):
        return render_template('type.html',
                               book_name=list(java['title'].values),
                               author=list(java['author'].values),
                               )
    elif (place == "sql") or (place == "SQL"):
        return render_template('type.html',
                               book_name=list(sql['title'].values),
                               author=list(sql['author'].values),
                               )
    elif (place == "c") or (place == "C"):
        return render_template('type.html',
                               book_name=list(c['title'].values),
                               author=list(c['author'].values),
                               )
    elif (place == "r") or (place == "R"):
        return render_template('type.html',
                               book_name=list(r['title'].values),
                               author=list(r['author'].values),
                               )
    elif (place == "cpp") or (place == "C++"):
        return render_template('type.html',
                               book_name=list(cpp['title'].values),
                               author=list(cpp['author'].values),
                               )
    elif (place == "ip") or (place == "IP"):
        return render_template('type.html',
                               book_name=list(ip['title'].values),
                               author=list(ip['author'].values),
                               )
    elif (place == "html") or (place == "HTML"):
        return render_template('type.html',
                               book_name=list(html['title'].values),
                               author=list(html['author'].values),
                               )
    elif (place == "Python") or (place == "python"):
        return render_template('type.html',
                               book_name=list(python['title'].values),
                               author=list(python['author'].values),
                               )
    else:
        return "Invalid Entry"


if __name__ == '__main__':
    app.run(debug=True)
