'''
Created on 15.07.2010

@author: i7
'''

import os
import codecs
from datetime import date
from MediaInfo import MediaInfo

class Database(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.dbMovies = {}
        self.dbSeries = {}
        self.dbEpisodes = {}
        
        self.duplicateDetector = []
        
    def reload(self):
        self.dbMovies = {}
        self.dbSeries = {}
        self.dbEpisodes = {}
        
        self.duplicateDetector = []
        
        self.load()
        
    def checkDuplicate(self, path, filename, extension):
        pth = path + "/" + filename + "." + extension
        pth = pth.replace("\\", "/")
        #print pth
        return pth in self.duplicateDetector
                
    def add(self, media):
        
        if media.isMovie or media.isEpisode:
            media.Path = media.Path.replace("\\", "/")
            if self.checkDuplicate(media.Path, media.Filename, media.Extension):
                return None
            else:
                pth = media.Path + "/" + media.Filename + "." + media.Extension
                self.duplicateDetector.append(pth)
        
        if media.isMovie:
            self.dbMovies[media.ImdbId] = media
        elif media.isSerie:
            if self.dbSeries.has_key(media.TheTvDbId) is False:
                self.dbSeries[media.TheTvDbId] = media
        elif media.isEpisode:
            if self.dbEpisodes.has_key(media.TheTvDbId) is False:
                self.dbEpisodes[media.TheTvDbId] = {}
            
            if self.dbEpisodes[media.TheTvDbId].has_key(media.Season) is False:
                self.dbEpisodes[media.TheTvDbId][media.Season] = {}
            
            self.dbEpisodes[media.TheTvDbId][media.Season][media.Episode] = media

    def __str__(self):
        return  "dbMovies: " + \
                "\n\t" + unicode(self.dbMovies) + \
                "\ndbSeries: " + \
                "\n\t" + unicode(self.dbSeries) + \
                "\ndbEpisodes: " + \
                "\n\t" + unicode(self.dbEpisodes) + \
                "\n\n" 

    def save(self):
        f = open("/hdd/valerie/moviedb.txt", 'wb')
        print "a"
        f.write(unicode(date.today()))
        print "b"
        for key in self.dbMovies:
            f.write(self.dbMovies[key].export().encode( "utf-8" ))
            self.dbMovies[key].setValerieInfoLastAccessTime(self.dbMovies[key].Path)
        print "c"
        f.close()
        
        f = open("/hdd/valerie/seriesdb.txt", 'wb')
        print "a"
        f.write(unicode(date.today()))
        print "b"
        for key in self.dbSeries:
            if self.dbEpisodes.has_key(key): # Check if we have episodes for that serie
                f.write(self.dbSeries[key].export().encode( "utf-8" ))
        print "c"
        f.close()
        
        for serie in self.dbEpisodes:
            f = open("/hdd/valerie/episodes/" + serie + ".txt", 'wb')
            print "a"
            f.write(unicode(date.today()))
            print "b"
            for season in self.dbEpisodes[serie]:
                for episode in self.dbEpisodes[serie][season]:
                    f.write(self.dbEpisodes[serie][season][episode].export().encode( "utf-8" ))
                    self.dbEpisodes[serie][season][episode].setValerieInfoLastAccessTime(self.dbEpisodes[serie][season][episode].Path)
            print "c"
            f.close()

    def load(self):
        try:
            db = codecs.open("/hdd/valerie/moviedb.txt", "r", "utf-8").read()[:-1]
            movies = db.split("\n----END----\n")
            for movie in movies:
                movie = movie.split("---BEGIN---\n")
                if len(movie) == 2: 
                    m = MediaInfo("","","")
                    m.importStr(movie[1], True, False, False)
                    path = unicode(m.Path) + "/" + unicode(m.Filename) + "." + unicode(m.Extension)
                    
                    if os.path.isfile(path) and m.getValerieInfoAccessTime(m.Path) == m.getValerieInfoLastAccessTime(m.Path):
                        self.add(m)
                    else:
                        print path
        except Exception, ex:
            print ex
        
        try:
            db = codecs.open("/hdd/valerie/seriesdb.txt", "r", "utf-8").read()[:-1]
            movies = db.split("\n----END----\n")
            for movie in movies:
                movie = movie.split("---BEGIN---\n")
                if len(movie) == 2: 
                    m = MediaInfo("","","")
                    m.importStr(movie[1], False, True, False)
                    self.add(m)
        except Exception, ex:
            print ex
            
        try:    
            for key in self.dbSeries:
                db = codecs.open("/hdd/valerie/episodes/" + key + ".txt", "r", "utf-8").read()[:-1]
                movies = db.split("\n----END----\n")
                for movie in movies:
                    movie = movie.split("---BEGIN---\n")
                    if len(movie) == 2: 
                        m = MediaInfo("","","")
                        m.importStr(movie[1], False, False, True)
                        path = unicode(m.Path) + "/" + unicode(m.Filename) + "." + unicode(m.Extension)
                        if os.path.isfile(path) and m.getValerieInfoAccessTime(m.Path) == m.getValerieInfoLastAccessTime(m.Path):
                            self.add(m)
                        else:
                            print path
        except Exception, ex:
            print ex
            
        #print self.duplicateDetector