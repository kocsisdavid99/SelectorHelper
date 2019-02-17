from selenium import webdriver
from selenium.webdriver.chrome.options import Options

raw_url_list = open("url_list.txt", "r")

options = Options()
options.add_argument('--headless')
options.add_argument('--silent')
options.add_argument('--disable-gpu')
options.add_argument('--log-level=3')
        
browser = webdriver.Chrome(executable_path='./chromedriver.exe', chrome_options=options)


statistics_0 = 0
statistics_1 = 0
statistics_2 = 0
statistics_3 = 0
 

for row in raw_url_list:
    row = row.split()
    row = str(row)
    row = row.strip()
    
   
    row = row.replace("['","")
    row = row.replace("']","")
    row = row.replace("', '›","")

    try:

        browser.get(row)
        source = browser.page_source
        source = str(source)
        
        if "entry-title" in source:
            status = 1
            statistics_1 += 1
            
        elif "post__link" in source:
            status = 2
            statistics_2 += 1
            
        else:
            status = 0
            statistics_3 += 1
            
            


        if status == 0:
            status = "Nem felismerhetõ"
            
        elif status == 1:
            status = ".entry-title>a a link selector"
        elif status == 2:
            status = "a.post__link a link selector"


        print("{0} -------- {1}".format(row, status))
    except Exception:
        print(row,"kihagytam")
        statistics_0 += 1
        pass
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

print("Statisztika:")
        

print(statistics_0,"db", "kihagytam") #kihagytam
print(statistics_1,"db", ".entry-title>a") #entry-title
print(statistics_2,"db", "a.post__link") #post-link
print(statistics_3,"db", "nem felismerhetõ") #nem felismerhetõ


        


    




