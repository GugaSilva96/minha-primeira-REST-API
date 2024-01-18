from flask import Flask, request

app = Flask(__name__)


@app.route("/<numero>", methods=["GET", "POST"])
def ola(numero):
    if request.method == "POST":
        return "Requisição POST recebida! {}".format(numero)
    else:
        return "Requisição GET recebida!{}".format(numero)


if __name__ == "__main__":
    app.run(debug=True)
