def name_encoder(url):

    url_splits = []
    url_splits = url.split(".")
    encoded_url = ""

    for i in url_splits:
         url_spl_len = len(i)
         encoded_url += str(url_spl_len) + i
    
    encoded_url+="0"
    return encoded_url




def main():

    url = "www.google.com"
    encoded_url =  name_encoder(url)

main()