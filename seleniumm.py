from selenium import webdriver

url_lists = []
current_url_lists=[]

#for i in range(0, 866):
#	name = input()
#	url_lists.append(name)

with open('url_input') as f:
	content = f.readlines()

url_lists = [x.strip() for x in content]

driver = webdriver.Chrome('/Users/ascent/Downloads/chromedriver')
for url in url_lists:
	driver.implicitly_wait(3)
#reach to url
#driver.get('https://nid.naver.com/nidlogin.login')
	#driver.get('https://www.expedia.co.kr/.0-n6337943-0.Travel-Guide-Filter-Hotels')
	driver.get(url)
	driver.implicitly_wait(5)
	current_url_lists.append(driver.current_url)

print(current_url_lists)
with open('output', mode='wt', encoding='utf-8') as myfile:
    myfile.write('\n'.join(current_url_lists))
