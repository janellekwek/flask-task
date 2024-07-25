from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

final=[]

@app.route("/", methods=["POST","GET"])
def home():
    if request.method=="POST":
        final.append({"contact":request.form["contact"], "handphone":request.form["handphone"],"email":request.form["email"]})
        return render_template("index.html", stuff=final)
    else:
        return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True, port=12344)
