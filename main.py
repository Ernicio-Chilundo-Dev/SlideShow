from datetime import datetime
from utils.age_utils import calculate_age, is_birthday, calculate_days_until_birthday
from utils.photo_utils import select_photo
from utils.slideshow import show_slideshow

def get_birth_date():
    while True:
        try:
            data_str = input("Enter your date of birth (DD/MM/AAAA): ")
            return datetime.strptime(data_str, "%d/%m/%Y")
        except ValueError:
            print("❌ Invalid format. Try again.")

def main():
    birth_date = get_birth_date()
    age = calculate_age(birth_date)

    if is_birthday(birth_date):
        print("🎉 Congratulations! Today is your special day!")
        photos = select_photo(age)
    else:
        days = calculate_days_until_birthday(birth_date)
        print(f"⏳ There are {days} days left until your birthday.")
        photos = select_photo(age)

    print("✨ Get ready for the slideshow... (Tip: the number of photos = the person's age 😉)")
    show_slideshow(photos)

if __name__ == "__main__":
    main()
