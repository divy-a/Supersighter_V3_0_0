from flask import Flask, request, jsonify, render_template
from supersighter import searcher
import random
import requests
from supersighter import searcher
import csv
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

@app.route("/admin")
def admin():
    return render_template('admin.html')

@app.route("/admin/update")
def admin_update():
    if request.args.get('code')=='694200':
        try:
            durl = request.args.get('durl')
            key = request.args.get('key')
            print(key)
            print(durl)
            response = requests.get(str(durl))
            fileName = str(random.random()).replace('.', '')
            open(f'data_files/{fileName}' , 'wb').write(response.content)
            file = open(f'data_files/{fileName}', mode='r', encoding='utf-8')
            csvFile = csv.DictReader(file)
            searcher.data = []
            searcher.allData = []
            for lines in csvFile:
                searcher.data.append(lines[str(key)])
                searcher.allData.append(lines)
        
            return 'Updated', 200
        
        except Exception as e:
            print(e)
            return 'Update Failed', 400
            
        
        
    else:
        return 'Update Failed', 400


#@app.route("/admin/authenticate", ['POST'])
#def admin_auth():
#    if(check_credentials(request.headers['user_id'], request.headers['password'])):
#        sessionId = random.random()
#        update_in_Session_id(session_id)
#        return sessionId, 200
#    else:
#        return 'Invalid Credentials', 500
    

if __name__ == '__main__':
    app.run(debug=True)
