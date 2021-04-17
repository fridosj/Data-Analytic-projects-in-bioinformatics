#Assignment name:assignment 1
#Hours spent:29 hours
#Date:28/01/2021
#Reference :mysql documentation
#Author name: Fridolin Steffe Mijo S J
#outcome: learnt how to work with mysql module in python

import mysql.connector
import csv
import json


# login to database
mydb = mysql.connector.connect(host="127.0.0.1",user='root',password='',database="patient_data")
print("connected")
mycursor = mydb.cursor()
s="Drop Table if exists patient_info"
mycursor.execute(s)
# command for insertion
sql = "CREATE TABLE IF NOT EXISTS patient_info(Diagnosis_Age VARCHAR(255),Sex VARCHAR(255),Ethnicity_Category VARCHAR(255),Histology VARCHAR(255),Adjuvant_Treatment VARCHAR(255),ECOG_Performance_Status VARCHAR(255),Smoking_History VARCHAR(255),Person_Cigarette_Smoking_History_Pack_Year_Value VARCHAR(255),Relapse_Free_Status VARCHAR(255),Relapse_Free_Status_Months VARCHAR(255),Ubiquitous_Assay_Panel VARCHAR(255),Percent_Necrosis VARCHAR(255),Tumor_Volume_cm3 VARCHAR(255),Tumor_Stage VARCHAR(255),Positron_emission_tomography_tumor_background_ratio VARCHAR(255),cfDNA_Input_ng VARCHAR(255),Lymph_Node_Involvement VARCHAR(255),Ki67_Percentage VARCHAR(255),CT_Slice_Spacing VARCHAR(255),patient_id VARCHAR(255)); "

mycursor.execute(sql)
print("table created")

print('done')
# loop through CSV each line and get
with open("patientdata.csv", "r") as csv_data:
   next(csv_data)
   for row in csv_data:
      r = row.strip().split(",")
      mycursor.execute("""INSERT INTO patient_info(Diagnosis_Age,Sex,Ethnicity_Category,Histology,Adjuvant_Treatment,ECOG_Performance_Status,Smoking_History,Person_Cigarette_Smoking_History_Pack_Year_Value,Relapse_Free_Status,Relapse_Free_Status_Months,Ubiquitous_Assay_Panel,Percent_Necrosis,Tumor_Volume_cm3,Tumor_Stage,Positron_emission_tomography_tumor_background_ratio,cfDNA_Input_ng,Lymph_Node_Involvement,Ki67_Percentage,CT_Slice_Spacing,patient_id) VALUES(%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s)""", (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], r[8], r[9], r[10], r[11], r[12],r[13],r[14],r[15],r[16],r[17],r[18],r[19]))

mydb.commit()
mycursor.close()


