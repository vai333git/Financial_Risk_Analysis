# Here we will write all the functions (constructor, loading files, prediction etc)
import json 
import pickle
import config
# Let's create class for Risk_Assessment
class Risk_Assessment():
    # Now we will create the constructor

    def __init__(self,loan_amnt,term,emp_length,home_ownership,annual_inc,verification_status,pymnt_plan,purpose,zip_code,total_acc,total_pymnt,recoveries,last_pymnt_d,last_pymnt_amnt,last_credit_pull_d,application_type,debt_settlement_flag,last_fico_range_high,last_fico_range_low,tot_coll_amt,tot_cur_bal):
        self.loan_amnt = loan_amnt
        self.term = term
        self.emp_length = emp_length
        self.home_ownership = home_ownership
        self.annual_inc = annual_inc
        self.verification_status = verification_status
        self.pymnt_plan = pymnt_plan
        self.purpose = purpose
        self.zip_code = zip_code
        self.total_acc = total_acc
        self.total_pymnt = total_pymnt
        self.recoveries = recoveries
        self.last_pymnt_d = last_pymnt_d
        self.last_pymnt_amnt = last_pymnt_amnt
        self.last_credit_pull_d = last_credit_pull_d
        self.application_type = application_type
        self.debt_settlement_flag = debt_settlement_flag
        self.last_fico_range_high = last_fico_range_high
        self.last_fico_range_low = last_fico_range_low
        self.tot_coll_amt = tot_coll_amt
        self.tot_cur_bal = tot_cur_bal
        
    def Load_Models(self):
        with open(config.MODEL_FILE_PATH,'rb') as fp:
            self.model = pickle.load(fp)
        with open(config.JSON_FILE_PATH, 'r') as fj:
            self.json = json.load(fj)

    def Get_Prediction(self):
        self.Load_Models()

        # Create test array
        test_list_cat = ['' for i in range(len(self.json['columns']))]
        
        # Numerical
        test_list_cat[self.json['columns'].index("loan_amnt")] =    self.loan_amnt 
        test_list_cat[self.json['columns'].index("emp_length")] =  self.emp_length 
        test_list_cat[self.json['columns'].index("annual_inc")] =  self.annual_inc 
        test_list_cat[self.json['columns'].index("total_acc")] =  self.total_acc 
        test_list_cat[self.json['columns'].index("total_pymnt")] =  self.total_pymnt 
        test_list_cat[self.json['columns'].index("recoveries")] =    self.recoveries 
        test_list_cat[self.json['columns'].index("last_pymnt_amnt")] =    self.last_pymnt_amnt 
        test_list_cat[self.json['columns'].index("last_fico_range_high")] =    self.last_fico_range_high 
        test_list_cat[self.json['columns'].index("last_fico_range_low")] =    self.last_fico_range_low 
        test_list_cat[self.json['columns'].index("tot_coll_amt")] =    self.tot_coll_amt 
        test_list_cat[self.json['columns'].index("tot_cur_bal")] =    self.tot_cur_bal 

        # Categorical
        test_list_cat[self.json['columns'].index("term")] =    self.term
        test_list_cat[self.json['columns'].index("home_ownership")] =    self.home_ownership
        test_list_cat[self.json['columns'].index("verification_status")] =    self.verification_status 
        test_list_cat[self.json['columns'].index("pymnt_plan")] =    self.pymnt_plan 
        test_list_cat[self.json['columns'].index("purpose")] =    self.purpose 
        test_list_cat[self.json['columns'].index("zip_code")] =    self.zip_code 
        test_list_cat[self.json['columns'].index("last_pymnt_d")] =    self.last_pymnt_d 
        test_list_cat[self.json['columns'].index("last_credit_pull_d")] =    self.last_credit_pull_d 
        test_list_cat[self.json['columns'].index("application_type")] =    self.application_type 
        test_list_cat[self.json['columns'].index("debt_settlement_flag")] =    self.debt_settlement_flag 

        result =  str(self.model.predict(test_list_cat))
        return self.json['target'][result]
