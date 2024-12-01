# app.py
from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcola', methods=['POST'])
def calcola():
    try:
        tipo_cloro = request.form['tipo_cloro']
        volume_acqua = float(request.form['volume_acqua'])
        ppm_desiderati = float(request.form['ppm_desiderati'])
        
        percentuale_cloro = 40 if tipo_cloro == 'granulare' else 14
        volume_litri = volume_acqua * 1000
        quantita_cloro_ml = (volume_litri * ppm_desiderati) / (percentuale_cloro * 10)
        
        return jsonify({
            'success': True,
            'risultato': round(quantita_cloro_ml, 2),
            'tipo_cloro': 'Granulare (40%)' if tipo_cloro == 'granulare' else 'Liquido (14%)',
            'volume_acqua': volume_acqua,
            'ppm_desiderati': ppm_desiderati
        })
    except:
        return jsonify({'success': False, 'error': 'Errore nel calcolo'})

if __name__ == '__main__':
    app.run(debug=True)