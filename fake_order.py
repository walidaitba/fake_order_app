from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains
import time
import random
import sys
import urllib.parse
import requests

def get_random_name():
    names = names = [
    "فاتحة", "Laila", "صلاح الدين", "بنرحو مريم", "شيماء", "سفيان", "Abdelkrim", "Said jawad", "مهاجر مصطفى", 
    "عادل", "محمد بنعمر", "Yassir", "سعيدة دهين", "Adil", "Ilham", "moufid", "Titrit bennani", "لطيفة اليماني", 
    "الوردي صديق", "ادريسية الجوهري", "كوثر", "ايوب جمعة", "صفية", "Souad", "Kaoutar benayad", "خديجة  الحرش", 
    "Ghizlane", "Amal", "Farida", "Amina", "Rachid", "Samra Mohamed", "ملولة عبد العزيز", "Nahid", "سلوى", 
    "Fatima ezzahra", "كوثر", "فاطمة", "مهداوي عبدالرزاق", "امغار  حنان", "ayoub", "هند", "EsSAHRAOUI", 
    "Zineb boulanouar", "Archanm", "Boulaarouf nadia", "علي عروب", "ayoub", "ayoub", "محمد", "Soufiane Ezziati", 
    "حفيط", "هدى", "حنان", "Hassan", "Manssour belkhair", "لمياء أمزالي", "هند بنعزة", "Rachid", "توفيق ازنبيل", 
    "المعتصم بالله فؤاد", "محمد مدوش", "احمد الدعنوني", "Wissal", "Manssour belkhair", "Ferdawss", "Kawtar labib", 
    "ايوب", "Fatima Zahra", "خديجة بوهوش", "Bouchra", "Douaa jaadane", "عمر اسهل", "عبد العزيز", "حميد", "Mustapha", 
    "said Rahmatoullah", "Zaineb", "عبدالله", "محمد حسان", "Raoui otmane", "احمدشي عبدالوهاب", "عبد المجيد الودغيري", 
    "Hicham", "التاجي", "محمد", "صدقان سورية", "زينب بلكوري", "ياسين", "سعاد", "ياسين", "جمال  أبورحو", "youssef", 
    "Anas", "Otman ait oualla", "Mahdi", "الحسين غورا", "Zaimi mustapha", "حسن", "karima", "Meryem NACIRI", "Ahmed", 
    "aymane zr", "Brahim", "محمد", "Marwan achari", "أسماء هاني", "yassine", "issame", "Kabiri", "Fatima", "hassan", 
    "Aymen zouita", "ali", "laila", "هاجر أبونصر", "مستعين امينة", "mariam", "ABID FATIHA", "اسماعيل الرحيوي", 
    "Rajaa Elhakkaoui", "خاليد", "Mina", "حسناء لبي", "Adil", "Dilal abdrahman", "ADIL", "Reda", 
    "Chanel Emmaüs Jaurès", "Blfkih mohamed", "ركراكي دريس", "Hamza", "Hailoufiy khalid", "Soufiane", "احمد", "Mohamed", 
    "Zakariya boskom", "ياسين العلمي", "محمد الزموري", "Nour", "Mehdi", "أشرف", "Mehdi finani", "Fatima ait elmouden", 
    "mohammed", "amine", "Btissame lwazania", "ياسين", "نجاة الشكلاطي", "Hicham  le brabouch", "محسين", "Najia", 
    "younes", "Jalal", "Ibtissam foukhar", "فاطمة", "hicham", "محمد أمزي", "مريم", "houda", "المختار", "Begdouri meriem", 
    "soufiane rolam", "ابتسام", "ياسين", "najat", "ياسين وحداش", "Simouhmad", "Souilah mohsine", "Kawtar", 
    "Siham mehdaoui", "محمد القماري", "Safaa fadali", "رشيدة والطالب", "Hamdane", "Nour", "Hamza", "Omar madouch", 
    "soufian", "محمد القماري", "فاطمة", "ياسين", "مصطفى معوش", "مصطفى", "سعيدة", "Hassan Semlali", "Zakaria hajji", 
    "Mohamed elouahami", "سكينة", "عمر", "إلياس خالد", "Mourad", "Elhoussine nour", "عبدالهادي", "اسيد", "فاطمة مجتهد", 
    "Khatri chouiar", "نعيمة", "Latifa tahmoune", "Mery", "Turia", "smail makroum", "مصطفى", "Ieieje", "حمزة العبدي", 
    "Maarouf hanane", "هلالي ادريس", "Jamal", "Bouchra", "Mohammed", "Simo", "عزالعرب", "Rachid Oukhatou", "محمد", 
    "Ismail", "Khalid", "mstapha oujaddi", "Hafid", "FOUAD", "Ans", "Soufiane", "Aicha nachit", "Ayoub", "مريم رافية", 
    "احموا", "Khadija", "عبدالإله ايت صالح", "Mouhcine bejhih", "سميه", "فهد", "Mustapha", "Mohammed lazhar", 
    "فاطمة الزهراء", "Fouad founounou", "CÉCILE godoua", "هشام", "فدوى", "عبدالله ادريسي", "Mohamed", "Younes marzouki", 
    "احمد", "محمد", "Nour", "Amine", "خالد", "سي محمد", "براهيم", "مريم لمتوح", "الحبيب", "Fettah", "Bichi", "جواد", 
    "Mbarek Rahi", "Chaimae", "Bouchra", "Hossine", "Karim", "btissam khlifi", "خديجه", "hamza", "ليلى", "Amine", 
    "عبدالهادي بوناصر", "يونس", "الصريدي", "Yosaf", "Sahabi khadijq", "مروان", "عزيزة فرزي", "عمراوي نورة", 
    "فاتحة وزين", "hnane", "حليمة الشافعي", "نبيل", "عبد المجيد", "Naima", "Kabbaj fatima", "Souad", "انتصار", 
    "بوراس لمياء", "Semlali Hassan", "مينة ايت عبدالله", "Aicha", "نسيمة قديدر", "بديعة", "فاطيمة مجدي", "Atika", 
    "اغموا", "Naima", "Mohamd", "Kawtar", "جميلة المعياطي", "اشبابي زكية", "Rabiaa bassou", "أمينة", "كوثر لصمك", 
    "عبدالنبي أمنشار", "Chacha Youssef", "Imane", "Lachheb loubna", "kabira", "سناء", "نورة", "اضرضور", "Slimani mustapha", 
    "حكيمة", "Tarfa", "نعيمة زدة", "فاتي دانا", "Kamal", "Hanan", "Fadila assiane", "Rahma Zaidoun", "Abdellatif", 
    "Asmae", "فاطمة الزهراء", "karim", "Mustapha", "Uness berrada", "Naima azahoum", "Mohamed", "عمر", "Adnane", "عبدالله", 
    "Achraf hamdan", "Mohamed Afaiz", "Sourair mokhtar", "سعاد  عبريتي", "سعاد", "Mustapha", "Hassan", "Labker", "كريم سميرة", 
    "عبدالله", "Adil sslami", "سعيدة", "Salma habbari", "سارة لوزا", "فاطمةلقصير", "جميلة بوشاطر", "خليصة", "رقية", "بشرى", 
    "فاتحة", "سعاد السعودي", "Fatiha chnika", "سكينة ايت مالك", "نزهة برطال", "مصطفى", "الحسين", "حميد", "Hassane", "محسن", 
    "Ayoub oulghazi", "نور الدين", "سناء", "Samih Zakaria", "Ahmed attaoui", "Fatima", "CHATT OUAFAE", "Belhaj", "Hamid", 
    "ABDELJALIL ELFARISSI", "عمر", "Omar idhaisoune", "Nabil maimouni", "Gontitti abdlkarim", "مطهر الكبير", "Mybrahim AIT MOUSSA", 
    "جميلة", "عبدالعالي شرفي", "دريس", "جمال", "أحمد بوجود", "طارق", "samir ouchen", "Hassan", "Mounaimlahmidi", "Zineb", 
    "عبد الهادي بن ريحان", "fahd", "nourdin", "غيتة بلمين", "Mounir Fakri", "مونية", "Meriem", "Abdelhadi", "Pearl", 
    "Bouchra akhrikhar", "Hamid", "fatima", "James faye", "سيف نادية", "Elyacoubi khatima", "Latifa", "Hassan", "نعيمة", 
    "عبدالوهاب", "mahmoud ait", "Rabie nezha", "Meryem", "Belghazi", "Belarbi", "aicha", "عادل ضيغم", "التوامي محمد", 
    "Mohamed", "يوسف دعلبي", "Ali", "محمد", "Bouchaib", "hanin", "لبنى", "Mohamed BAIH", "Achnine", "سناء", "Kenza", 
    "سناء", "Redouane", "محمد الشوبي", "سعيدة", "رضا القلعي", "Haj", "ابركان", "amine", "Zenati Abdelhakim", "عبد العزيز بنعلي", 
    "ناصر خالد", "Mohamed"]
    return random.choice(names)

def get_random_phone():
    return f"060{random.randint(1000000, 9999999)}"

def get_random_city():
    cities = [
    "وزان", "Azmour", "محسوب على برشيد ولاكن قرب دار بوعز نواحي كازا", "المحمدية", "سطات", "الدارالبيضاء", 
    "Settat", "Khouribga", "ابن احمد", "الفقيه بن صالح", "بركان حدا كافور", "جديدة", "Casa", "مراكش المغرب", 
    "مديونه", "Marrakech", "Agadir", "Agadir", "البيضاء", "القنيطرة", "سلا", "Tange", "طاطا", "سلا", "Casablanca", 
    "Tetouan (Martil)", "القنيطرة", "9arya", "Kenitra", "Rabat", "Casablanca", "Choisir une ville  bouskoura", 
    "Salé", "اليوسفية", "Tanger", "القنيطرة", "Errachidia", "Tange", "مراكش", "بركان", "الناظ", "mohammedia", 
    "الرباط", "CASA BLANCA", "Marrakech", "Agdire", "Meknes", "فاس", "mohammedia", "mohammedia", "الدار البيضاء", 
    "Errahma dar bouazza casa blanca", "العيون الجنوب", "مراكش", "العيون", "Ouarzazate", "Tanger", "أكادير", "خريبكة", 
    "الرباط", "العراءش", "بوسكورة", "تنغير", "الجرف أرفود", "Fes", "طنجة", "Tanger", "Casa", "فاس", "Fes", "تارودانت", 
    "Berkane", "Casablanca", "ماسة", "مراكش", "Marrakich", "أكادير", "tanger", "Martil", "الدلبضياء", "مكناس", "Temara", 
    "ايت ملول", "إبن جرير", "Marrakech", "مراكش", "مراكش", "الدار البيضاء", "طنجة", "خريبكة", "سلا", "سلا الجديدة", 
    "tamaris casa", "marrakech", "Marrakech", "Bouznika", "Mohammedia", "Taza", "اكوراي", "الرباط", "casa", 
    "sala jadida", "Reggada tiznit", "casa", "Driwach", "اكادير", "Safrou", "البيضاء", "ifrane", "settat", "Errachidia", 
    "Agadir", "sidi ismail", "Casa blanca", "Ain aouda", "ain harrouda", "الدار البيضاء", "الدارالبيضاء", "goulmima", 
    "DAKHLA", "الأربعاء صخور الرحامنة", "Marrakech", "تطوان", "Safi", "وادزم", "الدار البيضاء", "Dakhla", "Nousseur", 
    "Rabat", "Oujda", "Casa", "أكادير", "Agadiir", "Caza", "El gara", "المدينة الصخيرات", "Bensliman", "Titwan", "طنجة", 
    "مكناس", "Fes", "Casablanca", "برشيد", "Kénitra", "الرباط", "tamsna", "fes", "Kenitra", "الالف", "طنجة", "الصويرة", 
    "الرباط", "جرف الملحة", "Casa", "casa", "فاس", "Beni mellal", "الدروة", "الدار لبيضاء", "قلعة السراغنة", "مكناس", 
    "marrakech", "تطوان", "Tanger", "حدا كميسريا ديال العوامة", "wazan", "وزان", "مراكش", "agadir", "خنيفرة", "مراكش", 
    "Fes", "Agadir", "Oujda", "الدارالبيضاء", "Laayoun", "Boudinar driouch", "31", "Agadir", "tanja", "Ouarzazate", 
    "haj kadour", "الدارالبيضاء", "رباط", "مراكش", "الناضور", "ورزازات", "القتيطرة", "AGADIR", "zagoura", "Oujda", 
    "كولميم", "Fes", "Beni mellal", "Imzouren", "meknas", "طنجة", "بني ملال", "Casablanca", "Guelmim", "البيضاء", 
    "Casablanca", "Khouribga", "Fnida9", "tanger", "الدارالبيضاء", "mohammedia", "تيزنيت", "Casa", "البيضاء", 
    "الدار البيضاء", "Berkane", "Settat", "Khenifra", "اكادير", "وجدة", "مكناس", "OUJDA", "Maknas", "dakhla", "فاس", 
    "AGADiR", "Sale", "Casablanca", "فاس", "Tanger", "درا البيضاء بحي لالامريم حظ مرشي كريو", "Marakch", "Tanger", 
    "سدي سليمان", "Tanger", "اكادير", "طنجة", "Rabat", "Tanger", "سيدي إفنى", "مكناس ويسلان", "Marrakech", "tanger", 
    "تمارة", "فاس", "Casa", "اسفي", "الدار البيضاء", "مرتيل", "Marrakech", "Sale", "أسفي", "اسفي", "Casablanca", 
    "البئر الجديد", "فاس", "Chefchaouen", "Temara", "Sale", "Chichaoua", "Tanger", "Berkane", "Cza", "Benasliman", 
    "meknes", "سلا", "souk sebt", "الرباط", "Tamasna", "أكادير", "طنجة", "تطوان", "Fes", "Caza mdina", "الدرالبيضاء", 
    "القنيطرة", "مدينة بركان", "المحمدية", "tanger", "فاس", "فاس", "سلا", "Caza", "Marrakech", "Fes", "زايدة", "الرباط", 
    "AGADIR", "سلا القريه", "Fes", "تاونات", "البيضاء", "مركش", "Meknes", "طنجة", "Caza", "9enitra", "Khouribga", 
    "قلعة السراغنة", "السعيدية", "Casablanca", "طنجة", "القنيطرة", "شفشاون", "Casa Blanca", "Nador", "Sale", "mknas", 
    "أسفي", "طنجة", "Marrakech", "Oujda", "طنجة", "Ait melloul", "مراكش", "الدار البيضاء", "Nafil", "Tanger", 
    "Marrakech", "Agadir", "Ville verte", "Meknes", "القنيطرة", "الدشريين", "Temara", "Sale", "Meknes", "Casa", "مراكش", 
    "Casablanca", "Kenitera", "tetouan", "Aourir agadir", "Casablanca", "هرهورة-تمارة", "فاس", "Agadir", "Casablanca", 
    "Khemisset", "القلعة السراغنة", "طنجة", "Casa", "فاس", "Béni Mellal", "الدار البيضاء", "سلا", "مراكش", "فاس", 
    "اكادير", "تزنيت", "بني ملال", "مكناس", "Kenitra", "تمازارت ايت ملول", "Bouznika", "كزا", "Casablanca", "tanger", 
    "Dakhla", "مراكش", "Midelt", "Casa", "Marrakech", "Casablaca"]
    return random.choice(cities)

def create_driver():
    tries = 0
    max_tries = 3
    while tries < max_tries:
        try:
            options = webdriver.ChromeOptions()
            # Basic options
            options.add_argument('--disable-gpu')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            
            # Suppress DevTools and other logging
            options.add_argument('--log-level=3')  # Fatal errors only
            options.add_argument('--silent')
            options.add_argument('--disable-logging')
            options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
            
            # Disable WebGL and related warnings
            options.add_argument('--disable-webgl')
            options.add_argument('--disable-software-rasterizer')
            
            # Other anti-detection options
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_experimental_option('useAutomationExtension', False)
            
            # Create driver with options
            driver = webdriver.Chrome(options=options)
            
            # Modify navigator properties
            driver.execute_cdp_cmd('Network.setUserAgentOverride', {
                "userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
            })
            driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            return driver
        except Exception as e:
            tries += 1
            print(f"Failed to create driver (attempt {tries}/{max_tries}): {e}")
            time.sleep(2)
    raise Exception("Failed to create Chrome driver after multiple attempts")

def handle_captcha(driver, wait):
    try:
        # Check if captcha is present
        captcha_frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "iframe[title*='hCaptcha']")))
        if captcha_frame:
            print("Captcha detected, attempting to handle...")
            
            # Switch to captcha iframe
            driver.switch_to.frame(captcha_frame)
            
            # Find and click the checkbox
            checkbox = wait.until(EC.element_to_be_clickable((By.ID, "checkbox")))
            # Add random delay to seem more human
            time.sleep(random.uniform(1, 2))
            checkbox.click()
            
            # Switch back to main content
            driver.switch_to.default_content()
            
            # Wait for captcha to be solved or for form to be submittable
            time.sleep(3)  # Give time for potential challenge to appear
            
            # Look for the validate button if it exists
            try:
                validate_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.cb-button")))
                validate_button.click()
            except:
                print("No validate button found, continuing...")
            
            return True
    except Exception as e:
        print(f"Captcha handling error: {e}")
        return False

def fill_form(driver, url):
    try:
        wait = WebDriverWait(driver, 10)
        
        # Navigate to URL with retry
        retries = 3
        for attempt in range(retries):
            try:
                driver.get(url)
                break
            except Exception as e:
                if attempt == retries - 1:
                    raise
                print(f"Failed to load URL (attempt {attempt + 1}/{retries}): {e}")
                time.sleep(2)

        # First check for captcha
        try:
            if handle_captcha(driver, wait):
                print("Captcha handled successfully")
        except:
            print("No captcha found, proceeding with form fill")

        # Wait for form elements to be present
        wait = WebDriverWait(driver, 10)
        
        # Try different selectors with waits
        try:
            name_input = wait.until(EC.presence_of_element_located((By.NAME, "first_name")))
        except:
            name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='الإسم الشخصي']")))
            
        try:
            phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phone")))
        except:
            phone_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='رقم هاتف صحيح']")))

        try:
            city_input = wait.until(EC.presence_of_element_located((By.NAME, "city")))
        except:
            city_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[placeholder='المدينة']")))

        # Fill the form
        name_input.send_keys(get_random_name())
        phone_input.send_keys(get_random_phone())
        city_input.send_keys(get_random_city())

        # Before clicking submit, check for captcha again
        try:
            if handle_captcha(driver, wait):
                print("Post-form captcha handled successfully")
        except:
            print("No post-form captcha found")

        # Try to find and click submit button
        try:
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.button.single-submit[data-pb-field="button-text"]')))
        except:
            submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-pb-value="اضغط هنا للطلب"]')))

        submit_button.click()
        return True

    except Exception as e:
        print(f"Form fill error: {e}")
        return False

def check_pause_status():
    try:
        response = requests.get('http://localhost:5000/status')
        return response.json().get('paused', False)
    except:
        return False

def report_submission():
    try:
        requests.post('http://localhost:5000/submission')
    except:
        pass

def main(url, delay):
    submission_count = 0
    while submission_count < 10000:
        # Check if paused
        while check_pause_status():
            time.sleep(1)
            
        driver = None
        try:
            driver = create_driver()
            if fill_form(driver, url):
                submission_count += 1
                report_submission()
                print(f"Successfully submitted form #{submission_count}")
                
                # Wait only after first submission
                if submission_count > 1:
                    time.sleep(int(delay))
            
        except Exception as e:
            print(f"Main loop error: {e}")
            time.sleep(int(delay))  # Wait before retrying
            
        finally:
            # Always clean up the driver
            if driver:
                try:
                    driver.quit()
                except:
                    pass

if __name__ == "__main__":
    if len(sys.argv) > 2:
        url = sys.argv[1]
        delay = sys.argv[2]
        main(url, delay)
    else:
        print("Please provide URL and delay time as arguments")