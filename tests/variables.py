from faker import Faker


#Ссылки:
admin_link = "https://staging.portal.globaltruck.ru/auth/admin/master/console/#/realms/globaltruck"
main_link = "https://staging.portal.globaltruck.ru/"
new_counterparty_link = "https://staging.portal.globaltruck.ru/srm/orgs?action=add"
sb_link = "https://staging.portal.globaltruck.ru/security/requests"
GBDD_url = "https://xn--90adear.xn--p1ai/check/"
RSA_url = "https://dkbm-web.autoins.ru/dkbm-web-1.0/policyInfo.htm?serviceUnavailable=true"
focus_url = "https://focus.kontur.ru/login"
ati_url = "https://ati.su/"


#Данные:
manager_name = "галиакбарова"
login = "Sharaev_VA"
password = "Frght23hx"
counterparty_name = "БЕРКАТ ЕЕ"
inn_date = "7751515581"

#Фейковые параметры:
fake = Faker('ru_RU')
first_name = fake.first_name_male()
last_name = fake.last_name_male()
#middle_name = fake.middle_name()
phone_number = fake.phone_number()
inn_number = fake.ssn()
individual_inn = fake.individuals_inn()
business_inn = fake.businesses_inn()
seria_number = fake.plate_number_extra()
passport_number = fake.plate_number_special()
bic_number = fake.bic()
checking_account = fake.checking_account()
date = fake.date()
birthday = fake.date_of_birth()
email = fake.email()
address = fake.address()
gov_number = fake.license_plate()
company_form = fake.company_prefix()
