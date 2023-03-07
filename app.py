from flask import Flask, request, jsonify, render_template
from supersighter import searcher
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/search")
def search():
    
    results = searcher.get_results(request.args.get(
        'q'), request.args.get('max_results'), request.args.get('adv'))
    
    response = jsonify({
        'results': results
    })
    return response

@app.route("/getinfo")
def getinfo_template():
    id = request.args.get('id')
    return render_template('getinfo.html')


@app.route("/getinfo/<id>")
def getinfo(id):
    return jsonify(searcher.allData[int(id)])
    

if __name__ == '__main__':
    app.run(debug=True)
