"""

"""
from time import sleep
import keyring
from selenium import webdriver

envs = {
    "cz_test_CI": {
        "web_app": "http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/",
        "usr": "cis\\m.houska",
        "pwd": "heslo",
    },
    "cz_test": {
        "web_app": "https://test.tfsonline.cz/ToyotaDcM_branch/",
        "usr": "tfscz.cisadm.Houska",
        "pwd": "",  # see KeyPass CI
    },
    "cz_live": {
        "web_app": "https://www.tfsonline.sc/ToyotaDcM/",
        "usr": "tfscz.cisadm.Houska",
        "pwd": "",  # see KeyPass CI
    },
    "sk_live": {
        "web_app": "https://www.tfsonline.sk/ToyotaDcMSK/",
        "usr": "tfssk.cisadm.Houska",
        "pwd": "",  # see KeyPass CI
    },
}


def init(env_key="cz_test", kr=True):
    """
    keyring info - see below
    keyring: system <- env_key
    """
    try:
        env = envs[env_key]
    except:
        raise ValueError

    browser, web_app = open_browser(env)
    sleep(0.3)
    if kr:
        kr_sys = env_key
    else:
        kr_sys = None
    login(browser, env, kr_sys=kr_sys)

    return browser, web_app


def open_browser(env):
    browser = webdriver.Chrome()
    # web_app = "http://cishd-cls-app01/dm/CzechRep_Toyota_branch/Dev/WebApp/"
    web_app = env["web_app"]
    browser.get(web_app)
    return browser, web_app


def login(browser, env, kr_sys=None):
    try:
        usr = browser.find_element_by_id("txtUsername")
        pwd = browser.find_element_by_id("txtPassword")
        log_in = browser.find_element_by_id("btnLogin")

        usr_val = env["usr"]
        pwd_val = ""
        if kr_sys is None:
            pwd_val = env["pwd"]
        else:
            keyring.get_keyring()
            pwd_val = keyring.get_password(kr_sys, usr_val)

        sleep(0.3)
        usr.send_keys(usr_val)
        if pwd_val != "":
            pwd.send_keys(pwd_val)
            sleep(0.2)
            log_in.click()
            print("tried to log in")
    except:
        print("problem with login or already logged in")


"""
https://pypi.org/project/keyring/


conda install keyring
$ python
>>> import keyring
>>> keyring.get_keyring()
<keyring.backends.SecretService.Keyring object at 0x7f9b9c971ba8>
>>> keyring.set_password("system", "username", "password")
>>> keyring.get_password("system", "username")
'password'




"""