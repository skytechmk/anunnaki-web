from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def whitepaper():
    return render_template('whitepaper.html')

if __name__ == '__main__':
    # Run on all interfaces (required for Docker)
    app.run(host='0.0.0.0', port=5000, debug=False)
