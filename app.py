#!/usr/bin/env python
# coding: utf-8

# In[2]:


from flask import Flask,request,render_template
from textblob import TextBlob
import sqlite3
import datetime

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))
    
@app.route("/result",methods=["GET","POST"])
def result():
    t = request.form.get("t")
    result = TextBlob(t).sentiment
    return(render_template("result.html",result=result))

@app.route("/register",methods=["GET","POST"])
def register():
    name = request.form.get("name")
    currentDateTime = datetime.datetime.now()
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO user (name,timestamp) VALUES(?,?)',(name,currentDateTime))
    conn.commit()
    c.close()
    conn.close()
    return(render_template("register.html"))

@app.route("/query",methods=["GET","POST"])
def query():
    conn = sqlite3.connect('database.db')
    c = conn.execute('''select *
        from user''')
    r=""
    for row in c:
        print(row)
        r = r + str(row)
    c.close()
    conn.close()
    return(render_template("query.html",r=r))

@app.route("/next", methods=["GET","POST"])
def next():
    return(render_template("index.html"))
    
@app.route("/end", methods=["GET","POST"])
def end():
    return(render_template("end.html"))
    
if __name__ == "__main__":
    app.run()


# In[ ]:




