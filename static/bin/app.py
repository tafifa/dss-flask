from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    nama = request.form['nama']
    jenisPekerjaan = request.form['c1']
    jumlahPenghasilan = request.form['c2']
    jumlahTanggungan = request.form['c3']
    nilaiIpk = request.form['c4']
    c5 = request.form['c5']
    
    with open('data.txt', 'a') as f:
        f.write(f'{nama}, {jenisPekerjaan}, {jumlahPenghasilan}, {jumlahTanggungan}, {nilaiIpk}, {c5} \n')

    return jsonify({'message': 'Data submitted successfully!'})

if __name__ == '__main__':
    app.run(debug=True)