from pdf2image import convert_from_path, convert_from_bytes
from PIL import Image, ImageEnhance, ImageFilter
import pytesseract as pys
from flask import Flask,render_template,request
app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'uploads/'
app.config['OUT_FOLDER'] = 'out/'

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(app.config['UPLOAD_FOLDER']+'out.pdf')
      print(f)
      images = convert_from_path(app.config['UPLOAD_FOLDER']+'out.pdf')
      i=0
      txt=""
      for page in images:
          page.save(app.config['OUT_FOLDER']+str(i)+'.jpg','JPEG')
          txt = txt+pys.image_to_string(Image.open(app.config['OUT_FOLDER']+str(i)+'.jpg'))
          i=i+1
      return txt


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
