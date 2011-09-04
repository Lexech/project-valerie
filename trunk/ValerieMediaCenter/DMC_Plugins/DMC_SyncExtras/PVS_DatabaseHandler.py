# -*- coding: utf-8 -*-
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   PVS_DatabaseHandler.py
#   Project Valerie - Database Handler
#
#   Created by user on 01/01/1900.
#   Interface for working with databases
#   
#   Revisions:
#   v0.Initial - Zuki - renamed from database.py
#
#   v1 15/07/2011 - Zuki - minor changes to support SQL DB
#			 - Separate LoadALL in 3 processes (movies,series,failed)
#			 - Added Database requests to 
#   v2 18/07/2011 - Zuki - Added Counters for Movies/Series
#   v3 21/07/2011 - Zuki - Added new functions to access Series/Episodes 
##
################################################################################
# Function			Parameters		Return
################################################################################
# getMovies						dict of MediaInfo
# getMoviesValues					list of MediaInfo 
# getMoviesWithKey		movieKey		MediaInfo
# getMoviesPkWithImdb		ImdbID			ID
# getMoviesCount					Count
#
# getSeries						dict of MediaInfo
# getSeriesValues					list of MediaInfo
# getSeriesWithKey		serieKey		MediaInfo
# getSeriesPkWithTheTvDb	theTvDbId		ID
# getSeriesSeasons		serieKey		dict of MediaInfo
# getSeriesEpisodes		serieKey=None		list of MediaInfo
#				season=None
# getSeriesEpisode		serieKey,season,episode	MediaInfo
# getSeriesCount					Count
# getSeriesCountSeasons		serieKey		Count
# getEpisodesCount		mediaId,season		Count
#
# seriesDeleteCascadeOfSerie	serieKey		Boolean
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import cPickle   as pickle
from   datetime import date
import os
from threading import Lock
import time

from Components.config import config

import Config
import DirectoryScanner
from FailedEntry import FailedEntry
from MediaInfo import MediaInfo
import Utf8

from Plugins.Extensions.ProjectValerie.__common__ import printl2 as printl
from Plugins.Extensions.ProjectValerie.__common__ import log as log
	
DB_SQLITE_LOADED = False

try:
	from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.PVS_DatabaseHandlerSQL import databaseHandlerSQL
	from PVS_DatabaseHandlerSQL import databaseHandlerSQL
	DB_SQLITE_LOADED = True
	printl("PVS_DatabaseHandlerSQL Loaded    :) ", None, "W")	
except Exception, ex:
	printl("Exception: PVS_DatabaseHandlerSQL not Loaded :(   "+ str(ex), None, "W")
		
try:					   
	from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.PVS_DatabaseHandlerPICKLE import databaseHandlerPICKLE
	from PVS_DatabaseHandlerPICKLE import databaseHandlerPICKLE
	printl("PVS_DatabaseHandlerPICKLE Loaded :)", None, "W")
except Exception, ex:
	printl("Exception: PVS_DatabaseHandlerPICKLE not Loaded :(   "+ str(ex), None, "W")
		
try:
	from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.PVS_DatabaseHandlerTXD import databaseHandlerTXD
	from PVS_DatabaseHandlerTXD import databaseHandlerTXD
	printl("PVS_DatabaseHandlerTXD Loaded    :)", None, "W")
except Exception, ex:
	printl("Exception: PVS_DatabaseHandlerTXD not Loaded :(   "+ str(ex), None, "W")

#------------------------------------------------------------------------------------------

gDatabase = None
gDatabaseMutex = Lock()

class Database(object):
	DB_NONE   = 0
	DB_TXD    = 2
	DB_PICKLE = 3
	DB_SQLITE = 4

	DB_PATH   = config.plugins.pvmc.configfolderpath.value

	if DB_SQLITE_LOADED and os.path.exists(DB_PATH + "usesql"):
		USE_DB_TYPE    	= DB_SQLITE
	else:
		USE_DB_TYPE    	= DB_PICKLE
		
	USE_BACKUP_TYPE = DB_NONE  	# To do: will always backup to DB_PICKLE ????
	
	USE_INDEXES = False  		# Create indexes key/id
	PRELOADDB   = True  		# Reload All tables on Start (default)
	# NOTE: almost every queries to DB force to use all tables
	#  Examples:
	#  	 Count Records(webif)
	#  	 checkduplicates
	
	CONFIGKEY  = -999999
	
	def __init__(self):
		log("->", self, 10)
			
		if self.USE_DB_TYPE == self.DB_SQLITE:			
			self.dbHandler = databaseHandlerSQL().getInstance("from __init__")
			if self.dbHandler.DB_SQLITE_FIRSTTIME:
				printl("Sql FirstTime", self)					 
				self.importDataToSql()#.addCallback(self.ImportDone).addErrback(self.ImportError)

				self.dbHandler.DB_SQLITE_FIRSTTIME = False
					
		if self.USE_DB_TYPE == self.DB_PICKLE:			
			self.dbHandler = databaseHandlerPICKLE().getInstance()
		
		if self.USE_DB_TYPE == self.DB_TXD:
			self.dbHandler = databaseHandlerTXD().getInstance()
	
	def __str__(self):		
		try:
			rtv = unicode(self.getMoviesCount()) + \
					u" " + \
					unicode(self.getSeriesCount) + \
					u" " + \
					unicode(self.getEpisodesCount())
			return Utf8.utf8ToLatin(rtv)
		except Exception, ex:
			log("Error retriving _str_: "+ str(ex), self, 2)
			return "Error retriving _str_"			

	def importDataToSql (self):
		log("->", self, 10)
		try:
			printl("Importing Data", self)
			#self.preload()	# Load from PICKLE
			dbHandlerPickle = databaseHandlerPICKLE().getInstance()
			#dbHandlerSql 	= databaseHandlerSQL().getInstance("ImportDataToSql")
			self.dbHandler.overwriteDB(dbHandlerPickle.getMovies(),dbHandlerPickle.getSeries(),dbHandlerPickle.getSeriesEpisodes())
			
			self.save()  	# save to Database SQL
			try:
				pass #os.rename(self.DB_TXD, self.DB_TXD +'.'+ str(time.time()) + '.bak')
			except Exception, ex:
				printl("Backup movie txd failed! Ex: " + str(ex), __name__, "E")
		except Exception, ex:
			printl("Failed Import to SQL! Reloading Pickles Ex: " + str(ex), __name__, "E")
			self.dbHandler = databaseHandlerPICKLE().getInstance()
			#self.reload()	# Load from PICKLE
			

	def setDBType(self, version):
		self.USE_DB_TYPE = version
		log("DB Type set to " + str(version), self)

	def getDBTypeText(self):
		if self.USE_DB_TYPE == self.DB_TXD:
			return "TXD"
		elif self.USE_DB_TYPE == self.DB_PICKLE:
			return "Pickle"
		elif self.USE_DB_TYPE == self.DB_SQLITE:
			return "SQLite"
		else:
			return "No DB Type defined"

	def getInstance(self):
		log("->", self, 10)
		global gDatabase
		global gDatabaseMutex
		
		if gDatabase is None:
			printl("Acquiring Mutex", self, "W")
			gDatabaseMutex.acquire()
			try:
				printl("Creating new Database instance", self)				
				if self.PRELOADDB:
					self.preload()  # RELOAD ALLL 
					
				gDatabase = self
			finally:	
				gDatabaseMutex.release()
				printl("Released Mutex", self, "W")
		
		return gDatabase

	def preload(self):
		log("->", self, 10)
		self.dbHandler.loadAll()
		
	def deleteMissingFiles(self):
		log("->", self, 10)
		listMissing = []
		
		movies = self.getMoviesValues()
		log("test 1", self, 10)	
		for m in movies:
			path = m.Path + u"/" + m.Filename + u"." + m.Extension
			if os.path.exists(Utf8.utf8ToLatin(path)) is False:
				listMissing.append(m)
	
		#series = self.getSeries()
		episodes = self.getEpisodes()
		log("test 3", self, 10)
		#for key in series:
		#	if key in episodes:
		#		for season in episodes[key]:
		for m in episodes:
			path = m.Path + u"/" + m.Filename + u"." + m.Extension
			if os.path.exists(Utf8.utf8ToLatin(path)) is False:
				listMissing.append(m)
		
		printl("Missing: " + str(len(listMissing)), self)
		for m in listMissing:
			self.remove(m)

	def remove(self, media, is_Movie=False, is_Serie=False, is_Episode=False):
		printl("is Movie=" + str(media.isTypeMovie()) + " is Serie=" + str(media.isTypeSerie()) + " is Episode=" + str(media.isTypeEpisode()), self)

		return self.dbHandler.deleteMedia(media.Id)
	
	##
	# Adds media files to the db
	# @param media: The media file
	# @return: False if file is already in db or movie already in db, else True 
	def add(self, media):
		log("->", self, 10)
		#if media.MediaType == MediaInfo.FAILEDSYNC:
		#	nextID = len(self.dbFailed2)
		#	self.dbFailed2[nextID] = media			

		# Checks if a tvshow is already in the db, if so then we dont have to readd it a second time
		if media.isTypeSerie():
			return self.dbHandler.insertSerie(media)

		media.Path = media.Path.replace("\\", "/")
		# Checks if the file is already in db
		if self.checkDuplicate(media.Path, media.Filename, media.Extension) is not None:
			# This should never happen, this means that the same file is already in the db
			# But is a failure describtion here necessary ?
			return False
		
		#NOT USED
		#pth = media.Path + "/" + media.Filename + "." + media.Extension
		#self.duplicateDetector.append(pth)
		
		if media.isTypeMovie():
			return self.dbHandler.insertMovie(media)

		elif media.isTypeEpisode():
			return self.dbHandler.insertEpisode(media)

		return True

	def save(self):
		log("->", self, 10)
		global gDatabaseMutex
		printl("Acquiring Mutex", self, "W")
		gDatabaseMutex.acquire()
		try:
			printl("Acquired Mutex", self, "W")
			# Always safe pickel as this increses fastsync a lot
			
			# will be the backup
			#self.savePickel() 
			
			self.dbHandler.saveMovies()
			self.dbHandler.saveSeries()
			self.dbHandler.saveEpisodes()
			self.dbHandler.saveFailed()
			#self.dbHandler.saveFailed2(self.dbFailed2)
			return True
		except Exception, ex:
			printl("Failed Save! Ex: " + str(ex), __name__, "E")
			return False
		finally:	
			gDatabaseMutex.release()
			printl("Released Mutex", self, "W")
		
#
#################################   MEDIAS   ################################# 
#
	# DML statements
	#def insertMedia(self, media):
	#	return self.dbHandler.insertMedia(media)
	
	def insertMediaWithDict(self, key_value_dict):
		return self.dbHandler.insertMediaWithDict(key_value_dict)
	
	def updateMediaWithDict(self, key_value_dict):	#ID is Required
		return self.dbHandler.updateMediaWithDict(key_value_dict)
	
	def deleteMedia(self, id):
		return self.dbHandler.deleteMedia(id)

#
#################################   MOVIES   ################################# 
#
	def getDbDump(self):
		return self.dbHandler.getDbDump()
	
	def dbIsCommited(self):
		return self.dbHandler.dbIsCommited()
		
	def getMovies(self):
		return self.dbHandler.getMovies()

	def getMoviesValues(self, order=None, firstRecord=0, numberOfRecords=9999999):
		return self.dbHandler.getMoviesValues(order, firstRecord, numberOfRecords)	

	def getMovie(self, id):
		return self.dbHandler.getMovie(id)

	#def getMoviesPkWithImdb(self, imdbId):
	#	return self.dbHandler.getMovieKeyWithImdbId(imdbId)
		
	def getMoviesWithImdbId(self, imdbId):
		movieKey = self.dbHandler.getMovieKeyWithImdbId(imdbId)
		return self.dbHandler.getMoviesWithKey(movieKey)

	def getMoviesCount(self):
		return self.dbHandler.getMoviesCount()	
	
	def setMoviesSeen(self, id):
		return 	
#	
#################################   SERIES   ################################# 
#
	def getSeries(self, order=None, firstRecord=0, numberOfRecords=9999999):
		log("->", self, 15)
		return self.dbHandler.getSeries(order, firstRecord, numberOfRecords)
		
	def getSeriesValues(self, order=None, firstRecord=0, numberOfRecords=9999999):
		log("->", self, 15)
		return self.getSeries(order, firstRecord, numberOfRecords).values()
		
	def getSeriesWithKey(self, serieKey):
		return self.dbHandler.getSeriesWithKey(serieKey)	

	def getSeriesWithTheTvDbId(self, theTvDbId):
		Id = self.dbHandler.getSeriesIdWithTheTvDbId(theTvDbId)
		return self.dbHandler.getSerieWithId(Id)	
		
	def getSeriesCount(self):
		return self.dbHandler.getSeriesCount()
	#	
	######################   SEASONS   ######################
	#
	def getSeriesSeasons(self, serieKey):			
		return self.dbHandler.getSeriesSeasons(serieKey)				
	
	#def getSeasonsCount(self, mediaId): errr
	#	return self.dbHandler.getSeriesCountSeasonsWithKey(serieKey)

	#def getSeasonsCountWithTheTvDbId(self, theTvDbId):
	#	#Id = self.dbHandler.getSeriesIdWithTheTvDbId(theTvDbId)
	#	return self.dbHandler.getSeriesCountSeasons(theTvDbId)
	
	def getEpisodesCount(self, mediaId=None, season=None):
		return self.dbHandler.getEpisodesCount(mediaId, season)
		
	#def getEpisodesCountWithTheTvDbId(self, theTvDbId, season):
	#	id = self.dbHandler.getSeriesIdWithTheTvDbId(theTvDbId)
	#	return self.dbHandler.getEpisodesCount(id, season)
	
	def getSerie(self, id):
		return self.dbHandler.getSerieWithId(id)
	
	# DML statements
	def insertSerie(self, media):
		return self.dbHandler.insertSerie(media)

	def insertSerieWithDict(self, key_value_dict):
		return self.dbHandler.insertSerieWithDict(key_value_dict)

	def updateSerieWithDict(self, key_value_dict):		#ID is Required
		return self.dbHandler.updateSerieWithDict(key_value_dict)

	def deleteSerie(self, id):
		return self.dbHandler.deleteSerie(id)

#	
################################   EPISODES   ################################ 
#
	def getEpisodes(self, Id=None):
		return self.dbHandler.getEpisodes(Id)
		
	def getEpisodesWithKey(self, serieKey=None, season=None):
		return self.dbHandler.getEpisodesWithKey(serieKey, season)

	def getEpisodesWithTheTvDbId(self, theTvDbId, season=None):
		Id = self.dbHandler.getSeriesIdWithTheTvDbId(theTvDbId)
		return self.dbHandler.getEpisodes(Id, season)

#	def getSeriesEpisode(self, serieKey, season, episode):
#		return self.dbHandler.getEpisode(serieKey, season, episode)
	
	def getEpisode(self, id):
		return self.dbHandler.getEpisodeWithId(id)

	def insertEpisode(self, media):
		return self.dbHandler.insertEpisode(media)
	
	def insertEpisodeWithDict(self, key_value_dict):
		return self.dbHandler.insertEpisodeWithDict(key_value_dict)

	def updateEpisodeWithDict(self, key_value_dict):	#ID is Required
		return self.dbHandler.updateEpisodeWithDict(key_value_dict)

	def deleteEpisode(self, id):
		return self.dbHandler.deleteEpisode(id)
	
#	
#################################   FAILED   ################################# 
#
	def getFailed(self):
		return self.dbHandler.getFailed()

	def clearFailed(self):
		return self.dbHandler.deleteFailed()

	def addFailed(self, entry):
		return self.dbHandler.insertFailed(entry)

	def removeFailed(self, entry):
		return self.dbHandler.deleteFailed(entry)

	def getAddFailedCauseOf(self):
		try:
			cause = self.dbHandler._addFailedCauseOf
			if cause is None:
				return u"Error retriving Cause of Failed (cause Null)"
			self.dbHandler._addFailedCauseOf = None
			return cause.Path + u"/" + cause.Filename + u"." + cause.Extension
		except Exception, ex:
			log("Error retriving Cause of Failed: "+ str(ex), self, 2)
			return u"Error retriving Cause of Failed"
				
	
#
###################################  UTILS  ###################################
#
	##
	# Checks if file is already in the db
	# @param path: utf-8 
	# @param filename: utf-8 
	# @param extension: utf-8 
	# @return: True if already in db, False if not
	def checkDuplicate(self, path, filename, extension):
		return self.dbHandler.checkDuplicate(path, filename, extension)

	def transformGenres(self):
		self.dbHandler.transformGenres()
			


#	
############################################################################## 
#
	# NOT USED ???
	#def searchDeleted(self):
	#	log("->", self, 10)
	#	movies = self.getMovies()
	#
	#	for key in movies:
	#		m = movies[key]
	#		path = m.Path + u"/" + m.Filename + u"." + m.Extension
	#		if os.path.exists(Utf8.utf8ToLatin(path)) is False:
	#			printl(":-( " + Utf8.utf8ToLatin(path), self)
	#	
	#	series = self.getSeries()
	#	episodes = self.episodesGet()
	#	for key in series:
	#		if key in episodes:
	#			for season in episodes[key]:
	#				for episode in episodes[key][season]:
	#					m = episodes[key][season][episode]
	#					path = m.Path + u"/" + m.Filename + u"." + m.Extension
	#					if os.path.exists(Utf8.utf8ToLatin(path)) is False:
	#						printl(":-( " + Utf8.utf8ToLatin(path), self)

	#not tested
	#self.idxMoviesByImdb = {}
	#self.idxSeriesByTheTvDb = {}
	#def createMoviesIndexes(self):
	#	log("->", self, 10)
	#	start_time = time.time()
	#	self.idxMoviesByImdb = {}
	#	for key in self._dbMovies:
	#		if key != self.CONFIGKEY:		# only for Pickle
	#			self.idxMoviesByImdb[self._dbMovies[key].ImdbId] = key
	#	elapsed_time = time.time() - start_time
	#	log("Indexing Took : " + str(elapsed_time), self, 11)

	#not tested
	#def createSeriesIndexes(self):
	#	log("->", self, 10)
	#	start_time = time.time()
	#	self.idxSeriesByTheTvDb = {}
	#	for key in self._dbSeries:
	#		self.idxSeriesByTheTvDb[self._dbSeries[key].TheTvDbId] = key
	#	elapsed_time = time.time() - start_time
	#	printl("Indexing Took : " + str(elapsed_time), self)

	#def createSeriesIndexes(self):
	#	start_time = time.time()
	#	for key in self._dbSeries:
	#		self.idxSeriesByThetvdb[self._dbSeries[key].TheTvDbId] = key
	#	elapsed_time = time.time() - start_time
	#	printl("Indexing Took : " + str(elapsed_time), self)
