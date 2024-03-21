import eel
import csv
import numpy as np
import joblib
from sklearn.preprocessing import StandardScaler
#Ignore all warnings
import warnings
warnings.filterwarnings("ignore")


# Initialize Eel
eel.init('web')#web is folder name in which your html and javascript file is there

# Load the trained model
model = joblib.load("Diabetese_Prediction.joblib")
modelX = joblib.load("Diabetese_Prediction.pkl")

def predict_diabetes(input_data):
    try:
        # Preprocess input data
        scaler = StandardScaler()
        #print(input_data)
        #print(np.array(input_data).reshape(1, -1))
        X = scaler.fit_transform(np.array(input_data).reshape(1, -1))
        # Predict using the trained model
        prediction = model.predict(np.array(input_data).reshape(1, -1))
        #print(prediction)
        predictionX = model.predict(X)
        #print(predictionX)
        return prediction[0],predictionX[0],"Has Diabetes" if prediction[0] == 1 else "Does Not Have Diabetes"
    except Exception as e:
        return prediction[0],predictionX[0],"Has Diabetes" if predictionX[0] == 1 else "Does Not Have Diabetes"
    else:
        return f"Error predicting: {str(e)}"

#Expanding My Database 
def write_to_csv(input_data,without_scaler,with_scaler,compare):
    try:
        with open('Diabetese_Predictions.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            if file.tell() == 0:
                writer.writerow(['Gender', 'Age', 'Hypertension', 'Heart Disease', 'Smoking History','BMI', 'HbA1c_Level', 'Blood_Glucose_Level',
                                 'Predicted_Diabetes_Without_Scaler','Predicted_Diabetes_With_Scaler',"Result_Comparision_Of_Scalers"])
            writer.writerow(input_data+[without_scaler,with_scaler,compare])
            #print(input_data+[without_scaler,with_scaler,compare])
    except Exception as e:
        print(f"Error writing to CSV: {str(e)}")
# Expose the function to JavaScript
@eel.expose #Javascript is named "eel.js" it is in eel library folder
def Diabetes_Prediction(gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level):
    try:
        # Convert input data to appropriate format
        input_data = [
            int(gender), int(age), int(hypertension), int(heart_disease), int(smoking_history),
            float(bmi), float(hba1c_level), float(blood_glucose_level)
        ]
        # Make the prediction using the model
        without_scaler,with_scaler,result = predict_diabetes(input_data)
        compare=without_scaler==with_scaler
        write_to_csv(input_data,without_scaler,with_scaler,compare)
        return result
    except Exception as e:
        return f"Error processing input: {str(e)}"

# Start the Eel application
try:
    eel.start('app.html', size=(800, 600))
except Exception as e:
    print(f"Error starting Eel: {e}")
