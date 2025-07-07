



from odoo.tests.common import TransactionCase

class TestStudentRecord(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Create a common record for all test methods in the class
        cls.student = cls.env['student.student'].create({
            'name': 'John Doe',
            'age': 23  
        })

    def test_field_values(self):
        # Test the values of fields
        self.assertEqual(self.student.name,'John Doe', "Name field value is incorrect")
        self.assertEqual(self.student.age, 23, "Age field value is incorrect")

    def test_record_values(self):
        
        self.assertTrue(self.student, {
            'name': 'John Doe',
            'age': 23,
            
        })

    def test_some_actions(self):
        # add a record in a model.
        record = self.env['student.student'].create({'name': 'John Doe', 'age':12})
        
        # Check if the field and match the expected result
        self.assertNotEqual(record.name, 'John ')
        print('============================ Your test was successful! ====================================')



    @classmethod
    def tearDownClass(cls):
        # Clean up any resources if needed
        super().tearDownClass()
