from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

print("start")

def add(f, t):
    open(f + ".txt", "a").write(t + ";")

def read(f):
    t = open(f + ".txt", "r").read().split(";")

    for i, x in enumerate(t):
        if x == "":
            t.pop(i)

    print(','.join("'{0}'".format(x) for x in t))
    return"[" + ','.join("'{0}'".format(x) for x in t) + "]"


def add_words(en, fr):
    add("en", en)
    add("fr", fr)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        add_words(request.form['en'].rstrip(), request.form['fr'].rstrip())
        return render_template('index.html', l_en = read("en"), l_fr = read("fr"))
    elif request.method == 'GET':
        return render_template('index.html', l_en = read("en"), l_fr = read("fr"))


if __name__ == "__main__":
    app.run(debug=False, host=0.0.0.0)
