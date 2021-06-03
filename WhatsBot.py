from flask import Flask,request
from twilio.twiml.messaging_response import MessagingResponse
from textblob import TextBlob
from textblob import Word
from textblob.wordnet import VERB
import nltk
import random

app= Flask(__name__)


@app.route("/reply", methods=['POST'])
def reply():
    
    chat= request.form.get('Body')
    message=chat
    rep= MessagingResponse()
    Wishes=[message == "Hii",message == "hii", message == "Hey",message ==  "hey", message == "Dei", message == "dei",message == "hi"]
    Tamilwishes=[message == "vanakam",message == "Vanakam",message ==  "Namashakaram"]
    Starts=["Hey Dharani","வணக்கம் தரணி", "Hii Kanna", "Hey Bro", "Ena Nanba"]
    End=["😍😍","Bye","Tata"]
    Modes=["Sentiment Analysis", "Translator"]

    if (any(Wishes)):
        rep.message(random.choice(Starts))

    elif(any(Tamilwishes)):
        rep.message(random.choice(Starts))
    
    elif (message == ("I can do it")):
        rep.message("Yea...! You Born for doing it")

    elif((message != Wishes) and (message!= Tamilwishes)):

        ######################--------sentiment_analysis----------##################################

        lst=message[0:18]
        lst2=message[21:]
        def sentiment_analysis(lst2):
            test=TextBlob(lst2)
            b=test.correct()
            rep.message(str(test.sentiment))
        
        ######################---------TRANSLATOR----------#########################################

        lst3=message[0:16]
        lst4=message[19:]
        def Tamil_Translator(lst4):
            test=TextBlob(lst4)
            b=(test.correct())
            rep.message (str(b.translate(from_lang=u'auto',to=u'ta')))

        if message== "User Guide":
           rep.message ("Modes=['Sentiment Analysis = any sentimental words or sentence','Translator = try any lang to change in tamil']")

        elif lst3=="Tamil Translator":
            Tamil_Translator(lst4)
            
        elif lst=="Sentiment Analysis":
            sentiment_analysis(lst2)

        else:
            blob=TextBlob(message)
            b=str(blob.correct())           #       added auto correction to this
            a=str(Word(b).definitions)      #       Explanation for a word is(Definition)
            rep.message(a[2:-2])

    else:
        rep.message(random.choice(End))
    
    return str(rep)

if __name__ == "__main__":
    app.run(debug=True)
    
