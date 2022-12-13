from flask import Flask
from utils import get_all, get_by_pk, get_by_skill

app = Flask(__name__)


@app.route("/")
def index():
    candidates = get_all()
    resultat = '<br>'
    for candidate in candidates:
        resultat += candidate['name'] + '<br>'
        resultat += candidate['position'] + '<br>'
        resultat += candidate['skills'] + '<br>'
        resultat += '<br>'

    return f'<pre> {resultat} </pre>'


@app.route("/candidates/<int:pk>")
def candidate(pk):
    candidate = get_by_pk(pk)
    if not candidate:
        resultat = 'По данному id кандидат не найден.'
    else:
        url = candidate['picture']
        resultat = f'<img src={url}><br><br>'
        resultat += candidate['name'] + '<br>'
        resultat += candidate['position'] + '<br>'
        resultat += candidate['skills'] + '<br>'
        resultat += '<br>'

    return f'<pre>{resultat}</pre>'


@app.route("/candidates/<skill>")
def candidates_skill(skill):
    candidates_skills = get_by_skill(skill)
    resultat = '<br>'
    for candidate in candidates_skills:
        resultat += candidate['name'] + '<br>'
        resultat += candidate['position'] + '<br>'
        resultat += candidate['skills'] + '<br>'
        resultat += '<br>'

    return f'<pre> {resultat} </pre>'


if __name__ == '__main__':
    app.run(debug=True)
