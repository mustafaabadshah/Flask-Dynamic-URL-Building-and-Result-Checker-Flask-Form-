###  integrate html with flask
### HTTP verb Get and Post
from Flask import Flask, redirect, url_for, render_template,request


app = Flask(__name__)
@app.route("/")
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Pass"
    else:
        res="Fail"
    return render_template('/result.html',result=res)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has fail and marks is "+str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has fail and marks is "+str(score)

@app.route("/results/<int:marks>")
def results(marks):
    if marks<50:
        results="fail"
    else:
        results="success"
    return redirect(url_for(results, score=marks))
   
   #result checker submit html page
@app.route("/submit", methods=["POST", "GET"])
def submit():

    if request.method == "POST":
        science = float(request.form["science"])
        maths = float(request.form["maths"])
        c =float(request.form["c"])
        datascience = float(request.form["datascience"])
        total_score = ((science) + int(maths) + int(c) + int(datascience))/4
        res=""    
        return redirect(url_for('success', score=total_score))

if __name__ == "__main__":
    app.run(debug=True)