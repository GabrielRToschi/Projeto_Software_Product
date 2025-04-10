from app import app
from flask import Flask, render_template
from app import app  # importa seu app configurado

if __name__ == "__main__":
    app.run(debug=True)

@app.route('/')
def home():
    return render_template('interface.html')
