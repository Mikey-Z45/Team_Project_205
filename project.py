from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap
from sightengine.client import SightengineClient

UPLOAD_FOLDER = 'https://github.com/Mikey-Z45/Team_Project_205/tree/master/uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

client = SightengineClient('{api_user}', '{api_secret}') # don't forget to add your credentials

@app.route('/', methods=['GET', 'POST'])
def boot():
    return render_template('projectIndex.html')

#
# not sure if this upload file function works yet or not, there is no way to actually input a file
# but we I will keep looking at it, i found this code at http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
#
'''
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',
                                    filename=filename))
'''
# pulled this info from https://medium.com/@antoinegrandiere/image-upload-and-moderation-with-python-and-flask-e7585f43828a
# it uses and API that checks and makes sure nobody uploads bad images or profane images
# i just need to figure out how to use the API
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['image']
    filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)

    file.save(filename)
    invalidImage = False

    output = client.check('nudity', 'wad', 'celebrities', 'scam', 'face-attributes').set_file(filename)

    # contains nudity
    if output['nudity']['safe'] <= output['nudity']['partial'] and output['nudity']['safe'] <= output['nudity']['raw']:
        invalidImage = True
    # contains weapon, alcohol or drugs
    if output['weapon'] > 0.2 or output['alcohol'] > 0.2 or output['drugs'] > 0.2:
        invalidImage = True
    # contains scammers
    if output['scam']['prob'] > 0.85:
        invalidImage = True
    # contains celebrities
    if 'celebrity' in output:
        if output[0]['prob'] > 0.85:
            invalidImage = True
    # contains children
    if 'attributes' in output:
        if output['attributes']['minor'] > 0.85:
            invalidImage = True

    if invalidImage:
        os.remove(filename)

        return render_template('projectIndex.html', invalidImage=invalidImage, init=True)

app.run()
