from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
@app.context_processor
def inject_app_name():
    return dict(app_name="Arogya AI")

@app.route('/chatbot')
def chatbot():
    return redirect("https://huggingface.co/spaces/Supriyas-04/medico_ai", code=302)

@app.route('/diet')
def diet():
    return redirect("https://huggingface.co/spaces/Supriyas-04/diet-workout", code=302)

@app.route('/stress')
def stress():
    return redirect("https://stress-management.streamlit.app/", code=302)

# New routes for pages
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
