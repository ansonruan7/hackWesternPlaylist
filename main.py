from flask import Flask, request, render_template  # Import Flask Class
# from cohereGen import flaskTrans
app = Flask(__name__)  # Create an Instance
uri = "spotify:episode:7makk4oTQel546B0PZlDM5"


@app.route('/')  # Route the Function
def main():  # Run the function
  return render_template('index.html')


@app.route("/generate", methods=["GET", "POST"])
def need_input():
  funnySentence = request.form.get("sentence")
  # flaskTrans(funnySentence)
  #funnysentence -> cohere -> spotify -> spotify spits uri
  #uri -> new generated.html
  return render_template('generated.html', uri=str(uri))

@app.route("/regen", methods=["GET", "POST"])
def restart():
  return render_template('index.html')

@app.route("/form", methods=["GET"])
def get_form():
  return render_template('index.html')


app.run(host='0.0.0.0', port=5000,debug=True)  # Run the Application (in debug mode),


#thigns we need from user
#spotify client, secret, <- optional demo purpoess

#Spotify playlist uri from the owner of client and secret <-- !!!!!!!!!
#Input for funny sentences


