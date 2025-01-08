from flask import Flask, session, render_template, request



app2 = Flask(__name__)
app2.secret_key = "123"

# uncomment the 3 lines below to use server file sessions
# from flask_session import Session
#app2.config['SESSION_TYPE'] = 'filesystem'
#server_session = Session(app2)

@app2.context_processor
def inject_enumerate():
    return dict(enumerate=enumerate)


@app2.route("/", methods=["GET"])
def index():
    messages = session.get("messages", [])
    return render_template("index2.html", messages=messages)


@app2.route("/clear", methods=["POST"])
def clear_messages():
    session["messages"] = []
    return index()


@app2.route("/add", methods=["POST"])
def add_message():
    messages = session.get("messages", [])
    messages.append(request.form["new_message"])
    session["messages"] = messages
    return index()


# code below is not necessary for the example


# initializing code before every request
@app2.before_request
def before_request():
    # ... useful code here
    print("initialize")


# initializing code once for the whole app - does not do anything
@app2.before_request
def initializeApp():
    # ... useful code here
    print("initializeApp")
    app2.before_request_funcs[None].remove(initializeApp)


# convenient method to run in development environment with:
# python app2.py
if __name__ == "__main__":
    app2.run()
