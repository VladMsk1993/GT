from selenium.webdriver.common.by import By


class LoginPageLocators():
    """Страница авторизации при входе на портал GlobalTruck."""

    E_MAIL = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "#kc-login")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "#kc-content-wrapper > div.alert.alert-error > span.kc-feedback-text")


class AdminPageLocators():
    """Панель админа"""

    USERS_BUTTON = (By.XPATH, "//*[@id=\"view\"]/div[2]/div[3]/ul/li[2]/a")
    SEARCH = (By.CSS_SELECTOR, ".form-control.search.ng-pristine.ng-untouched.ng-valid.ng-empty")
    SEACRH_BOTTUN = (By.CSS_SELECTOR, ".fa-search")
    IMPERSIONATE_BUTTON = (By.CSS_SELECTOR, "[data-ng-click='impersonate(user.id)']")


class CounterPartyPageLocators():
    """Страница перевозчики в SRM."""

    COUNTERPARTY_BUTTON = (By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[1]/div[1]/div/a[2]")   #Кнопка левого меню.
    BUTTON_CREATE_COUNTERPARTY = (By.CSS_SELECTOR, ".UiButton_filled_xjAHl")
    SEACRH_BOTTUN = (By.XPATH, "//*[@id=\"content\"]/div[1]/div[2]/div/div[1]")
    SEARCH_AREA = (By.CSS_SELECTOR, "[data-qa='PageCarrierHeaderInputSearchBox']")
    THE_RESULT = (By.CSS_SELECTOR, ".OrgNameCell_name_-2HkL")

    DOCUMENT_LINK = (By.CSS_SELECTOR, "")
    DOWNLOAD_DOCUMENT1 = (By.CSS_SELECTOR, "")
    DOWNLOAD_DOCUMENT2 = (By.CSS_SELECTOR, "")
    DOWNLOAD_DOCUMENT3 = (By.CSS_SELECTOR, "")
    DOWNLOAD_DOCUMENT4 = (By.CSS_SELECTOR, "")

    AGREEMENT_LINK = (By.CSS_SELECTOR, "")
    AGREEMENT_BUTTON = (By.CSS_SELECTOR, ".UiButton_filled_xjAHl")


class CreateCounterPartyPageLocators():
    """Окно создания нового перевозчика при нажатии на кнопку "Добавить" на странице "Перевозчики" (SRM)."""

    INN_AREA = (By.CSS_SELECTOR, ".multiselect.UiMultiSelect_multiselect_35zUA")
    INN_SEARCH_BUTTON = (By.CSS_SELECTOR, ".SvgIcon_svg_39_CT.OrgStepOnboarding_icon_3iGZt")
    START_BUTTON = (By.XPATH, "//*[@id=\"app\"]/div[2]/div/div[2]/div[3]/div/button")   #Необходим нормальный CCS от разраба!

    BIK_AREA = (By.XPATH, "//*[@i]") #Необходим нормальный CCS от разраба!
    CHECKING_ACCOUNT = (By.CSS_SELECTOR, "[placeholder='20 цифр'")
    CONFIRM_BUTTON1 = (By.CSS_SELECTOR, ".UiButton_isHaveAppendIcon_37q3d") #Необходим нормальный CCS от разраба!

    EMAIL_AREA = () #Необходим нормальный CCS от разраба!
    PHONE_AREA = () #Необходим нормальный CCS от разраба!
    CONFIRM_BUTTON2 = (By.CSS_SELECTOR, ".UiButton_appendIcon_2czVf")   #Необходим нормальный CCS от разраба!

    GARAGE_ADDRESS = (By.CSS_SELECTOR, ".UiTextarea_input_Jm2ka")
    CONFIRM_BUTTON3 = (By.CSS_SELECTOR, ".UiButton_appendIcon_2czVf")   #Необходим нормальный CCS от разраба!


class CreateAutoLocators():
    """Страница контрагента в SRM. Добавление траснпортнго стредства."""
    TS_LINK = (By.CSS_SELECTOR, "[data-qa='CarrierSideBarMenuVehicles']")
    CREATE_BUTTON = (By.CSS_SELECTOR, ".UiButton_content_3_QEx")

    TRUCK_RADIO = (By.CSS_SELECTOR, "")
    TRAILER_RADIO = (By.XPATH, "//label[text()=\"Прицеп\"]")
    CONFIRM_BUTTON1 = (By.XPATH, "//span[text()=\" Начать \"]")

    DOWNLOAD_DOCUMENT1 = (By.CSS_SELECTOR, "")
    DOWNLOAD_DOCUMENT2 = (By.CSS_SELECTOR, "")
    SERIA_AREA1 = (By.CSS_SELECTOR, "")
    NOMBER_AREA1 = (By.CSS_SELECTOR, "")
    DATA_GIVEN1 = (By.CSS_SELECTOR, "")
    GIVEN_BY1 = (By.CSS_SELECTOR, "")
    DOWNLOAD_DOCUMENT3 = (By.CSS_SELECTOR, "")
    DOWNLOAD_DOCUMENT4 = (By.CSS_SELECTOR, "")
    SERIA_AREA2 = (By.CSS_SELECTOR, "")
    NOMBER_AREA2 = (By.CSS_SELECTOR, "")
    DATA_GIVEN2 = (By.CSS_SELECTOR, "")
    GIVEN_BY2 = (By.CSS_SELECTOR, "")
    CONFIRM_BUTTON2 = (By.CSS_SELECTOR, "")

    MARK_AUTO = (By.CSS_SELECTOR, "[placeholder='Выберите марку']")
    GOV_NUMBER = (By.CSS_SELECTOR, "[placeholder='Введите гос. номер']")
    COUNTRY = (By.CSS_SELECTOR, "")
    VIN_NUMBER = (By.CSS_SELECTOR, "[placeholder='Введите VIN']")
    YEAR_PRODUCTION = (By.CSS_SELECTOR, "")
    CONFIRM_BUTTON3 = (By.CSS_SELECTOR, "")
    TYPE_TRAILER = (By.CSS_SELECTOR, "[placeholder='Выберите полуприцеп']")
    TYPE_LOADING = (By.CSS_SELECTOR, "[placeholder='Выберите тип погрузки']")


class CreateDriverLocators():
    """Страница контрагента в SRM. Добавление водителя."""
    DRIVER_LINK = (By.CSS_SELECTOR, "[data-qa='CarrierSideBarMenuDrivers']")
    CREATE_BUTTON = (By.CSS_SELECTOR, ".UiButton_content_3_QEx")

    DOWNLOAD_DOCUMENT1 = (By.CSS_SELECTOR, "#app > div:nth-child(2) > div > div.UiPanelContent_content_IDJtS > div.UiPanelContent_contentBody_2xZoq > div > div.DriverDocuments_container_MMNIa > div:nth-child(1) > div > form:nth-child(3) > div > div > div.UiFile_actions_2Ea7_ > label > svg")
    DOWNLOAD_DOCUMENT2 = ()
    SERIA_AREA1 = (By.CSS_SELECTOR, "")
    NOMBER_AREA1 = (By.CSS_SELECTOR, "")
    DATA_GIVEN1 = (By.CSS_SELECTOR, "")
    GIVEN_BY1 = (By.CSS_SELECTOR, "")
    DOWNLOAD_DOCUMENT3 = (By.CSS_SELECTOR, "")
    DOWNLOAD_DOCUMENT4 = (By.CSS_SELECTOR, "")
    SERIA_AREA2 = (By.CSS_SELECTOR, "")
    NOMBER_AREA2 = (By.CSS_SELECTOR, "")
    DATA_GIVEN2 = (By.CSS_SELECTOR, "")
    GIVEN_BY2 = (By.CSS_SELECTOR, "")
    CONFIRM_BUTTON1 = (By.CSS_SELECTOR, "")

    FIRST_NAME = (By.CSS_SELECTOR, "[placeholder='Введите фамилию']")
    SECOND_NAME = (By.CSS_SELECTOR, "[placeholder='Введите имя']")
    FATHER_NAME = (By.CSS_SELECTOR, "[placeholder='Введите отчество']")
    BIRTHDAY_DATE = (By.CSS_SELECTOR, "")
    PHONE_NUMBER = (By.CSS_SELECTOR, "[placeholder='+7 (000) 000-00-00']")
    CONFIRM_BUTTON2 = (By.CSS_SELECTOR, "")


class LeftMenuLocators():
    """Левоё меню в модуле СЭБ."""
    WORK_PAGE_BUTTON = (By.XPATH, "//span[text()=\" Рабочий стол \"]")
    COUNTEPARTY_BUTTON = (By.XPATH, "//span[text()=\" Контрагенты \"]")
    ELASTIC_BUTTON = (By.XPATH, "//span[text()=\" Дашборд \"]")
    EXIT_BUTTON = (By.XPATH, "//span[text()=\" Выход \"]")
    WORK_PAGE = (By.XPATH, "//div[text()=\" Рабочий стол \"]")
    COUNTEPARTY_PAGE = (By.XPATH, "//div[text()=\" Контрагенты \"]")


class MainPageLocators():
    """Основаная страница 'Рабочий стол'."""
    ALL = ()
    VEHICLE = (By.XPATH, "//a[text()=' ТС ']")
    DRIVERS = (By.XPATH, "//a[text()=' Водители ']")
    COUNTERPARTY = (By.XPATH, "//a[text()=' Контрагенты ']")
    SEARCH_RESULT = (By.CSS_SELECTOR, ".SecurityEntityTitle_name_yh3xC")


class HeaderLocators():
    """Страница СЭБ"""
    SEARCH = (By.CSS_SELECTOR, "[placeholder='Поиск в таблице']")
    SPECTRUM_BUTTON = (By.CSS_SELECTOR, "[title='Спектрум']")
    GBDD_BUTTON = (By.CSS_SELECTOR, "[title='ГИБДД']")
    RSA_BUTTON = (By.CSS_SELECTOR, "[title='РСА']")
    KONTUR_FOCUS_LINK = (By.XPATH, "//span[text()=' Перейти в Контур.Фокус ']")
    ATISU_LINK = (By.XPATH, "//span[text()=' Перейти в Ati.su ']")


class DriverPageLocators():
    """Карточка водителя в СЭБ."""
    TAKE_FOR_WORK = (By.XPATH, "//span[text()=' Взять в работу ']")
    STATUS_NEW = (By.CSS_SELECTOR, ".UiBadge_danger_UhxIo")
    STATUS_IN_AGREEING = (By.CSS_SELECTOR, ".UiBadge_warning_x5niQ")
    STATUS_AGREED = (By.CSS_SELECTOR, ".UiBadge_success_3DNJW")
    AGREE_BUTTON = (By.XPATH, "//span[text()=' Согласовать ']")
    DENY_BUTTON = (By.XPATH, "//span[text()=' Отклонить ']")
    CHANGE_BUTTON = (By.XPATH, "//span[text()=' Изменить ']")


class CounterpartyPageLocators():
    """Карточка контрагента."""
    CHANGE_BUTTON = (By.XPATH, "//span[text()=' Изменить ']")


class ExchangeWindow():
    CONFIRM_BUTTON = (By.XPATH, "//label[text()=' Согласовать ']")
    DENY_BUTTON = (By.CSS_SELECTOR, "[value=\"4\"]")
    REPEAT_BUTTON = (By.XPATH, "//label[text()=' Повторная проверка ']")
    COMMENT_MANAGER = (By.CSS_SELECTOR, "[placeholder='Комментарий для менеджера']")
    COMMENT_SB = (By.CSS_SELECTOR, "[placeholder='Комментарий для СБ']")


class SpectrumLocators():
    CHECK_BUTTON = (By.XPATH, "//span[text()=' Проверить ']")
    GOOD_RESULT_CHECKING = (By.XPATH, "//span[text()=' Проверка завершена, результат вы можете увидеть в разделе \"Отчеты\" ']")
    CLOSE_BUTTON = (By.CSS_SELECTOR, "")
    LICENSE_PAGE = (By.XPATH, "//a[text()=\" Водительское удостоверение \"]")