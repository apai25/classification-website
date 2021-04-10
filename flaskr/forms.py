from flask_wtf import FlaskForm # FlaskForm is a class that tcan be inherited from to create cutomizable forms. This is provided by the flask_wtf library.
from wtforms import SubmitField, SelectField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

POSSIBLE_K_NEIGHBORS = ['1', '2', '3', '4', '5']

class UploadForm(FlaskForm):
    training_data = FileField(label='Please upload a csv file containing the training data: ', 
                              validators=[FileAllowed(['csv'], 
                              message='Make sure that you are uploading a csv file.'), DataRequired()])

    prediction_data = FileField(label='Please upload a csv file containing the prediction data: ', 
                                validators=[FileAllowed(['csv'], 
                                message='Make sure that you are uploading a csv file.'), DataRequired()])
    
    n_neighbors = SelectField(label='Please select the number of neighbors the classifier should use for classification: ',
                              choices=POSSIBLE_K_NEIGHBORS,
                              validators=[DataRequired()])

    submit = SubmitField(label='Submit')