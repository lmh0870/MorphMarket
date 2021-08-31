import pandas as pd


def tableMorph(page):
    url = 'https://www.morphmarket.com/us/search?q=&q=&cat=2&sex=&maturity=0&min_weight=0&max_weight=1000000&prey_state=0&prey_food=0&min_genes=4&max_genes=9&traits=&neg_traits=&min_price=0&max_price=1000000&cur=USD&epoch=0&store=&nearby_location=&lat=&lng=&radius=&country=&export=&sort=def&layout=list&page='
    urlPage = f'{url}{page}'
    df = pd.read_html(urlPage)[0]
    print(f'Page {page}')
    return df


def tableGather(start, end, filename):
    for i in range(start, end+1):
        if i == start:
            print("Start")
            mergeDf = tableMorph(i)
        else:
            df = tableMorph(i)
            mergeDf = mergeDf.append(df, ignore_index=True)

    mergeDf.drop_duplicates(inplace=True)
    mergeDf.to_excel(filename, index=False)
    print('Done')
