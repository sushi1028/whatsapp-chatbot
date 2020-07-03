'''
python app.py
'''
# Initialise the modules
from     nltk.stem                       import WordNetLemmatizer
from     flask                           import Flask, request
from     twilio.twiml.messaging_response import MessagingResponse
from     tensorflow.keras.models         import  load_model
from     tensorflow.python.keras.backend import set_session
from     tensorflow.python.keras.backend import set_session
import   tensorflow
import   numpy                           as np
import   warnings
import   pickle
import   nltk
import   json
import   random

warnings.filterwarnings("ignore")
sess = tensorflow.Session()

lemmatizer  = WordNetLemmatizer()
graph       = tensorflow.get_default_graph()

set_session(sess)
model       = load_model('chatbot_model.h5')
intents     = json.loads(open('intents.json').read())
words       = pickle.load(open('words.pkl','rb'))
classes     = pickle.load(open('classes.pkl','rb'))

# Clean the words
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words
    # return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)

    global sess
    global graph
    with graph.as_default():
        set_session(sess)
        #y = model.predict(X)
        res = model.predict(np.array([p]))[0]

    ERROR_THRESHOLD = 0.25
    results         = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(msg):
    ints= predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

# Initialise app
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    print(msg)
    # Create reply
    response = chatbot_response(msg)
    # follow reply format
    resp = MessagingResponse()
    resp.message(response)
    
    print("Response from chatbot :",resp)
    
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)

