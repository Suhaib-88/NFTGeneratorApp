from nft import photo2pixelart,overlay_pictures
from flask import Flask,request,render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route("/NFT_Generator",methods=['POST'])
def NFT_Generator():
    if request.method=='POST':
        new_img=overlay_pictures()
        photo2pixelart('new.png', (45,45))
        
    return render_template('result.html')

if __name__=="__main__":
    app.run()