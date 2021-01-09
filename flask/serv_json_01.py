from flask import Flask, request, json
app = Flask(__name__)

@app.route('/api/json_data', methods=['GET', 'POST'])
def json_data():
    if request.method == 'POST':
        data = {
            'message': 'Hello, I\'s Virat ',
            'desc': 'This is message from json Service'
        }
        return method1()
        #return json.dumps(data, indent=4)
        #return json.load(data)
    return '200'

@app.route('/api/policy', methods=['POST'])
def policy_data():
    if request.method == 'POST':
        try:
        with open(file,'r',encoding='utf-8') as f:
            load_data = json.load(f)
        except Exception as e:
            print(e)
        response = app.response_class(
            response=json.dumps(load_data),
            mimetype='application/json'
        )                                   
        return response
    return '200'

def method1():
    try:
        with open('policy.json','r',encoding='utf-8') as f:
            comfirm_med = json.load(f)
    except Exception as e:
        print(e)
    #return json.dumps(comfirm_med)    

    response = app.response_class(
        response=json.dumps(comfirm_med),
        mimetype='application/json'
    )                                   
    return response