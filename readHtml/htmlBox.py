import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


class boxClass:
    def __init__(self, url, test=False, chromePath=r"C:\myPackage\chromedriver.exe"):
        self.options = Options()
        self.url = url
        if test == False:
            self.options.add_argument("headless")
        self.driver = webdriver.Chrome(
            executable_path=chromePath, options=self.options)
        self.driver.implicitly_wait(3)

    def boxLastpage(self):
        self.driver.get(self.url)
        lastPage = self.driver.find_element_by_xpath(
            '/html/body/div[3]/div[3]/div/div[4]/div/div/div/ul/li[9]/a').get_attribute('href')
        lastPage = lastPage.split('page=')[-1]
        return int(lastPage)

    def boxUrl(self, page):
        self.driver.get(f'{self.url}{page}')
        elem = self.driver.find_elements_by_xpath(
            '/html/body/div[3]/div[3]/div/div[2]/div')

        for el in elem:
            imageLink = el.find_element_by_tag_name('img').get_attribute('src')
            link = el.find_element_by_tag_name('a').get_attribute('href')
            # print(imageLink, link)

            try:
                df = df.append(pd.DataFrame(
                    {'Link': link, 'Src': imageLink}, index=[0]), ignore_index=True)
            except:
                df = pd.DataFrame(
                    {'Link': link, 'Src': imageLink}, index=[0])
        if len(elem) == 0:  # Recursive
            print('Retry')
            self.boxUrl(page)
        else:
            return df

    def boxGather(self, start, filename):
        end = self.boxLastpage()
        for i in range(start, end+1):
            if i == start:
                print("Start")
                mergeDf = self.boxUrl(i)
            else:
                df = self.boxUrl(i)
                mergeDf = mergeDf.append(df, ignore_index=True)
            print(f'Page {i}')
        mergeDf.drop_duplicates(inplace=True)
        mergeDf.to_excel(filename, index=False)
        print('Done')
