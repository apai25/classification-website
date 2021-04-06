from flaskr import app, forms
from flask import render_template, redirect, url_for
from util.classifier import KNeighborsClassifier
from util.data_preprocessing import preprocess_data


@app.route('/', methods=['GET', 'POST'])
def home():
    form = forms.UploadForm()
    classification_statement = False
    if form.validate_on_submit():
        classifier = KNeighborsClassifier(n_neighbors=int(form.n_neighbors.data))

        form.training_data.data.save('flaskr/data/training_data.csv')
        form.prediction_data.data.save('flaskr/data/prediction_data.csv')

        X_train, y_train, test = preprocess_data()
        classifier.fit(X_train, y_train)
        classification = classifier.predict(test)
        classification_statement = f'Classification: {classification}'

    return render_template('home.html', form=form, prediction=classification_statement)

if __name__ == '__main__':
    app.run(debug=True)
