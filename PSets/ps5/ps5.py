# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory

class NewsStory(object):
    def __init__(self, guid, title, description, link, pubdate):
        
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        
        
    def get_guid(self):
        """ 
        returns the value of GUID
        
        """
        return self.guid
    
    def get_title(self):
        """ 
        returns the value of title
        
        """
        return self.title
    
    def get_description(self):
        """ 
        returns the value of description
        
        """
        return self.description
    
    def get_link(self):
        """ 
        returns the value of link
        
        """
        return self.link
    def get_pubdate(self):
        """ 
        returns the value of pubdate
        
        """
        return self.pubdate
            

    
#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# TODO: PhraseTrigger

class PhraseTrigger(Trigger):
    
    def __init__(self, phrase):
        
        self.phrase = phrase

# Problem 3
# TODO: TitleTrigger
class TitleTrigger(PhraseTrigger):
    def __init__(self, phrase):
        
        PhraseTrigger.__init__(self, phrase)
        
        
    def evaluate(self, story):
        Cphrase = self.phrase
        Cphrase = Cphrase.lower()
        Oristory = story.get_title()
        Cstory = Oristory[:].lower()
        clear = ''
        
        for i in Cstory:
            if i in string.punctuation:
                clear+=" "
            else:
                clear+= i
                
        clear = clear.strip(" ")
        clear = clear.split(" ")
        Copyclear = clear[:]
        
        result_clear = ""
        for i in Copyclear:
            if i == '':
                clear.remove(i)
            else:
                result_clear+= i
                result_clear+= " "
                
        Copyclear = clear[:]
        clear = result_clear[:-1]
        # print(clear)
        second_check = set(Cphrase.split(" ")).issubset(Copyclear)

        if Cphrase in clear:
            return True and second_check
        else:
            return False and second_check
    
# Problem 4
# TODO: DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, phrase):
        
        PhraseTrigger.__init__(self, phrase)
        
        
    def evaluate(self, story):
        Cphrase = self.phrase
        Cphrase = Cphrase.lower()
        Oristory = story.get_description()
        Cstory = Oristory[:].lower()
        clear = ''
        
        for i in Cstory:
            if i in string.punctuation:
                clear+=" "
            else:
                clear+= i
                
        clear = clear.strip(" ")
        clear = clear.split(" ")
        Copyclear = clear[:]
        
        result_clear = ""
        for i in Copyclear:
            if i == '':
                clear.remove(i)
            else:
                result_clear+= i
                result_clear+= " "
                
        Copyclear = clear[:]
        clear = result_clear[:-1]
        # print(clear)
        second_check = set(Cphrase.split(" ")).issubset(Copyclear)

        if Cphrase in clear:
            return True and second_check
        else:
            return False and second_check
    
# TIME TRIGGERS
# Problem 5
# TODO: TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.

class TimeTrigger(Trigger):
    def __init__(self, Time):
        self.Time = time.strptime(Time, "%d %b %Y %H:%M:%S")
        self.Time = self.Time.replace(tzinfo=pytz.timezone("EST"))
        
# Problem 6
# TODO: BeforeTrigger and AfterTrigger

class BeforeTrigger(TimeTrigger):
    def __init__(self, Time):
        TimeTrigger.__init__(self, Time)
        
    def evaluate(self, story):
        
        storytime = story.get_pubdate()[:]
        storytime = storytime.replace(tzinfo=pytz.timezone("EST"))
        if self.Time > storytime:
            return True 
        else:
            return False
        
        # # time1 = time.strptime(story.get_pubdate(), "%d %b %Y %H:%M:%S")
        # time1 = story.get_pubdate().replace(tzinfo=pytz.timezone("EST"))
        # time2 = self.Time
        # if time1.tm_year >= time2.tm_year:
        #     # print("passed1")
        #     if time1.tm_mon >= time2.tm_mon:
        #         # print("passed2")
        #         if time1.tm_mday >= time2.tm_mday:
        #             # print("passed3")
        #             if time1.tm_hour >= time2.tm_hour:
        #                 # print("passed4")
        #                 if time1.tm_min >= time2.tm_min:
        #                     # print("passed5")
        #                     if time1.tm_sec >= time2.tm_sec:
        #                         # print("passed6")
        #                         return False
            
        # return True
    
    
class AfterTrigger(TimeTrigger):
    def __init__(self, Time):
        TimeTrigger.__init__(self, Time)
        
    def evaluate(self, story):
        storytime = story.get_pubdate()[:]
        storytime = storytime.replace(tzinfo=pytz.timezone("EST"))
        if self.Time < storytime:
            return True 
        else:
            return False

# COMPOSITE TRIGGERS

# Problem 7
# TODO: NotTrigger
class NotTrigger(Trigger):
    
    def __init__(self, OtherTrigger):
        self.OtherTrigger = OtherTrigger
        
    def evaluate(self, news_item):
       return not self.OtherTrigger.evaluate(news_item)
       
        
        
    
# Problem 8
# TODO: AndTrigger

class AndTrigger(Trigger):
    
    def __init__(self, Triggerone, Triggertow):
        self.Triggerone = Triggerone
        self.Triggertow = Triggertow
        
    def evaluate(self, news_item):
       return self.Triggerone.evaluate(news_item) and self.Triggertow.evaluate(news_item)

# Problem 9
# TODO: OrTrigger

class OrTrigger(Trigger):
    
    def __init__(self, Triggerone, Triggertow):
        self.Triggerone = Triggerone
        self.Triggertow = Triggertow
        
    def evaluate(self, news_item):
       return self.Triggerone.evaluate(news_item) or self.Triggertow.evaluate(news_item)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    finalstories= []
    for s in stories:
        for t in triggerlist:
            if t.evaluate(s):
                finalstories.append(s)
    return finalstories                



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    # TODO: Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    
    
    triggersDic = {}
    configuration = []
    for line in lines:
        #print(lineCopy)
        trig = line[:].split(",")
        
        if trig[0] == "ADD":
            for i in trig[0:]:
                configuration.append(triggersDic[i])
        else:
            if trig[1] == "TITLE":
                triggersDic[trig[0]] = TitleTrigger(trig[2])
            elif trig[1] == "DESCRIPTION":
                triggersDic[trig[0]] = DescriptionTrigger(trig[2])
            elif trig[1] == "AFTER":
                triggersDic[trig[0]] = AfterTrigger(trig[2])
            elif trig[1] == "BEFORE":
                triggersDic[trig[0]] = BeforeTrigger(trig[2])
            elif trig[1] == "AND":
                triggersDic[trig[0]] = AndTrigger(trig[2],trig[3])
            elif trig[1] == "OR":
                triggersDic[trig[0]] = OrTrigger(trig[2],trig[3])
            elif trig == "NOT":
                triggersDic[trig[0]] = NotTrigger(trig[1])
                
                
                
            
                
            
                
        
    # print(lines) # for now, print it so you see what it contains!



SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("biden")
        t2 = DescriptionTrigger("biden")
        t3 = DescriptionTrigger("biden")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t2]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        # triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

