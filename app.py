from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        return redirect(url_for('information', name=name, email=email, phone=phone, message=message))
    return render_template('send.html')


@app.route('/information', methods=['GET', 'POST'])
def information():
    if request.method == 'POST':
      
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')
        
        return redirect(url_for('success', name=name, email=email, phone=phone, message=message))
    
  
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    message = request.args.get('message')
    return render_template('information.html', name=name, email=email, phone=phone, message=message)


@app.route('/success')
def success():
    
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    message = request.args.get('message')
    return render_template('success.html', name=name, email=email, phone=phone, message=message)

if __name__ == "__main__":
    app.run(debug=True)