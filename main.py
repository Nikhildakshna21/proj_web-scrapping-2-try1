from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
from progress.bar import *
from progress.spinner import MoonSpinner
import pandas as pd
import os

START_URL ="https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
browser = webdriver.Chrome('D:\chromedriver.exe')
browser.get(START_URL)

os.system('cls')
with ShadyBar('loading',max=1000) as bar:
    for i in range(1000):
        time.sleep(0.01)
        bar.next()
        



def safe(x):return str(x).encode('utf-8')

#region [rgba(0,0,0,1)] 
def scrape():
    os.system('cls')
    headers = ["star","constellation","right ascension","Declination","apparent magnitude","distance","spectral type","brown dwarf","mass","radius","orbital period","semimajor axis","ecc","discovery year"]
    star_data = []
   
    soup=BeautifulSoup(browser.page_source, "html.parser")
    table = soup.find_all('table')[3]
    for tr in table.find_all('tr'):
        temp_list = []
        for index,td in enumerate(tr.find_all('td')):
            
                if index == 0:
                    temp_list.append(safe(str(td.find('a').string).replace('\u2212','-')))
                elif index == 1:
                    temp_list.append(safe(str(td.find('a').string).replace('\u2212','-')))
                elif index == 2:
                    unit = []
                    val = []
                    val_unit = []
                    output = ''
                    for sup in td.span.find_all('sup'):unit.append(str(sup.string))
                    for sup in td.span.find_all('sup'):sup.decompose()
                    span_string = str(td.span).replace('<span class="nowrap">','').replace('</span>','').split(' ')
                    for a in span_string:
                        if a != '':val.append(a)
                    for ind,b in enumerate(val):val_unit.append(str(b)+unit[ind])
                    for a in val_unit:output += a
                    temp_list.append(output)
                    
                elif index == 3:
                    temp_list.append(safe(str(td.string).replace('\u2032',"'").replace('\u2033','"').replace('\u2212','-').replace('\uff0d','-')))
                    
                elif index == 4:
                    if td.string is None:
                        temp_list.append('')
                    else:
                        temp_list.append(str(td.string))
                
                elif index == 5:
                    if td.string is None:
                        temp_list.append('')
                    else:
                        temp_list.append(str(td.string))   

                elif index == 6:
                      if td.string is None:
                        td.br.decompose()  
                        temp_list.append(safe(str(td).replace('<td>','').replace('</td>','')))
                      else:
                        temp_list.append(safe(str(td.string)))    
                      #print(td) 
                elif index == 7:
                    if td.string is None:
                        temp_list.append(td.a.string)
                    else:
                        temp_list.append(td.string)
                
                elif index == 8:
                    if td.string is None:
                        if not td.sup is None:
                            td.sup.decompose()
                            temp_list.append(str(td.string))
                        elif not td.a is None:
                            st = ''
                            st += str(td.a.var.string)+str(td.a.sub.string)
                            td.a.decompose()
                            temp_list.append(safe(str(td.string)+st))
                        else:
                            temp_list.append('')
                    else:
                        temp_list.append(str(td.string))

                elif index == 9:
                    if td.string is None:
                        temp_list.append('')
                    else:
                        temp_list.append(str(td.string))
                
                elif index == 10:
                    if td.string is None:
                        if not td.sup is None:
                            td.sup.decompose()
                            temp_list.append(str(td.string))
                        else:
                            temp_list.append('')
                    else:
                        temp_list.append(str(td.string))
                elif index == 11:
                    if td.string is None:
                        if not td.sup is None:
                            td.sup.decompose()
                            temp_list.append(str(td.string))
                        else:
                            temp_list.append('')
                    else:
                        temp_list.append(td.string)
                
                elif index == 12:
                    if td.string is None:
                        if not td.sup is None:
                            td.sup.decompose()
                            temp_list.append(str(td.string))
                        else:
                            temp_list.append('')
                    else:
                        temp_list.append(td.string)
                elif index == 13:
                    if td.string is None:
                        if not td.sup is None:
                            td.sup.decompose()
                            temp_list.append(str(td).replace('<td>','').replace('\n</td>',''))
                        else:
                            temp_list.append('')
                    else:
                        temp_list.append(td.string)
                    print(temp_list[13])                    
        star_data.append(temp_list)

    star_data.remove([])
                
    with open("final.csv","w") as f:
        a=csv.writer(f)
        a.writerow(headers)
        a.writerows(star_data)
#endregion        
scrape()
