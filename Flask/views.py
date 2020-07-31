from app import *
from flask import render_template
import forms
import os

@app.route('/', methods=['GET', 'POST'])
def index():
    
    form = forms.Submit()
    print(form.submit.data)
    if form.submit.data == True:
        print("SUBMITED")
        Imprimir(1)
    
    
  

    return render_template('index.html', form=form)

