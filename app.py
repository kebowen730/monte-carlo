'''
NOTES
-----
- bootstrapped code from flask docs (http://flask.pocoo.org/docs/0.12/patterns/fileuploads/)
'''

import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import keras
from keras.preprocessing import image
from keras import backend as K

UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024 <--(uncomment to limit the maximum upload size to 16 megabytes. If a larger file is transmitted, Flask will raise an RequestEntityTooLarge exception)

model = None
graph = None

# @TODO: update boilerplate  keras code to work with our model/expected images
# Loading a keras model with flask --> (https://blog.keras.io/building-a-simple-keras-deep-learning-rest-api.html)

'''def load_model():
    global model
    global graph
    model = keras.models.load_model("mnist_trained.h5")
    graph = K.get_session().graph

# @TODO: update once fixed
# load_model()

def prepare_image(img):
    # Convert the image to a numpy array
    img = image.img_to_array(img)
    # Scale from 0 to 255
    img /= 255
    # Invert the pixels
    img = 1 - img
    # Flatten the image to an array of pixels
    image_array = img.flatten().reshape(-1, 28 * 28)
    # Return the processed feature array
    return image_array'''


# Checks if an extension is valid
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Uploads the file and redirects the user to the URL for the uploaded file
@app.route('/', methods=['GET', 'POST'])
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
            # save file to uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # @TODO: REPLACE BOILERPLATE CODE (Keras image processing from 4/.../04-Evr_MNIST_Heroku)
            '''
	        # Load the saved image using Keras and resize it to the mnist format of 28x28 pixels
            image_size = (28, 28)
            im = image.load_img(filepath, target_size=image_size, grayscale=True)

            # Convert the 2D image to an array of pixel values
            image_array = prepare_image(im)
            print(image_array)

            # Get the tensorflow default graph and use it to make predictions
            global graph
            with graph.as_default():

                # Use the model to make a prediction
                predicted_digit = model.predict_classes(image_array)[0]
                data["prediction"] = str(predicted_digit)

                # indicate that the request was a success
                data["success"] = True

            return jsonify(data)
            '''
            return redirect(url_for('uploaded_file', filename=filename))

    return render_template("index.html")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Function to serve uploaded files (returns file of specified name from upload_file()
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    # image = send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    # return url_for('uploaded_file', filename=filename)
    # return render_template('results.html', image=image)


if __name__ == "__main__":
    app.run(debug=True)
