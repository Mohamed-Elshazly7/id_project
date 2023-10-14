users = {
    "conan": {"password": "mido1234",
              "national_id": "30307031202798",
              "name": "Conan",
              "gender": "Male",
              "birth_date": "03/07/03",
              "city": "Cairo",
              "serial_number": "123456"},
}


def login():
    username = input("الرجاء إدخال اسم المستخدم: ")
    password = input("الرجاء إدخال كلمة المرور: ")

    if username in users and users[username]["password"] == password:
        print("تم تسجيل الدخول بنجاح!")
        display_user_info(users[username]["national_id"])
    else:
        print("المستخدم غير موجود أو كلمة المرور غير صحيحة.")


def signup():
    new_username = input("الرجاء إدخال اسم المستخدم الجديد: ")
    new_password = input("الرجاء إدخال كلمة المرور الجديدة: ")
    new_national_id = input("الرجاء إدخال الرقم القومي الجديد: ")

    # حفظ معلومات المستخدم الجديد في قاعدة البيانات
    users[new_username] = {
        "password": new_password,
        "national_id": new_national_id,
    }
    print("تمت إضافة المستخدم بنجاح!")


def extract_info_from_national_id(national_id):
    # الرقم الأول: قرن الميلاد
    century = int(national_id[0])
    # الأرقام الست التالية: تاريخ الميلاد
    birth_date = national_id[1:3]+"/"+national_id[3:5]+"/"+national_id[5:7]
    # الرقمان التاليان: رقما محافظة الميلاد
    governorate_code = national_id[7:9]
    # الأرقام الأربعة التالية: أرقام لرقم مسلسل
    serial_number = national_id[9:13]
    # الرقم الأخير: رقم اختياري للتأكيد على صحة الرقم القومي
    confirmation_digit = national_id[-1]
    # الرقم الثالث عشر: إذا كان زوجياً فالمستخدم ذكر وإذا كان فردياً فالمستخدم أنثى
    gender = "انثى" if int(national_id[-3]) % 2 == 0 else "ذكر"
    # كود المحافظة
    governorates = {
        "01": "القاهرة", "02": "الإسكندرية", "03": "بورسعيد", "04": "السويس", "11": "دمياط",
        "12": "الدقهلية", "13": "الشرقية", "14": "القليوبية", "15": "كفر الشيخ", "16": "الغربية",
        "17": "المنوفية", "18": "البحيرة", "19": "الإسماعيلية", "21": "الجيزة", "22": "بني سويف",
        "23": "الفيوم", "24": "المنيا", "25": "أسيوط", "26": "سوهاج", "27": "قنا", "28": "أسوان",
        "29": "الأقصر", "31": "البحر الأحمر", "32": "الوادي الجديد", "33": "مطروح", "34": "شمال سيناء",
        "35": "جنوب سيناء", "88": "خارج الجمهورية"
    }
    governorate = governorates.get(governorate_code, "غير معروفة")

    return century, birth_date, governorate, serial_number, gender, confirmation_digit


def display_user_info(national_id):
    century, birth_date, governorate, serial_number, gender, confirmation_digit = extract_info_from_national_id(national_id)
    print("الرقم القومي: ", national_id)
    print("قرن الميلاد: ", century)
    print("تاريخ الميلاد: ", birth_date)
    print("محافظة الميلاد: ", governorate)
    print("رقم المسلسل: ", serial_number)
    print("الجنس: ", gender)
    print("رقم التأكيد: ", confirmation_digit)


def main():
    print("مرحبًا بك!")
    choice = input("log in or sign up : ").lower()

    if choice == "log in":
        login()
    elif choice == "sign up":
        signup()
    else:
        print("اختيار غير صحيح.")


if __name__ == "__main__":
    main()
