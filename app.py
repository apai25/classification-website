from flaskr import app, forms # These imports are from the __init__.py file in the folder flaskr.
# The render_template function is one provided by the flask framework. It reads an HTML file with Jinja2 templating to integrate a Python backend with an HTML/CSS frontend.
from flask import render_template 
from util.classifier import KNeighborsClassifier # Imported from the classifier.py file in the util folder.
from util.data_preprocessing import preprocess_data # imported from the data_preprocessing.py file in the util folder.


@app.route('/', methods=['GET', 'POST'])
def home():
    form = forms.UploadForm()
    prediction = False
    if form.validate_on_submit():
        classifier = KNeighborsClassifier(n_neighbors=int(form.n_neighbors.data))

        # The .save() method is a method that comes with the FlaskForm class provided by the Flask framework. It saves an uploaded file on the inputted file path.
        form.training_data.data.save('flaskr/data/training_data.csv')
        form.prediction_data.data.save('flaskr/data/prediction_data.csv')

        X_train, y_train, test = preprocess_data()
        classifier.fit(X_train, y_train)
        prediction = classifier.predict(test)

    # Using the render_template function to display "home.html" and pass in the form and prediction variables with Jinja2 templating.
    return render_template('home.html', form=form, prediction=prediction) 

if __name__ == '__main__':
    app.run(debug=True)
