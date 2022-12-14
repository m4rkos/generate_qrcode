import os
from class_tools import Tools
from flask import Flask, render_template, redirect, request
from flask_cors import CORS

app = Flask(__name__, template_folder='./templates', static_url_path='', static_folder='./static')
CORS(app)
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})


@app.route("/", methods=['GET'])
def base():
    a = Tools()

    value = 'https://google.com'
    print(f"\n{value}\n")

    qr_image = 'qr_codes/02648d98-c7d5-487b-96a2-005b474d62f1.png'
    if os.path.exists(f'./static/{qr_image}') == False:
        qr_image = a.save_qrcode(value)['name']
    
    a.show_qrcode(value)

    return render_template("index.html", qr_code=qr_image, label=value)


@app.route("/generate", methods=['POST'])
def base_genarate():
    a = Tools()
    
    if request.form['item']:
        value = request.form['item']
        qr_image = a.save_qrcode(value)
        a.show_qrcode(value)

        return redirect(f"/qrcode/{qr_image['id']}")

    return redirect('/')


@app.route("/qrcode/<id>", methods=['GET'])
def base_qrcode(id):
    return render_template("qrcode.html", qr_code=id)


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html", msg=e)


def app_routes():
    app.run(debug=False, port=5000)


if __name__ == '__main__':
    app_routes()