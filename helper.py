import json
import logging
from urllib.request import urlopen
from threading import Thread

def sortList(result, key="id", order=False):
    return sorted(result, key=lambda k: k.get(key, 0), reverse=order)

def removeduplicate(result):
    lst=[]
    ids=[]
    for each in result:
        for post in each["posts"]:
            if(post["id"] not in ids):
                lst.append(post)
                ids.append(post["id"])
    return lst

def threading(urls):
    result = [{} for x in urls]
    threads = []
    # In this case 'urls' is a list of urls to be crawled.
    for ii in range(len(urls)):
        # We start one thread per url present.
        process = Thread(target=crawl_posts, args=[urls[ii], result, ii])
        process.start()
        threads.append(process)
    # We now pause execution on the main thread by 'joining' all of our started threads.
    # This ensures that each has finished processing the urls.
    for process in threads:
        process.join()


    return removeduplicate(result)

def crawl_posts(url, result, index):
    
    try:
        data = urlopen(url).read()
        logging.info("Requested..." + url)
        result[index] = json.loads(data.decode('utf8').replace("'", '"'))
    except:
        logging.error('Error with URL check!')
        result[index] = {}

    return True
