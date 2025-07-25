from flask import Flask, render_template, request, jsonify

app = Flask(__name__) 

# Sample dictionary for symptom suggestions
symptom_data = {
    "fever": "You may have an infection. Rest, hydrate, and monitor temperature.",
    "cough": "Could be a cold or allergy. Drink warm fluids and rest.",
    "headache": "Rest, stay hydrated. Persistent pain may need a doctor's check.",
    "sore throat": "Gargle with warm salt water, avoid cold drinks.",
    "chest pain": "⚠ Seek immediate medical help.",
    "shortness of breath": "⚠ Could be serious. Visit a hospital.",
    "nausea": "Avoid oily food, hydrate, and rest.",
    "diarrhea": "Drink ORS, avoid spicy food. Consult if persistent.",
    "body ache": "Rest and mild pain relief may help.",
    "runny nose": "Likely cold or allergy. Use antihistamines if needed."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/check', methods=['POST'])
def check_symptoms():
    data = request.get_json()
    symptoms = [s.strip().lower() for s in data.get('symptoms', '').split(',')]
    results = {}

    for symptom in symptoms:
        if symptom in symptom_data:
            results[symptom] = symptom_data[symptom]

    if not results:
        return jsonify({"status": "no_match", "message": "No known symptoms matched. Please consult a doctor."})
    
    return jsonify({"status": "success", "results": results})

if __name__ == '__main__':
    app.run(debug=True)