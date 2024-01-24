from flask import Flask, render_template, request, redirect
from extractors.remo import extract_remo_jobs
from extractors.wwr import extract_wwr_jobs

app = Flask("Job Scrapper")

db = {}


@app.route("/")
def hello():
  return render_template("index.html")


@app.route("/search")
def search():
  keyword = request.args.get("keyword")
  if keyword == None:
    return redirect("/")

  if keyword in db:
    jobs = db[keyword]
  else:
    remo = extract_remo_jobs(keyword)
    wwr = extract_wwr_jobs(keyword)
    jobs = remo + wwr
    db[keyword] = jobs
  return render_template("search.html", keyword=keyword, jobs=jobs)


app.run("0.0.0.0")
