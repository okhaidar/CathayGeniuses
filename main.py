from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("front.html", content="opa", image2="https://lifestyle-api.asiamiles.com/medias/X-mas-Gift-Box-Mood-Shot.jpg-AML-Convert-294Wx195H?context=bWFzdGVyfGltYWdlc3wzNDI5NnxpbWFnZS9qcGVnfGFHTTNMMmd6TkM4eE1qUXdPREkxTnpBNE5UUTNNQzlZSjIxaGN5QkhhV1owSUVKdmVDQk5iMjlrSUZOb2IzUXVhbkJuWDBGTlRDMURiMjUyWlhKMExUSTVORmQ0TVRrMVNBfDM5MzIyOTI2NjgwMDAzYTVlNzhmNGFlOGJkOThkY2RiZGY2NzJmOTZjNGM2NDU2YjM4NWVhODg2NjFjYmMwYjA")
    #return "hello"
@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("front.html")


@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin!"))
if __name__ == "__main__":
    app.run(port=5001)