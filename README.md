# Flask - Twilio Based chatbot
**1.** Create account on [Twilio](https://www.twilio.com/try-twilio)


**2.** Create new project
    >Select Products
    >Choose Programmable SMS
    >Click Continue
    >Give your project a name
    >Click Continue (and skip remaining steps if you want)

**3.** Open Programmable SMS Dashboard on project console and select WhatsApp Beta.


**4.** Learn features of Twilio Sandbox for WhatsApp.

   >Link your WhatsApp phone number to your Sandbox.
   >Shortcut link: https://api.whatsapp.com/send?phone=+14155238886&text=join%20horn-metal
   >Send a One-Way WhatsApp Message. (Notice that outbound messages have a predefined format)
   >Test Two-Way Messaging


**5.** Setup a Python Virtual Environment

   >A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.

   i. Create a Project Folder.

   ii. Run following command to create a new virtual environment inside your project folder:
    
     python3 -m venv chatboatenv
    
   >After running above command, a folder named myvenv will get created in your project folder.

   iii. Activate the virtual environment by running following command:
   
   For ubuntu and mac users:

         source chatboatenv/bin/activate

   For windows users:

          chatboatenv\Scripts\activate


**6.** Install required Python Packages:

   >flask
   
```pip install flask```
    
   >twilio

```pip install twilio```
    
   >tensorflow

```pip innstall tensorflow```

   >nltk
   
```pip install nltk```



**7.** To Train a model with your custom data, Add your dialogues to intents.json & then run

```python3 train_model.py```



**8.** Run the flask app

```python app.py```



**9.** For local testing: Generate Public URL for Webhook using ngrok.io

   >*ngrok is a free tool that allows us to tunnel from a public URL to our application running locally.*

   i. Download [ngrok](https://ngrok.com/download).

   ii. Run ngrok from command line (from the location where executable is stored)

```./ngrok http 5000```

   iii. Copy the HTTPS Forwarding URL

   iv. Paste it as the webhook URL for incoming messages in your twilio sandbox configuration. 


**Congratulation**, **You can test your bot now.**
