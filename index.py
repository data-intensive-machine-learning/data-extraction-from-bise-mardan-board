from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import json

# Give the name of the JSON file
filename = "Result2ndYear2023.json"
data = []

with open("roll.txt", "r") as roll_file:
    roll = roll_file.read().splitlines()

for roll_number in roll:

    try:
        # Add headless option when creating the WebDriver instance
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)


        # Link to the website
        driver.get("https://result.bisemdn.edu.pk/")

        # Add leading zeros to the roll number
        roll_number = roll_number.zfill(6)

        # ROLL NO INPUT FIELD
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="RnoSearch"]/input'))
        )
        input_field.clear()
        input_field.send_keys(roll_number)

        # CLICKING CHECK RESULT BUTTON
        view_result_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="hssc12Form"]/button'))
        )
        view_result_button.click()

        # ROLL NO
        ROLL = WebDriverWait(driver, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="info-table"]/tbody/tr[1]/td/h2'))
        ).text

        # CLASS
        CLASS = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="info-table"]/tbody/tr[2]/td[1]'))
        ).text

        # GROUP 
        GROUP = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="info-table"]/tbody/tr[2]/td[2]'))
        ).text

        # NAME
        NAME = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="info-table"]/tbody/tr[3]/td[1]'))
        ).text

        # FATHER NAME
        FATHERNAME = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="info-table"]/tbody/tr[3]/td[2]'))
        ).text

        # MARKS
        MARKS = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="info-table"]/tbody/tr[4]/td[1]'))
        ).text

        # MARKS
        REMARKS = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="info-table"]/tbody/tr[4]/td[2]'))
        ).text

        if MARKS == "0":
            error = {
             "E-DMC NOT AVAILABLE FOR ROLL NUMBER ": ROLL   
            }

            data.append(error)
            continue

        SUBJECT1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[3]/td[1]'))
        ).text

        SUBJECT2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[4]/td[1]'))
        ).text

        SUBJECT3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[5]/td[1]'))
        ).text

        SUBJECT4 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[6]/td[1]'))
        ).text

        SUBJECT5 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[7]/td[1]'))
        ).text

        SUBJECT6 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[8]/td[1]'))
        ).text

        SUBJECT7 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[9]/td[1]'))
        ).text

        SUBJECT8 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[10]/td[1]'))
        ).text

        SUBJECT9 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[11]/td[1]'))
        ).text

        SUBJECT10 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[12]/td[1]'))
        ).text

        SUBJECT11 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[13]/td[1]'))
        ).text

        SUBJECT12 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[14]/td[1]'))
        ).text

        # Subject wise marks
        MARKS1 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[3]/td[4]'))
        ).text

        MARKS2 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[4]/td[4]'))
        ).text

        MARKS3 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[5]/td[4]'))
        ).text

        MARKS4 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[6]/td[4]'))
        ).text

        MARKS5 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[7]/td[4]'))
        ).text

        MARKS6 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[8]/td[4]'))
        ).text

        MARKS7 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[9]/td[4]'))
        ).text

        MARKS8 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[10]/td[4]'))
        ).text

        MARKS9 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[11]/td[4]'))
        ).text

        MARKS10 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[12]/td[4]'))
        ).text

        MARKS11 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[13]/td[4]'))
        ).text

        MARKS12 = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="marks-table"]/tbody/tr[14]/td[4]'))
        ).text

        # STORE DATA IN DICTIONARY
        result_data = {
            "ROLL #": ROLL, 
            "CLASS": CLASS, 
            "GROUP": GROUP, 
            "NAME": NAME, 
            "FATHER NAME": FATHERNAME, 
            "MARKS": MARKS, 
            "REMARKS": REMARKS,
            SUBJECT1: MARKS1,
            SUBJECT2: MARKS2,
            SUBJECT3: MARKS3,
            SUBJECT4: MARKS4, 
            SUBJECT5: MARKS5,
            SUBJECT6: MARKS6,
            SUBJECT7: MARKS7,
            SUBJECT8: MARKS8,
            SUBJECT9: MARKS9,
            SUBJECT10: MARKS10,
            SUBJECT11: MARKS11,
            SUBJECT12: MARKS12}

        # APPEND DATA TO THE LIST
        data.append(result_data)

        # WRITE DATA
        with open(filename, 'w') as json_file:
          json.dump(data, json_file,  indent=0) 


        driver.quit()

    except NoSuchElementException as exception:
        error = {
             "DATA NOT AVAILABLE FOR ROLL NUMBER ": ROLL   
            }

        data.append(error)
        continue


    
print("Data has been written to", filename)
