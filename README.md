# [Diabetes Prediction Using Machine Learning](https://replit.com/@shivampatel2552/DiabetesPredictionUsingMachineLearning)
## External Library Used Pandas,Seaborn,Numpy,Scikit-Learn,Eel,MatplotLib
### Installing :- go to Terminal/CommandPrompt type ```pip install -r reqdment.txt``` or run ```installer.py```

**Creating Jupyter Environment**
1) Download Suitable Python installer from [Python.Org](https://www.python.org/)
2) When Installing It in Windows **MUST SELECT ADD PYTHON TO PATH OPTION**
3) Open Terminal/Command Prompt type ```pip install virtualenv```
4) After Installation is completed Type ```virtualenv <Virtual_Environment_Folder_Name_of_Your_Choice (example : venv)>```
5) For Linux User type in terminal ```source path_to/venv/bin/activate``` for windows user type in command prompt```path_to\venv\Scripts\activate```
6) after acivating virtual environment type ```pip install jupyterlab```
7) after jupyterlab is installed run it by typing ```jupyter lab```
___Hence Jupyter Environment Is Created___

## About Dataset

### Source :- https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset

The Diabetes prediction dataset is a collection of medical and demographic data from patients, along with their diabetes status (positive or negative). The data includes features such as age, gender, body mass index (BMI), hypertension, heart disease, smoking history, HbA1c level, and blood glucose level.

=> Gender - Gender refers to the biological sex of the individual, which can have an impact on their susceptibility to diabetes.

         -  male
         -  other
         -  female
         
=> Age - Age is an important factor as diabetes is more commonly diagnosed in older adults.Age ranges from 0-80 in our dataset.

=> Hypertension - Hypertension is a medical condition in which the blood pressure in the arteries is persistently elevated.

=> Heart Disease - Heart disease is another medical condition that is associated with an increased risk of developing diabetes.

=> Smoking_History - Smoking history is also considered a risk factor for diabetes and can exacerbate the complications associated
 
     -  never : Indicates individuals who have never smoked.
     -  No Info : Suggests that there is no information available regarding their smoking history.
     -  current : Represents individuals who currently smoke.
     -  former:  Indicates individuals who used to smoke but have quit.
     -  ever : Possibly indicating individuals who have smoked at some point, irrespective of current status.
     -  not current : Suggests individuals who are not currently smoking.
     
=> BMI - BMI (Body Mass Index) is a measure of body fat based on weight and height. Higher BMI values are linked to a higher risk

=> HbA1c - HbA1c (Hemoglobin A1c) level is a measure of a person's average blood sugar level over the past 2-3 months. Higher level

=> Blood_Glucose_Level - Blood glucose level refers to the amount of glucose in the bloodstream at a given time. High blood glucose levels are a key

=> Diabetes - Diabetes is the target variable being predicted, with values of 1 indicating the presence of diabetes and 0 indicating the absence of diabetes.

Note:-

The following Features are Most important features to predict Diabetes :

    HbA1c level:
        Normal: Less than 5.7%
        Prediabetes: 5.7% to 6.4%
        Diabetes: 6.5% or higher

    Fasting blood glucose level:
        Normal: Less than 100 mg/dL
        Prediabetes: 100 mg/dL to 125 mg/dL
        Diabetes: 126 mg/dL or higher
        
## [See Model at Kaggel](https://www.kaggle.com/sh1vam2003/diabetes-prediction)
## [Run Application on Replit](https://replit.com/@shivampatel2552/DiabetesPredictionUsingMachineLearning)

Software Requirements :-
           [Python](https://www.python.org/) ,
           [Chromium](https://www.kali.org/tools/chromium/) / [Chrome](https://www.google.com/intl/en_in/chrome/) Browser

# Future Scope

+ Ask User if the Output is correct to not and then add/record user response to CSV File. <p>
+ Add Obesity Prediction based on BMI and also predict its Category. <p>
+ Predict if person is UnderWeight or not based on BMI. <p>
+ Instead of taking BMI use Hight and Weight of person to calculate it based on formula. <p>
+ Add Explaination for given output.
