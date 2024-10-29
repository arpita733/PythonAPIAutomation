### Tech Stack

-Python 3.12
-Requests - HTTP Requests
-PyTest - Testing Framework
-Reporting - Allure Report, PyTest HTML
-Test Data - CSV, Excel, JSON, Faker
-Advance API Testcase - jsonschema
-Parallel Execution - x distribute (xdist)
-How to Install Packages

'''
pip install requests pytest pytest-html faker allure-pytest jsonschema

pip install requests pytest pytest-html allure-pytest faker jsonschema pytest-xdist python-dotenv pandas

pip list

pip freeze > requirements.txt

pytest -s src/tests/test_sample.py --alluredir=allure_result

allure serve allure_result 


'''

How to run your Testcase Parallel

'''
pip install pytest-xdist
'''

How to run the Basic Test with Allure report

'''
pytest tests/tests/crud/test_create_booking.py --alluredir=allure_result -s
'''
