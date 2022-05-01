import webbrowser

def website_opener(domain):
    try:
        url = 'https://www.' + f"{domain}.com"
        webbrowser.open(url)
        return True
    except Exception as e:
        print(e)
        return False