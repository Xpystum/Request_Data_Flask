from flask import Flask, request

# import main Flask class and request object
from flask import Flask, request

# create the Flask app
app = Flask(__name__)

@app.route('/query-example2/<phrase>')
def query_example2(phrase):
    #При получении любого значение <phrase> http://127.0.0.1:5000/query-example2/test_provirka
    # language = request.args.get('language')
    return f"<h1>The Language value is: {phrase}</h1>"

@app.route('/query-example')
def query_example():
    #При отправки атрибута language со значением или без http://127.0.0.1:5000/query-example?language=Python
    language = request.args.get('language')
    return f"<h1>The Language value is: {language}</h1>"

@app.route('/form-example',  methods=['GET', 'POST'])
def form_example():
    #Проверка на метод - POST или GETY
    if request.method == 'POST':
        language = request.form.get('language')
        framework = request.form.get('framework')
        return '''
                  <h1>The language value is: {}</h1>
                  <h1>The framework value is: {}</h1>'''.format(language, framework)

    # otherwise handle the GET request
    return '''
        <form method="POST">
            <div><label>Language: <input type="text" name="language"></label></div>
            <div><label>Framework: <input type="text" name="framework"></label></div>
            <input type="submit" value="Submit">
        </form>'''

# GET requests will be blocked
@app.route('/json-example', methods=['GET','POST'])
def json_example():
    request_data = request.get_json()

    language = None
    framework = None
    python_version = None
    example = None
    boolean_test = None

    if request_data:
        if 'language' in request_data:
            language = request_data['language']

        if 'framework' in request_data:
            framework = request_data['framework']

        if 'version_info' in request_data:
            if 'python' in request_data['version_info']:
                python_version = request_data['version_info']['flask']

        if 'examples' in request_data:
            if (type(request_data['examples']) == list) and (len(request_data['examples']) > 0):
                example = request_data['examples'][2]

        if 'boolean_test' in request_data:
            boolean_test = request_data['boolean_test']

    return '''
           The language value is: {}
           The framework value is: {}
           The Python version is: {}
           The item at index 0 in the example list is: {}
           The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)


#Чтобы прочитать данные, вы должны понимать, как Flask переводит данные JSON в структуры данных Python:
#1. Все, что является объектом, преобразуется в словарь Python. {"key" : "value"}в JSON соответствует somedict['key'], который возвращает значение в Python.
#2. Массив в JSON преобразуется в список в Python. Поскольку синтаксис тот же, вот примерный список:[1,2,3,4,5]
#3. Значения внутри кавычек в объекте JSON становятся строками в Python.
#4. Boolean true и false становятся True и False в Python.
#5. Наконец, числа без кавычек вокруг них становятся числами в Python.

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)