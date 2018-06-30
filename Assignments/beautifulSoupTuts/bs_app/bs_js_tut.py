import dryscrape

sess = dryscrape.Session()
sess.visit('https://pythonprogramming.net/parsememcparseface/')
source = sess.body()

soup = bs.BeautifulSoup(source,'lxml')
js_test = soup.find('p', class_='jstest')
print(js_test.text)