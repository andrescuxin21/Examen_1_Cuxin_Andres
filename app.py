from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'clave_secreta'

@app.route('/')
def index():
    name = "Andre Ricardo Cuxin Xool"
    age = 21
    height = 1.68
    return render_template('index.html', name=name, age=age, height=height)

@app.route('/skills')
def skills():
    skills_list = ["Deportivos", "Programación", "Matematicos", "Eficiente", "Comunicativo"]
    return render_template('skills.html', skills=skills_list)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        email = request.form['email']
        full_name = request.form['full_name']
        last_name = request.form['last_name']
        age = request.form['age']
        gender = request.form['gender']
        phone_number = request.form['phone_number']
        description = request.form['description']
        print("Correo:", email)
        print("Nombre completo:", full_name)
        print("Apellidos:", last_name)
        print("Edad:", age)
        print("Género:", gender)
        print("Número de teléfono:", phone_number)
        print("Descripción:", description)
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
