#Name - Shreyas Ravi
#Date - 02/14/2021
#Honor Statement - I have not given or recieved any unauthorized assistance for this assignment
#YoutTube Link - https://youtu.be/JUzSuaz8iq0



from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser
from operator import itemgetter
from re import search
import re
stop_words = ['a', 'about', 'above', 'across', 'after', 'afterwards', 'again',
'against', 'all', 'almost', 'alone', 'along', 'already', 'also',
'although', 'always', 'am', 'among', 'amongst', 'amoungst',
'amount', 'an', 'and', 'another', 'any', 'anybody', 'anyhow', 'anyone',
'anything', 'anyway', 'anywhere', 'are', 'area', 'areas', 'around',
'as', 'ask', 'asking', 'asked', 'asks', 'at', 'b', 'back', 'backed',
'backing', 'backs' 'be','became', 'because', 'become', 'becomes',
'becoming', 'been', 'before', 'began', 'beforehand', 'behind', 'being',
'beings', 'best', 'better', 'below', 'beside', 'besides',
'between', 'beyond', 'big', 'bill', 'both', 'bottom', 'but', 'by', 'c',
'call', 'came', 'can', 'cannot', 'cant', 'case', 'cases', 'certain',
'certainly', 'clear', 'clearly', 'come', 'computer', 'con', 'could',
'couldnt', 'cry', 'd', 'de', 'describe', 'detail', 'did', 'differ',
'different', 'differently', 'do', 'does', 'done', 'down', 'downed',
'downing', 'downs', 'dr', 'due', 'during', 'e', 'each', 'early', 'eg',
'eight', 'either', 'eleven', 'else', 'elsewhere', 'empty', 'end', 'ended',
'ending', 'ends', 'enough', 'etc', 'even', 'evenly', 'ever', 'every',
'everybody', 'everyone', 'everything', 'everywhere', 'except', 'f', 'face',
'faces', 'fact', 'facts', 'far', 'felt', 'few', 'fifteen', 'fifty', 'fill',
'find', 'finds', 'fire', 'first', 'five', 'for', 'former', 'formerly',
'forty', 'found', 'four', 'from', 'front', 'full', 'fully', 'further',
'furthered', 'furthering', 'furthers', 'g', 'gave', 'general', 'generally',
'get', 'gets', 'give', 'given', 'gives', 'go', 'going', 'good', 'goods',
'got', 'great', 'greater', 'greatest', 'group', 'grouped', 'groups', 'had',
'h', 'had', 'has', 'hasnt', 'have', 'having', 'he', 'hence', 'her',
'here', 'hereafter', 'hereby', 'herein', 'hereupon', 'hers', 'herself',
'high', 'higher', 'highest', 'him', 'himself', 'his', 'how', 'however',
'hundred', 'i', 'ie', 'if', 'important', 'in', 'inc', 'indeed',
'interest', 'interested', 'interesting', 'interests', 'into', 'is',
'it', 'its', 'itself', 'j', 'just', 'k', 'keep', 'keeps', 'kind',
'knew', 'know', 'known', 'knows', 'l', 'large', 'largely', 'last',
'later', 'latest', 'latter', 'latterly', 'least', 'less', 'let',
'lets', 'like', 'likely', 'long', 'longer', 'longest', 'ltd', 'm', 'made',
'make', 'making', 'man', 'many', 'may', 'me', 'meanwhile', 'member',
'members', 'men', 'might', 'mill', 'mine', 'more', 'moreover',
'most', 'mostly', 'move', 'mr', 'mrs', 'ms', 'much', 'must', 'my',
'myself', 'n', 'name', 'namely', 'necessary', 'need', 'needed', 'needing',
'needs', 'neither', 'never', 'nevertheless', 'new', 'newer', 'newest',
'next', 'nine', 'no', 'nobody', 'non', 'none', 'noone', 'nor', 'not',
'nothing', 'now', 'nowhere', 'number', 'numbers', 'o', 'of', 'off',
'often', 'old', 'older', 'oldest', 'on', 'once', 'one', 'only', 'onto',
'open', 'opened', 'opening', 'opens', 'or', 'order', 'ordered', 'ordering',
'orders', 'other', 'others', 'otherwise', 'our', 'ours', 'ourselves', 'out',
'over', 'own', 'p', 'part', 'parted', 'parting', 'parts', 'per', 'perhaps',
'place', 'places', 'please', 'point', 'pointed', 'pointing', 'points',
'possible', 'present', 'presented', 'presenting', 'presents', 'problem',
'problems', 'put', 'puts', 'q', 'quite', 'r', 'rather', 're', 'really',
'right', 'room', 'rooms', 's', 'said', 'same', 'saw', 'say', 'says',
'second', 'seconds', 'see', 'seem', 'seemed', 'seeming', 'seems', 'sees',
'serious', 'several', 'shall', 'she', 'should','show', 'showed', 'showing',
'shows', 'side', 'sides', 'since', 'sincere', 'six', 'sixty', 'small',
'smaller', 'smallest', 'so', 'some', 'somebody', 'somehow', 'someone',
'something', 'sometime', 'sometimes', 'somewhere', 'state', 'states', 'still',
'such', 'sure', 'system', 't', 'take', 'taken', 'ten', 'than',
'that', 'the', 'their', 'them', 'themselves', 'then', 'thence',
'there', 'thereafter', 'thereby', 'therefore', 'therein', 'thereupon',
'these', 'they', 'thick', 'thin', 'thing', 'things', 'think', 'thinks',
'third', 'this', 'those', 'though', 'thought', 'thoughts', 'three', 'through',
'throughout', 'thru', 'thus', 'to', 'today', 'together', 'too', 'took', 'top',
'toward', 'towards', 'turn', 'turned', 'turning', 'turns', 'twelve', 'twenty',
'two', 'u', 'un', 'under', 'until', 'up', 'upon', 'us', 'use', 'used', 'uses',
'v', 'very', 'via', 'w', 'want', 'wanted', 'wanting', 'wants', 'was', 'way',
'ways', 'we', 'well', 'wells', 'went', 'were', 'what', 'whatever', 'when',
'whence', 'whenever', 'where', 'whereafter', 'whereas', 'whereby', 'wherein',
'whereupon', 'wherever', 'whether', 'which', 'while', 'whither', 'who',
'whoever', 'whole', 'whom', 'whose', 'why', 'will', 'with', 'within',
'without', 'work', 'worked', 'working', 'works', 'would', 'x', 'y', 'year',
'years', 'yet', 'you', 'young', 'younger', 'youngest', 'your', 'yours',
'yourself', 'yourselves', 'z']


class Collector(HTMLParser):
    'collects hyperlink URLs into a list'

    def __init__(self, url):
        'initializes parser, the url, and a list'
        HTMLParser.__init__(self)
        self.url = url
        self.links = []
        self.data = ''
        self.starttag = '' #initiated method starttag recognizes the type of text
        
    def handle_data(self,data):
        if self.starttag != 'script' and self.starttag != 'style': #do not want script or style just body
            self.data = self.data+' ' +str(data).strip() #getting rid of whitespaces

    def handle_starttag(self, tag, attrs):
        
            'collects hyperlink URLs in their absolute format'
            self.starttag = tag
            if tag == 'a': #a for hyperlink since we are looking for hyperlinks
                for attr in attrs:
                    if attr[0] == 'href': #attribute to a tag
                        # construct absolute URL
                        absolute = urljoin(self.url, attr[1])
                        if search('law.depaul.edu', absolute)!=None:
                            # collect HTTP URLs
                            self.links.append(absolute)
                            
                    
    def getLinks(self):
        'returns hyperlinks URLs in their absolute format'
        return self.links
    
    def getData(self):
        'get the entire text from the webpage'
        return self.data
            
visited=set() #initialize visited to an empty set
dictionary = {}
def crawl2(url):
    '''a recursive web crawler that calls analyze()
       on every visited web page'''

    # add url to set of visited pages
    global visited     # warns the programmer 
    visited.add(url)

    # analyze() returns a list of hyperlink URLs in web page url 
    links = analyze(url)

    # recursively continue crawl from every link in links
    for link in links:
        # follow link only if not visited
        if link not in visited:
            try:
                crawl2(link)
            except:
                pass
    

def main():
    url = input('Please enter your url to be crawled: ')
    crawl2(url)
    #print(dict(sorted(dictionary.items(), key=lambda item: item[1])[:25]))
    print(dict(sorted(dictionary.items(), key = itemgetter(1), reverse = True)[:25]))
    #itemgetter - takes first key from dictionary and returns it 

def analyze(url):
    
    print('\n\nVisiting', url)           # for testing

    # obtain links in the web page
    content = urlopen(url).read().decode()
    collector = Collector(url)
    collector.feed(content)
    urls = collector.getLinks()          # get list of links
    # print(content)
    # compute word frequencies
    content = collector.getData() # get the entire text
    # print(content)
    content = re.sub('[^a-zA-Z ]','',content)
    # print(content)
    freq = frequency(content)       #count the most frequent words 
    return urls

def frequency(content):
    
   # split all the word of the string. 
    lst = content.split() 
   
    # take each word from lst and pass it to the method count. 
    for elements in lst: 
        if elements not in stop_words:
            # if there exists a key as "elements" then simply 
            # increase its value. 
            if elements in dictionary: 
                dictionary[elements] += 1
           
            # if the dictionary does not have the key as "elements"  
            # then create a key "elements" and assign its value to 1. 
            else: 
                dictionary.update({elements: 1})
                
                
                
    



            
            
            
            
    
    
        
