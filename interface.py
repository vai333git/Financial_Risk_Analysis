# Here we will write all the api's  and converge all the files

from flask import Flask,render_template,jsonify,request
from Project_app.utils import Risk_Assessment
# import os

# Creating flask instance
app = Flask(__name__)
# Special variable that evaluates name of the current module

# Source File == Main Programme then '__name__' == '__main__'
# Source File != Main Programme then '__name__' == filename

# __name__ represents name of the application package and is used by the flask to identify resources
# like templates, static assets and their instance folder

# BASE API
@app.route('/')
def home():
    print('this is home api')
    return render_template('index.html')

@app.route('/submit',methods = ['POST','GET'])
def predict():
    print('This is submit api')

    if request.method == 'POST':
        
        loan_amnt = float(request.form['loan_amnt'])
        term = str(request.form['term'])
        emp_length = float(request.form['emp_length'])
        home_ownership = str(request.form['home_ownership'])
        annual_inc = float(request.form['annual_inc'])
        verification_status = str(request.form['verification_status'])
        pymnt_plan = str(request.form['pymnt_plan'])
        purpose = str(request.form['purpose'])
        zip_code = str(request.form['zip_code'])
        total_acc = float(request.form['total_acc'])
        total_pymnt = float(request.form['total_pymnt'])
        recoveries = float(request.form['recoveries'])
        last_pymnt_d = str(request.form['last_pymnt_d'])
        last_pymnt_amnt = float(request.form['last_pymnt_amnt'])
        last_credit_pull_d = str(request.form['last_credit_pull_d'])
        application_type = str(request.form['application_type'])
        debt_settlement_flag = str(request.form['debt_settlement_flag'])
        last_fico_range_high = float(request.form['last_fico_range_high'])
        last_fico_range_low = float(request.form['last_fico_range_low'])
        tot_coll_amt = float(request.form['tot_coll_amt'])
        tot_cur_bal = float(request.form['tot_cur_bal'])


        ra = Risk_Assessment(loan_amnt,term,emp_length,home_ownership,annual_inc,verification_status,pymnt_plan,purpose,zip_code,total_acc,total_pymnt,recoveries,last_pymnt_d,last_pymnt_amnt,last_credit_pull_d,application_type,debt_settlement_flag,last_fico_range_high,last_fico_range_low,tot_coll_amt,tot_cur_bal)
    
        result = ra.Get_Prediction()

        return render_template('result.html',result = result)


if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 1111)

