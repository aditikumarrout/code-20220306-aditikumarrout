import unittest
import bmi_calculator

class BmiTest(unittest.TestCase):
    
    def test_for_valid_source_record(self):
        test_data = {"Gender": "Male", "HeightCm": "171", "WeightKg": "150" }
        self.assertTrue(bmi_calculator.is_valid_record(test_data))
        
    
    def test_for_invalid_source_record(self):
        test_data = {"Gender": "Male", "HeightCm": "171", "WeightKg": "unknown" }
        self.assertFalse(bmi_calculator.is_valid_record(test_data))
        
    
    def test_for_bmi_calculation(self):
        test_data = {"Gender": "Male", "HeightCm": "161", "WeightKg": "85" }
        expected_result = {'BMI_categoty': 'Moderately obese', 'BMI_range': 32.79194475521777, 'Health_risk': 'Medium Risk'}
        self.assertEqual(bmi_calculator.calculate_bmi(test_data), expected_result)
        
    
    def test_for_get_over_weight_people(self):
        test_data = [
                {'Gender': 'Male', 'HeightCm': '180', 'WeightKg': '77', 'BMI_categoty': 'Normal Weight', 'BMI_range': 23.76543209876543, 'Health_risk': 'Low Risk'},
                {'Gender': 'Female', 'HeightCm': '167', 'WeightKg': '250', 'BMI_categoty': 'Very Severly obese', 'BMI_range': 89.64107712718277, 'Health_risk': 'Very High Risk'}
            ]
        expected_result = [
                {'Gender': 'Female', 'HeightCm': '167', 'WeightKg': '250', 'BMI_categoty': 'Very Severly obese', 'BMI_range': 89.64107712718277, 'Health_risk': 'Very High Risk'}
            ]       
        self.assertEqual(bmi_calculator.get_over_weight_people(test_data), expected_result)
        
    
    def test_for_exception(self):
        test_data = None
        with self.assertRaises(Exception):
            bmi_calculator.processing_for_bmi_calculation(test_data)
            
        
if __name__ == '__main__':
    unittest.main()