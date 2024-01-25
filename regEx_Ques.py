1. Application of Regular Expression: Web Scraping and Data Collection (URL)
import re
import requests

url = 'https://accounts.google.com/v3/signin/identifier?authuser=0&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ec=GALAFw&hl=en-GB&service=mail&flowName=GlifWebSignIn&flowEntry=AddSession&theme=glif'

response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extracting URLs using regular expression
    html_content = response.text
    url_pattern = re.compile(r'href="(https?://.*?)"')
    urls = url_pattern.findall(html_content)

    # Displaying the extracted URLs
    for extracted_url in urls:
        print(extracted_url)
else:
    print(f"Failed to retrieve the webpage. Status Code: {response.status_code}")


3. Entity Recognition: Pattern Detection for Iris, Emails, Text, Date-Time Manipulation
a) Pattern Detection in Iris Data:
    import re

iris_data = "SepalLength: 5.1, SepalWidth: 3.5, PetalLength: 1.4, PetalWidth: 0.2"

# Pattern detection for Iris data
pattern_iris = re.compile(r'SepalLength: (\d+\.\d+), SepalWidth: (\d+\.\d+), PetalLength: (\d+\.\d+), PetalWidth: (\d+\.\d+)')
match_iris = pattern_iris.search(iris_data)

if match_iris:
    print("Iris Data Detected:")
    print("Sepal Length:", match_iris.group(1))
    print("Sepal Width:", match_iris.group(2))
    print("Petal Length:", match_iris.group(3))
    print("Petal Width:", match_iris.group(4))
else:
    print("No match found in Iris data.")

b) Email Pattern Detection:
    import re

text_with_email = "Contact us at support@example.com for assistance."

# Email pattern detection
pattern_email = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
match_email = pattern_email.search(text_with_email)

if match_email:
    print("Email Detected:", match_email.group())
else:
    print("No email found in the text.")


c) Text Detection:
    import re

text_with_pattern = "Pattern detected in this text."

# Pattern detection in text
pattern_text = re.compile(r'Pattern')
match_text = pattern_text.search(text_with_pattern)

if match_text:
    print("Text Detected:", match_text.group())
else:
    print("Pattern not found in the text.")


d)) Date and Time Manipulation:
    import re

date_time_text = "Date: 2022-01-01 Time: 12:30 PM"

# Date and time manipulation
pattern_date_time = re.compile(r'Date: (\d{4}-\d{2}-\d{2}) Time: (\d{2}:\d{2} [APMapm]+)')
match_date_time = pattern_date_time.search(date_time_text)

if match_date_time:
    print("Date Detected:", match_date_time.group(1))
    print("Time Detected:", match_date_time.group(2))
else:
    print("No date and time found in the text.")

