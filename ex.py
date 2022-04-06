# -------------------------- Machine Learning and AI Imports ----------------------------
import random , json , pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
# --------------------------- Flask and Web Imports ----------------------------------
import webbrowser
from flask import Flask,render_template,redirect,request,url_for

app = Flask(__name__)

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("intents.json").read())

words = pickle.load(open('words.pkl','rb'))
classes = pickle.load(open('classes.pkl','rb'))
model = load_model("chatbotmodel.h5")

def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = clean_up_sentence(sentence)
    bag= [0]*len(words)
    for w in sentence_words:
        for i,word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [(i,r) for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x:x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]] , 'probability':str(r[1])})
    return return_list

def get_response(intents_list , intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            # break
    if tag == 'registeration':
        result = "Redirecting..........."
        webbrowser.open("http://192.168.0.110:3030/")
    return result

@app.route("/" , methods=['POST','GET'])
def index():
    return render_template("index.html")

@app.route("/get")
def getresponse():
    userText = request.args.get('msg')
    ints = predict_class(userText)
    res = get_response(ints, intents)
    return str(res)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=3030)

# print()
# print("Hey Iam ChatBot Ask Me Something")

# while True:
#     message = input("Me : ")
#     ints = predict_class(message)
#     res = get_response(ints, intents)
#     print(res)