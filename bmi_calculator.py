import json
import csv
import traceback
import pandas as pd

class BodyMassIndex:
    bmi_categoty = { 
                    'UW':'Underweight',
                    'NW': 'Normal Weight',
                    'OW': 'Over Weight',
                    'MO': 'Moderately obese',
                    'SO': 'Severly obese',
                    'VSO': 'Very Severly obese'
        }

    health_risk = {
                    'MR':'Malnutrition Risk',
                    'LR': 'Low Risk',
                    'ER': 'Enhanced Risk',
                    'MRS': 'Medium Risk',
                    'HR': 'High Risk',
                    'VHR': 'Very High Risk'
        }
    

def read_input():
    with open('json_input.json') as f:
        records = json.load(f,  parse_int=str)
    return records


def calculate_bmi(data):
    BMI_categoty = None
    Health_risk = None
    BMI_range = None
    
    x = int(data['HeightCm'])
    y = int(data['WeightKg'])
    bmi = y/((x/100)**2)
    
    if bmi <= 18.4 :
        BMI_categoty = BodyMassIndex.bmi_categoty.get('UW')
        BMI_range = bmi
        Health_risk = BodyMassIndex.health_risk.get('MR')
        
    elif bmi >= 18.5 and bmi <= 24.9:
        BMI_categoty = BodyMassIndex.bmi_categoty.get('NW')
        BMI_range = bmi
        Health_risk = BodyMassIndex.health_risk.get('LR')
        
    elif bmi >= 25 and bmi <= 29.9:
        BMI_categoty = BodyMassIndex.bmi_categoty.get("OW")
        BMI_range = bmi
        Health_risk = BodyMassIndex.health_risk.get('ER')
        
    elif bmi >= 30 and bmi <= 34.9:
        BMI_categoty = BodyMassIndex.bmi_categoty.get("MO")
        BMI_range = bmi
        Health_risk = BodyMassIndex.health_risk.get('MRS')
        
    elif bmi >= 35 and bmi <= 39.9:
        BMI_categoty = BodyMassIndex.bmi_categoty.get("SO")
        BMI_range = bmi
        Health_risk = BodyMassIndex.health_risk.get('HR')
        
    elif bmi > 40:
        BMI_categoty = BodyMassIndex.bmi_categoty.get("VSO")
        BMI_range = bmi
        Health_risk = BodyMassIndex.health_risk.get('VHR')
        
    bmi_list ={
        'BMI_categoty': BMI_categoty,
        'BMI_range': BMI_range,
        'Health_risk': Health_risk
        }
    return bmi_list

def is_valid_record(record):
    if record['Gender'].isalpha() == True and record['HeightCm'].isnumeric() == True and record['WeightKg'].isnumeric() == True:
        return True
    else:
        return False


def processing_for_bmi_calculation(data):
    record_count = 0
    valid_records = []
    invalid_records = []
  
    for item in data:
        if is_valid_record(item):
            bmi = calculate_bmi(item)
            bmi_complete = { **item, **bmi }
            valid_records.append(bmi_complete)
        else:
            invalid_records.append(item)
        record_count +=1
        
        
    print('Failed to calculate BMI for following records due to invalid data: \n', pd.DataFrame(invalid_records).to_string(index=False))   
    print('Valid BMI calculator result: \n', pd.DataFrame(valid_records).to_string(index=False)) 
    return valid_records


def get_over_weight_people(data):
    ow_category = ['Over Weight', 'Moderately obese', 'Severly obese', 'Very Severly obese']
    ow_data = [d for d in data if d['BMI_categoty'] in ow_category]
    print('List of Overweight people : \n', pd.DataFrame(ow_data).to_string(index=False)) 
    return ow_data



def produce_result(data, file_name):
    keys = data[0].keys()
    with open(file_name, 'w',newline='') as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
    print("BMI calculator generated result successfully")


if __name__ == '__main__':
    try:
        source_data = read_input()
        
        bmi_data = processing_for_bmi_calculation(source_data)
        produce_result(bmi_data, 'bmi_calculator_result_all.csv')
        
        ow_filtered = get_over_weight_people(bmi_data)
        produce_result(ow_filtered, 'bmi_calculator_result_overweight.csv')
    except:
        print("Error occured while running the BMI calculator process")
        traceback.print_exc()
