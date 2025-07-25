from datetime import datetime
from utils.age_utils import calculate_age, is_birthday, calculate_days_until_birthday
from utils.photo_utils import select_photo
from utils.slideshow import show_slideshow

def get_birth_date():
    while True:
        try:
            data_str =  input("Enter your date of birth |(DD/MM/YYYY): ")
            return datetime.strptime(data_str, "%d/%m/%y")
        except ValueError:
            print("❌ Invalid format. Try again.")