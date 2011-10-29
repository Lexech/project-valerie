##############################################################################
# THIS FILE HAS ALL CLASSES AND FUNCTION THAT ARE NEEDED FOR THE WEBIF
# TO PROVIDE NONE CLICKABLE SUB-ACTIONS
##############################################################################

from urllib import urlencode
from Components.config import config
from twisted.web.resource import Resource

from Plugins.Extensions.ProjectValerie.__common__ import printl2 as printl
from Plugins.Extensions.ProjectValerie.DMC_Global import Update
from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_WebInterfaceExtras.core.WebData import WebData
from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_WebInterfaceExtras.core.WebHelper import WebHelper

import os
#------------------------------------------------------------------------------------------

# +++ LAZY IMPORTS +++
Manager = None
MediaInfo = None
utf8ToLatin = None
MediaInfo = None
MobileImdbComProvider = None
# --- LAZY IMPORTS ---

##########################
# CLASS:
##########################
class MediaForm(Resource):
	def render_GET(self, request):
		return self.action(request)

	def render_POST(self, request):
		return self.action(request)
	
	def action(self, request):
		global MediaInfo
		if MediaInfo is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.MediaInfo import MediaInfo
		global utf8ToLatin
		if utf8ToLatin is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.Utf8 import utf8ToLatin
		global Manager
		if Manager is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.Manager import Manager
		
		finalOutput = WebHelper().getHtmlCore("MediaInfo", True)
		
		Id = None
		ParentId = None
		imdbId = u""
		theTvDbId = u""
		currentMode = request.args["mode"][0]
		if "type" in request.args:
			type = request.args["type"][0]
		else:
			type = u""
			
		#######################
		# DONE MODE
		#######################
		if currentMode == "showDoneForm" :
			
			return finalOutput
		
		#######################
		# ERROR MODE
		######################
		elif currentMode == "showErrorForm":
			
			return finalOutput
		
		#######################
		# EDIT MODE
		#######################
		elif currentMode == 'showEditForm':
			nextMode = "alterMediaInDb"
			finalOutput = finalOutput.replace("<!-- CUSTOM_TITLE -->", " - Edit Media")
			Id = request.args["Id"][0]
			m = self._getMediaDetails(type, int(Id))
		
		#######################
		# ADDBYIMDB MODE
		#######################
		elif currentMode == 'showAddByImdbForm':
			fileData = None
			if "Id" in request.args:
				if request.args["Id"][0] == "":
					nextMode = "addMediaToDb"
				else:
					printl("ID => " + request.args["Id"][0], self, "D")
					nextMode = "alterMediaInDb"
					fileData = self._getMediaDetails(type, int(request.args["Id"][0]))
			else:
				nextMode = "addMediaToDb"
				
			finalOutput = finalOutput.replace("<!-- CUSTOM_TITLE -->", " - Add Media")
			m = MediaInfo()
			m.ImdbId = "";
			m.SearchString = "";
			if type == "isEpisode":
				type = "isSerie" # we need to do this because Manger.syncelemnts uses this name not the name till now isTvShow
			
			if fileData is not None:
				path = fileData.Path
				filename = fileData.Filename
				extension = fileData.Extension
			else:
				path = u"test"
				filename = u"test"
				extension = u"test"
				
			if type == "isMovie":
				m.ImdbId = request.args["ImdbId"][0]
				printl("showAddByImdbForm: "+str(request.args["ImdbId"][0]) + " " + str(type))
				syncData = Manager().syncElement(path, filename, extension, m.ImdbId, False)
				m = syncData[0]
			
			if type == "isSerie":
				m.ImdbId = request.args["ImdbId"][0]
				printl("showAddByImdbForm: "+str(request.args["ImdbId"][0]) + " " + str(type))
				syncData = Manager().syncElement(path, filename, extension, m.ImdbId, True)
				m = syncData[0]
		
		#######################
		# ADDBYTITLE MODE
		#######################				
		elif currentMode == 'showAlternativesForm':
			nextMode = "showAddByImdbForm"
			finalOutput = finalOutput.replace("<!-- CUSTOM_TITLE -->", " - Add Media")	
			mediainfo.SearchString = request.args["Title"][0]
			results = Manager().searchAlternatives(mediainfo)			
		
		if "Id" in request.args:
			Id = request.args["Id"][0]
		else:
			Id = u""		
			
		if "ParentId" in request.args:
			ParentId = request.args["ParentId"][0]
		else:
			ParentId = u""

		image = u""
		backdrop = u""
		mediaFolderPath = config.plugins.pvmc.mediafolderpath.value
		
		
		mediaForm = WebHelper().getHtmlForm("mediaForm")
		
		#######################
		# ADD MODE
		#######################	
		if currentMode=="showManualAddForm":
			nextMode = "addMediaToDb"
			mediaForm = mediaForm % (type, nextMode ,u"", ParentId, type, u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", u"", 0)
		else:
			if type == "isMovie":
				if os.path.isfile(mediaFolderPath + m.ImdbId + "_poster_195x267.png"):
					image = """<img id="duck_img" src="%s" width="78" height="107" alt="n/a"></img>""" % ("/media/" + m.ImdbId + "_poster_195x267.png")
				else:
					image = """<img src=\"http://val.duckbox.info/convertImg2/poster/%s_195x267.png\" width="78" height="107" alt="n/a"></img>""" % (m.ImdbId)
				
				if os.path.isfile(mediaFolderPath + m.ImdbId + "_backdrop_320x180.png"):
					backdrop = """<img id="duck_backdrop_img" src="%s" width="160" height="90" alt="n/a"></img>""" % ("/media/" + m.ImdbId + "_backdrop_320x180.png")
				else:
					backdrop = """<img src=\"http://val.duckbox.info/convertImg2/backdrop/%s_320x180.png\" width="160" height="90" alt="n/a">""" % (m.ImdbId)
				
				
			elif type == "isTvShow" or type == "isEpisode":
				if os.path.isfile(mediaFolderPath + m.TheTvDbId + "_poster_195x267.png"):
					image = """<img id="duck_img" src="%s" width="78" height="107" alt="n/a"></img>""" % ("/media/" + m.TheTvDbId + "_poster_195x267.png")
				else:
					image = """<img src=\"http://val.duckbox.info/convertImg2/poster/%s_195x267.png\" width="78" height="107" alt="n/a"></img>""" % (m.TheTvDbId)
				
				if os.path.isfile(mediaFolderPath + m.TheTvDbId + "_backdrop_320x180.png"):			
					backdrop = """<img id="duck_backdrop_img" src="%s" width="160" height="90" alt="n/a"></img>""" % ("/media/" + m.TheTvDbId + "_backdrop_320x180.png")
				else:
					backdrop = """<img src=\"http://val.duckbox.info/convertImg2/backdrop/%s_320x180.png\" width="160" height="90" alt="n/a">""" % (m.TheTvDbId)
			
			seenCheck = ""
			
			if m.Seen == "1":
				seenCheck = "checked"
			printl("nextMode = " + nextMode, self, "W")
			
			if m.ParentId == None:
				m.ParentId = u""

			mediaForm = mediaForm % (type, nextMode, Id, m.ParentId, type, Id, m.ImdbId, m.TheTvDbId, m.Title, m.Tag, m.Season, m.Disc, m.Episode, m.Plot, m.Runtime, m.Year, m.Genres, self._getPopularity(m.Popularity), m.Path, m.Filename, m.Extension, seenCheck)

		finalOutput = finalOutput.replace("<!-- CUSTOM_IMAGE -->", image)
		finalOutput = finalOutput.replace("<!-- CUSTOM_BACKDROP -->", backdrop)
		finalOutput = finalOutput.replace("<!-- CUSTOM_FORM -->", mediaForm)
	
		return utf8ToLatin(finalOutput)

	def _getPopularity(self, value):
		str = u""
		str += """<option value="">-- Select --</option>"""
		for i in range(1,11):
			if i==value:
				str += """<option value="%d" selected="yes">%d</option>""" % (i,i)
			else:
				str += """<option value="%d">%d</option>""" % (i,i)
		return str
		
	def _getMediaDetails(self, type, Id):
		data = WebData().getData("MediaInfo_" + type, Id)
		return data

##########################
# CLASS:
##########################
class Alternatives(Resource):
	def render_GET(self, request):
		return self.action(request)

	def render_POST(self, request):
		return self.action(request)
	
	def action(self, request):
		global utf8ToLatin
		global MediaInfo
		global MobileImdbComProvider
		
		if utf8ToLatin is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.Utf8 import utf8ToLatin
		if MediaInfo is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.MediaInfo import MediaInfo
		if MobileImdbComProvider is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.MobileImdbComProvider import MobileImdbComProvider
				
		finalOutput = WebHelper().getHtmlCore("Alternatives", True)
		
		tableHeader = WebHelper().readFileContent(u"/DMC_Plugins/DMC_WebInterfaceExtras/content/custom/Alternatives/Header.tpl")
		tableBody = u""
		
		mediainfo = MediaInfo()
		mediainfo.ImdbId = "";
		mediainfo.SearchString = "";

		mediainfo.SearchString = request.args["searchString"][0]
		entries = MobileImdbComProvider().getAlternatives(mediainfo)
		if entries is not None:
			for entry in entries:
				
				entry.type = request.args["type"][0]
				
				if "Id" in request.args:
					entry.Id = request.args["Id"][0]
				else:
					entry.Id = u""
	
				if "Path" in request.args:
					entry.Path = request.args["Path"][0]
				else:
					entry.Path = u""
				if "Filename" in request.args:
					entry.Filename = request.args["Filename"][0]
				else:
					entry.Filename = u""
				if "Extension" in request.args:
					entry.Extension = request.args["Extension"][0]
				else:
					entry.Extension = u""
			
			
				evtApply = self._getApplyAlternativeString(entry)
				
				tableBody += u"""   <tr>
									<td>%s</td>
									<td><a href=http://www.imdb.com/title/%s/ target="_blank">%s</a></td>
									<td>%s</td>
									<td>%s</td>
									<td>
										<a href="#" onclick="%s"><img class="action_img" src="/content/global/img/apply.png" alt="apply" title="apply" /></a>
									</td>
									</tr>
							""" % (entry.Year, entry.ImdbId, entry.ImdbId, utf8ToLatin(entry.Title), entry.IsTVSeries, evtApply)
			
		
		finalOutput = finalOutput.replace("<!-- CUSTOM_THEAD -->", tableHeader)
		finalOutput = finalOutput.replace("<!-- CUSTOM_TBODY -->", tableBody)
		
		return utf8ToLatin(finalOutput)
		
	############################################
	# HELPER:
	############################################
	def _getApplyAlternativeString (self, entry):
		onclick  = "javascript:window.open('/mediaForm?"
		onclick  += urlencode({'type':entry.type}) + "&"
		onclick  += urlencode({'mode':'showAddByImdbForm'}) + "&"
		onclick  += urlencode({'ImdbId':entry.ImdbId}) + "&"
		onclick  += urlencode({'Id':entry.Id})
		onclick  += "', '_self');"
		
		return onclick
		
##########################
# CLASS:
##########################	
class AddRecord (Resource):
	def render_GET(self, request):
		return self.action(request)

	def render_POST(self, request):
		return self.action(request)
	
	def action(self, request):
		global utf8ToLatin
		if utf8ToLatin is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.Utf8 import utf8ToLatin
		
		finalOutput = WebHelper().getHtmlCore("AddRecord", True)
	
		return utf8ToLatin(finalOutput)	
		
##########################
# CLASS:
##########################
class MediaActions(Resource):

	def render_GET(self, request):
		return self.action(request)

	def render_POST(self, request):
		return self.action(request)

	def action(self, request):
		global Manager
		global utf8ToLatin
		global MediaInfo
		if Manager is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.Manager import Manager
		if utf8ToLatin is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.Utf8 import utf8ToLatin
		if MediaInfo is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.MediaInfo import MediaInfo
		
		printl("request: " + str(request), self)
		printl("request.args: " + str(request.args), self)
		printl("request.args[mode]: " + str(request.args["mode"]), self)	
		
		##########################
		# ADD SECTION
		# Argument: 	request.args["mode"][0] 			== "addMediaToDb"
		# Subargument:  request.args["type"][0] 			== "isMovie" | "isTvShow" | "isEpisode"
		#				request.args["ParentId"][0] 		== Integer
		##########################
		if request.args["mode"][0] == "addMediaToDb":
			printl("mode (addMediaToDb)", self, "I")
			
			manager = Manager()	
			type = request.args["type"][0]
			parentId = request.args["ParentId"][0]
			
			key_value_dict = {}				
			for key in request.args.keys():
				key_value_dict[key] = request.args[key][0]
			
			# add movies
			if type == "isMovie":
				printl ("INSERT MOVIE : " + str(key_value_dict), self, "I")
				result = manager.insertMedia(Manager.MOVIES, key_value_dict)
				if result["status"] > 0:
					return WebHelper().redirectMeTo("/movies?mode=showDoneForm&showSave=true")
				else:
					return WebHelper().redirectMeTo("/mediaForm?mode=showErrorForm&type=isMovie&"+urlencode({'msg':result["message"]}))
			
			# add tvshows
			elif type == "isTvShow":
				printl ("INSERT TVSHOW : " + str(key_value_dict), self, "I")
				result = manager.insertMedia(Manager.TVSHOWS, key_value_dict)
				if result["status"] > 0:
					return WebHelper().redirectMeTo("/tvshows?mode=showDoneForm&showSave=true")	
				else:
					return WebHelper().redirectMeTo("/mediaForm?mode=showErrorForm&type=isTvShow&"+urlencode({'msg':result["message"]}))	
			
			# add tvshowepisodes
			elif type == "isEpisode":
				printl ("INSERT EPISODE: " + str(key_value_dict), self, "I")
				result = manager.insertMedia(Manager.TVSHOWSEPISODES, key_value_dict)				
				if result["status"] > 0:
					return WebHelper().redirectMeTo("/episodes?mode=showDoneForm&ParentId=" + parentId + "&showSave=true")
				else:
					return WebHelper().redirectMeTo("/mediaForm?mode=showErrorForm&type=isEpisode&ParentId=" + parentId + "&"+urlencode({'msg':result["message"]}))
		
		##########################
		# EDIT SECTION	
		# Argument: 	request.args["mode"][0] 		== "alterMediaInDb"
		# Subargument:  request.args["type"][0] 		== "isMovie" | "isTvShow" | "isEpisode"
		#				request.args["Id"][0]			== Integer
		#				request.args["ParentId"][0]		== Integer
		##########################
		elif request.args["mode"][0] == "alterMediaInDb":
			printl("mode (alterMediaInDb)", self, "I")
			
			manager = Manager()
			type = request.args["type"][0]
			Id = request.args["Id"][0]
			parentId = request.args["ParentId"][0]
			
			key_value_dict = {}				
			for key in request.args.keys():
				key_value_dict[key] = request.args[key][0]
			
			if not "Seen" in request.args:
				key_value_dict["Seen"] = "0"
			
			# edit movies		
			if type == "isMovie":
				result = manager.updateMedia(Manager.MOVIES, key_value_dict)
				if result:
					return WebHelper().redirectMeTo("/movies?mode=showDoneForm&Id=" + Id + "&showSave=true")
				else:
					return WebHelper().redirectMeTo("/mediaForm?mode=showErrorForm&type=isMovie&Id=" + Id)
			
			# edit tvshows
			elif type == "isTvShow":
				result = manager.updateMedia(Manager.TVSHOWS, key_value_dict)
				if result:
					return WebHelper().redirectMeTo("/tvshows?mode=showDoneForm&Id=" + Id + "&showSave=true")
				else:
					return WebHelper().redirectMeTo("/mediaForm?mode=showErrorForm&type=isTvShow&Id=" + Id)
			
			# edit tvsshowepisodes
			elif type == "isEpisode":
				result = manager.updateMedia(Manager.TVSHOWSEPISODES, key_value_dict)
				if result:
					return WebHelper().redirectMeTo("/episodes?mode=showDoneForm&Id=" + Id + "&ParentId=" + parentId + "&showSave=true")
				else:
					return WebHelper().redirectMeTo("/mediaForm?mode=showErrorForm&type=isEpisode&ParentId="+  parentId + "&Id=" + Id)
		
		##########################
		# DELETE SECTION
		# Argument: 	request.args["mode"][0] 		== "deleteMediaFromDb"
		# Subargument:  request.args["Id"][0]		 	== Integer
		#				request.args["ParentId"][0] 	== Integer
		#				request.args["type"][0] 		== "isMovie" | "isTvShow" | "isEpisode"
		##########################
		elif request.args["mode"][0] == "deleteMediaFromDb":
			printl("mode (deleteMediaFromDb)", self, "I")
			
			manager = Manager()
			id = request.args["Id"][0]
			type = request.args["type"][0]
			parentId = request.args["ParentId"][0]
			
			#delete movie
			if type == "isMovie":
				result = manager.deleteMedia(Manager.MOVIES, id)
				if result:
					return WebHelper().redirectMeTo("/movies?mode=showDoneForm&showSave=true")
				else:
					return WebHelper().redirectMeTo("/mediaForm?mode=showErrorForm&type=isMovie")
				
			# delete tvshowepisodes
			elif type == "isEpisode":
				result = manager.deleteMedia(Manager.TVSHOWSEPISODES, id)
				if result:
					return WebHelper().redirectMeTo("/episodes?mode=showDoneForm&ParentId=" + parentId + "&showSave=true")
				else:
					return WebHelper().redirectMeTo("/mediaForm?mode=showErrorForm&tpye=isEpisode&ParentId=" + parentId)
				
			# delete tvshow		
			elif type == "isTvShow":
				result = manager.deleteMedia(Manager.TVSHOWS, id)
				if result:
					return WebHelper().redirectMeTo("/tvshows?mode=showDoneForm&showSave=true")
				else:
					return WebHelper().redirectMeTo("/mediaForm?mode=showErrorForm&type=isTvShow")
					
			# delete failed		
			elif type == "isFailed":
				result = manager.deleteMedia(Manager.FAILED, id)
				if result:
					return WebHelper().redirectMeTo("/failed?showSave=true")
				else:
					return WebHelper().redirectMeTo("/mediaForm?mode=showErrorForm&type=isTvShow")

		##########################
		# CHANGE ARTS SECTION
		# Argument: 	request.args["mode"][0] == "changeMediaArts"
		# Subargument:  request.args["Id"][0] == Integer
		#				request.args["type"][0] == "isMovie" | "isTvShow" | "isEpisode"
		#				request.args["media_type"][0] == "poster" | "backdrop"
		#				request.args["media_source"][0] == String
		##########################
		elif request.args["mode"][0] == "changeMediaArts":
			printl("mode (changeMediaArts)", self, "I")
			
			manager = Manager()
			type = request.args["type"][0]
			media_source = request.args["media_source"][0]
			media_type = request.args["media_type"][0]
			Id = request.args["Id"][0]
			
			#change movie art
			if type == "isMovie":
				t = Manager.MOVIES
			
			#change tvshow art
			elif type == "isTvShow":
				t = Manager.TVSHOWS
			
			#change episode art
			elif type == "isEpisode":
				t = Manager.TVSHOWSEPISODES
			
			else:
				return utf8ToLatin("error")
			
			if media_type == "poster":
				result = manager.changeMediaArts(t, Id, True, None, media_source)
				if result == True:
					return utf8ToLatin("success")
				else:
					return utf8ToLatin("error")
			
			elif media_type == "backdrop":
				result = manager.changeMediaArts(t, Id, True, media_source, None)
				if result == True:
					return utf8ToLatin("success")
				else:
					return utf8ToLatin("error")
			else:
				printl("no media type found", self)
				return utf8ToLatin("error")
			
			return utf8ToLatin("error")

		##########################
		# SAVE TO DB
		# Argument: 	request.args["mode"][0] == "saveChangesToDb"
		##########################
		elif request.args["mode"][0] == "saveChangesToDb":
			printl("mode (saveChangesToDb)", self, "I")
			
			manager = Manager()
			manager.finish()
			
			if request.args["return_to"][0] == "movies":
				return WebHelper().redirectMeTo("/movies")
			
			elif request.args["return_to"][0] == "tvshows":
				return WebHelper().redirectMeTo("/tvshows")
			
			elif request.args["return_to"][0] == "episodes":
				return WebHelper().redirectMeTo("/episodes")
			
			elif request.args["return_to"][0] == "failed":
				return WebHelper().redirectMeTo("/failed")

##########################
# CLASS:
##########################
class WebFunctions(Resource):

	def render_GET(self, request):
		return self.action(request)

	def render_POST(self, request):
		return self.action(request)

	def action(self, request):
		global Manager
		global utf8ToLatin
		global MediaInfo
		if Manager is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.Manager import Manager
		if utf8ToLatin is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.Utf8 import utf8ToLatin
		if MediaInfo is None:
			from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.MediaInfo import MediaInfo
		
		printl("request: " + str(request), self)
		printl("request.args: " + str(request.args), self)
		printl("request.args[mode]: " + str(request.args["mode"]), self)	
		
		##########################
		# OPTIONS SECTION
		# Argument: 	request.args["mode"][0] 			== "options.saveconfig"
		#				request.args["what"][0]				== "settings_global" | "settings_sync"
		##########################
		if request.args["mode"][0] == "options.saveconfig":
			printl("mode (options.saveconfig)", self, "I")	
			
			what = request.args["what"][0]
			
			#settings_global
			if what == "settings_global":
				name = request.args["name"][0]
				value = "unchecked"
				if request.args.has_key("value"):
					value = request.args["value"][0]
				
				valueType = request.args["type"][0]
				
				printl("name=\"%s\" value=\"%s\" type=\"%s\"" % (name, value, valueType), self, "D")
				
				entries = WebData().getData("options.global")
				for entry in entries:
					if entry[0] == name:
						if valueType == "text" or valueType == "select":
							printl("Setting \"%s\" to \"%s\"" % (name, value), self, "I")
							entry[1].value = value
						elif valueType == "checkbox":
							if value == "checked" or value == "on":
								value = True
							else:
								value = False
							printl("Setting \"%s\" to \"%s\"" % (name, value), self, "I")
							entry[1].value = value
						entry[1].save()
			
			# settins_sync
			elif what == "settings_sync":
				printl("argument => what = settings_sync", self, "I")
				if request.args["section"][0] == "paths":
					printl("argument => section = path", self, "I")
					id = request.args["Id"][0]
					directory = request.args["directory"][0]
					typeFolder = request.args["type"][0]
					enabled = request.args.has_key("enabled")
					useFolder = request.args.has_key("usefolder")
					
					path = {"directory": directory, "enabled": enabled, "usefolder": useFolder, "type": typeFolder}
					
					from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.PathsConfig import PathsConfig
					PathsConfig().getInstance().setPath(id, path)
					PathsConfig().getInstance().save()
				
				elif request.args["section"][0] == "filetypes":
					printl("argument => section = filetypes", self, "I")
					value = request.args["value"][0]
					from Plugins.Extensions.ProjectValerie.DMC_Plugins.DMC_SyncExtras.PathsConfig import PathsConfig
					PathsConfig().getInstance().setFileTypes(value.split("|"))
					PathsConfig().getInstance().save()
			
			return WebHelper().redirectMeTo("/options")			
		
		##########################
		# DUMP DATABASE - view via webif http://url:8888/dumps
		# Argument: 	request.args["mode"][0] == "dumpDb"
		##########################
		elif request.args["mode"][0] == "dumpDb":
			printl("mode (dumpDb)", self, "I")
			
			Manager().getDbDump()
			return WebHelper().redirectMeTo("/dumps")	
			
		##########################
		# BACKUP SECTION
		# Argument: 	request.args["mode"][0] 			== "backupValerie"
		##########################
		elif request.args["mode"][0] == "backupValerie":
			printl("mode (backupValerie)", self, "I")
			
			import zipfile, os

			zipf = zipfile.ZipFile('/hdd/valerie-backup.zip', mode='w', compression=zipfile.ZIP_STORED )
			path = utf8ToLatin(config.plugins.pvmc.tmpfolderpath.value)
			WebHelper().recursive_zip(zipf, path)
			zipf.close()

			return WebHelper().redirectMeTo("/elog/valerie-backup.zip")	

		##########################
		# RESTORE SECTION - do not use for now fills up the flash => freeze
		# Argument: 	request.args["mode"][0] 			== "restoreValerie"
		# Information:	http://webpython.codepoint.net/cgi_file_upload
		##########################
		elif request.args["mode"][0] == "restoreValerie":
			printl("mode (restoreValerie)", self, "I")

			outputStream = open(filename, '/hdd/test.zip')
			outputStream.write(request.args['myFile'])
			outputStream.close()			
			