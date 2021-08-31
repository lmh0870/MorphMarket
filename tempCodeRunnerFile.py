from readHtml import htmlBox

box = htmlBox.boxClass(url='https://www.morphmarket.com/us/search?q=&q=&cat=2&sex=&maturity=0&min_weight=0&max_weight=1000000&prey_state=0&prey_food=0&min_genes=4&max_genes=9&traits=&neg_traits=&min_price=0&max_price=1000000&cur=USD&epoch=0&store=&nearby_location=&lat=&lng=&radius=&country=&export=&sort=def&layout=grid&page=')
box.boxGather(
    start=1,
    filename=r'C:\Users\Newcrop\Desktop\sample1.xlsx')
