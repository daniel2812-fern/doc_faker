from docxtpl import DocxTemplate
import pandas as pd
import os 
import sys
import datetime
import random

src = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(1, src)
from src.label import kie_labelling,save_label
from src.dir import template_list


def random_gender():
    """Return a random gender string in Chinese."""
    return random.choice(["男", "女"])
def random_date(start, end):
    """Return a random date between start and end."""
    return start + datetime.timedelta(days=random.randint(0, (end - start).days))
def adjust_year(date_obj, years_to_subtract):
    """Subtract a certain number of years from a date, handling day out of range for month."""
    try:
        return date_obj.replace(year = date_obj.year - years_to_subtract)
    except ValueError:  # If day is out of range for month
        # Subtract days until we get a valid date. This usually corrects for Feb 29th leap year issues.
        return adjust_year(date_obj - datetime.timedelta(days=1), years_to_subtract)


def random_number_string(length=5):
    """Return a random string of numbers with a specified length."""
    return ''.join([str(random.randint(0, 9)) for _ in range(length)])


df = pd.read_excel("dataset/medicalfakedata.xlsx")
fake_personale_df = pd.read_csv("dataset/fake_personal_information.csv")

for template in  template_list:
    doc = DocxTemplate(os.path.abspath("templates/"+template))    
    for index, row in df.iterrows():
        random_rows = fake_personale_df.sample(n=3)
        patient = random_rows.iloc[0]
        doctor = random_rows.iloc[1]
        advisor = random_rows.iloc[2] 
        template_name = template.split('.')[0]
        label_dir = docx_dir ="output/"+template_name+"/label/"
        docx_dir ="output/"+template_name+"/docx/"
        
        if not os.path.exists(label_dir):
            os.makedirs(label_dir)
        if not os.path.exists(docx_dir):
            os.makedirs(docx_dir)

        context = {
            'patient_name': patient['name'],
            'patient_sex': random_gender(),
            'patient_address': patient['address'],
            'patient_nation': '臺灣',
            'patient_id': patient['id'],
            'patient_birth': adjust_year(random_date(datetime.date(1945, 1, 1), datetime.date(2000, 12, 30)), 1941).strftime('%Y年%m月%d日'),
            'medical_history': random_number_string(6),
            'date_exam': adjust_year(random_date(datetime.date(2001, 1, 1), datetime.date(2023, 12, 30)), 1941).strftime('%Y年%m月%d日'),
            'hospital_name' : row['機構名稱'],
            'hospital_address' : row['機構地址'],
            'diagnosis':row['適應症'],
            'doctor_comment':row['醫師囑言'],
            'department':row['科別'],
            'doctor_name':doctor['name'],
            'advisor_name':advisor['name']
        }
        kie = kie_labelling(rowdata=context,templatename=template_name)
        save_label(kie,label_dir+ str(index)+".json" )
        doc.render(context)
        doc.save(docx_dir+str(index)+".docx" )
