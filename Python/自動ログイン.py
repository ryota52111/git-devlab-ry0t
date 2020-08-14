from selenium import webdriver
borwser = webdriver.Chrome(executable_path=r'chromedriver.exeのファイルパス')
borwser.get("https://ja-jp.facebook.com/")
borwser.find_element_by_id("email").send_keys("IDを入力")
borwser.find_element_by_id("pass").send_keys("passwordを入力")
borwser.find_element_by_id("u_0_b").submit()

