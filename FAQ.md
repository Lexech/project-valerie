

---

# Installation #
### How can I install PVMC? ###
Installation of PVMC can be done by simply installing an IPK-package. A step-by-step installation guide can be found [here](EasyInstallation#Installation_of_Project_Valerie.md).

### How can I uninstall PVMC? ###
In order to remove Project Valerie please check the steps described [here](EasyInstallation#Remove_of_Project_Valerie.md).

### What is the PVMC Web-Interface and how can I access it? ###
The Web-Interface (a.k.a. WebIf) offers an easy way to configure PVMC. Additionally it's possible to edit video details (e.g. edit plots, adapt titles or exchange poster and backdrops etc.). Please have a look [here](WebIF.md) in order to find out, how to use the WebIf.

### How do I specify where to search for videos? ###
This can be done by either using the Enigma2-GUI of PVMC - or more easily and much more comfortable by using the [Web-Interface](WebIF.md): "start page of WebIf" => "Options" => "Sync Settings". There you can specify the search path under "Path Settings".

### Can I use a folder located on an external drive or NAS for the Poster / Backdrops? ###
This can be done by either using the Enigma2-GUI of PVMC - or more easily and much more comfortable by using the [Web-Interface](WebIF.md): "start page of WebIf" => "Options" => "Global Settings". There you can specify the directory under "EXPERT Valerie Medienverzeichnis (Poster, Hintergründe):".

### How can I get that animated main menu working? ###
The configuration of the animated main menu is described [here](skin#Animated_Main-Menu.md).

### How can I configure and use the sub-title feature? ###
It is possible to display subs for videos. The configuration and usage is described [here](subtitles.md).

### The installation worked well - but the GUI looks ugly! ###
PVMC uses the native resolution of Enigma2 - perhaps the resolution specified there is not the correct one?
<br>
<br>
<h1>Synchronization</h1>
<h3>What is the purpose of "synchronization"?</h3>
PVMC differs from a "regular" video player by additional display of several information for each video, for example poster, plot air date or genre. Since all of these information can not be retrieved by from the video file itself PVMC has to "somehow" detect the video and afterwards the above listed info has to be downloaded from the internet. The whole described workflow is called "synchronization". In case a video has been successfully parsed the information is stored in a local database in order to have it available later on.<br>
<br>
<h3>How is the synchronization working in detail?</h3>
Details on synchronization will be described later on in the wiki. For now please consider the following points in order to get a good detection rate:<br>
<ul><li>PVMC uses several online databases in order to download the above mentioned additional information for videos (=> for details please see <a href='Sync#Media_provider.md'>here</a>).<br>
</li><li>prior downloading additional video information a video file has to be identified uniquely<br>
</li><li>the search string used is either the file name of the video file or - in case of Enigma2 recordings - the content of the so-called Enigma2 metafiles, where Enigma2 stores data from the EPG of the related show<br>
</li><li>in order to remove extra characters from the file name that might disturb the video detection (for example "<i>" in the filename or strings like "DVD_rip", "1080" etc.) it is possible to remove such stuff by using <a href='Sync#Regular_expressions.md'>regular expressions</a>
Problems may occur for example in case of remakes that use the same tile for different movies - or in case the first search result is a totally different video. Another source of potential errors during media detection are the already mentioned information contained in the Enigma2 metafiles: unfortunately no standard exists for these files so it's sometimes hard for PVMC to detect a recorded video.</li></ul></i>

PVMC offers several possibilities described <a href='Sync#Fix_wrong_parsed_media.md'>here</a> to fix wrong detected videos.<br>
<br>
Additionally it's possible to give PVMC "search hints" in order to detect the correct video - the different ways of doing things are described <a href='Sync#Excludes_and_search_hints.md'>here</a>, for example it's possible to provide the correct IMDb-ID in the filename. In case of Enigma2 recordings it's additionally possible to adapt the previously mentioned meta files in order to correct the contained information - but in that case other Enigma2 applications might have problems to evaluate these files.<br>
<br>
<h3>How do I start the synchronization?</h3>
Currently the synchronization can only be started using the <a href='Sync#Synchronisation.md'>PVMC Enigma2 GUI</a>. In future releases it may also be possible to start it from the web interface.<br>
<br>
<h3>How are the file information get stored?</h3>
The additional information of a detected movie get stored in a local database. See also <a href='Resources#Database_files.md'>here</a>.<br>
<br>
<h3>I have Microsoft Access / TOAD / SQLTalk / ... can I use it to edit the database?</h3>
No - it's not possible to manually edit the database files in a useful way. Please use the edit options provided by PVMC in order to fix the cause, why a special movie has not been detected correctly, for example by trying one of the solutions described <a href='Sync#Excludes_and_search_hints.md'>here</a>).<br>
<br>
<h3>There are several wrong / not detected videos in my movie list!</h3>
This may happen because of:<br>
<ul><li>there's no entry in the corresponding online database. For movies we use <a href='http://www.imdb.de/'>IMDb</a> and <a href='http://www.themoviedb.org'>TheMovieDb</a> - for TV-Shows <a href='http://www.thetvdb.com'>TheTvDb</a> => in that case the easiest way to fix things would be, to register a free account and to add that video so PVMC can retrieve the information with the next synchronization run<br>
</li><li>the search string PVMC builds out of filename or Enigma2 meta file results in multiple hits. In that case PVMC uses the first result (and that may be the wrong one). In that case just read the <a href='Sync#Excludes_and_search_hints.md'>chapter describing the available search hints</a> or correct the result using the WebIf.</li></ul>

<h3>Most movies are detected correctly but the plot uses the wrong language!</h3>
if that happens for ALL videos then the synchronization language might be configured wrong ( => see <a href='Sync#Settings.md'>sync settings</a>). Another cause might be, that for these movies no plot in the desired language are available at <a href='http://www.themoviedb.org'>TheMovieDb</a> / <a href='http://www.thetvdb.com'>TheTvDb</a>. In that case just register a free account and add the plots in your language.<br>
<br>
<h3>Most movies are detected correctly, but the covers are in a different language!</h3>
That happens very often and currently there's nothing we can do about that. The cause for that is simply: previously in the online databases used by PVMC (<a href='http://www.themoviedb.org'>TheMovieDb</a> / <a href='http://www.thetvdb.com'>TheTvDb</a>) the poster were not stored depending on their language. This "attribute" has been added just several months ago. Hence all "old" posters added right from the start have no language setting at all! (language is set to "none"). In that case it's possible to replace the poster using the web interface by either a local one. Additionally it's also possible to specify the URL of a different one.<br>
<br>
<h3>Is it possible to edit a plot or to add an own one?</h3>
This is possible by using the web interface. Besides the plot several more attributes can be edited!<br>
<br>
<h3>I own several documentations and video recordings not contained in IMDb. Is it possible to manage them in PVMC, too?</h3>
Currently it's possible to specify at least attributes like title, plot, genre etc. by using an nfo-file (similar to the ones used by XBMC). A major drawback of that solution is, that up to now it's not possible to specify the arts (e.g. poster and backdrops). More information on that can be found <a href='Sync#XBMC-style_nfo-files.md'>here</a>.<br>
<br>
<h3>Syncing takes very long - do I have to wait for the process to finish?</h3>
No, you don't have to! As soon as the synchronization has been started it's possible to leave the synchronization manager by pressing the "Exit" key on your remote control in order to watch the "live TV". As soon as the synchronization has been finished a message box shows up in order to inform you about the end of the synchronization.<br>
<br>
<br>
<h1>Playing videos</h1>
<h3>If I change from one movie to another in the movie list I hear some noise and it takes quite a while until the new backdrop is being displayed!</h3>
Please delete all poster and backdrops from the synchronization manager menu and perform a new synchronization run.<br>
<br>
<h3>My media collection is quite large - can I filter the movie list by genres?</h3>
Yes - it's possible to display for example only "horror" movies. This can be achieved by performing a "long" press on the green key in order to get a selection box where all available genres are listed.<br>
<br>
<h3>My media collection is quite large - can I filter the movie list by starting letter of the title?</h3>
That's also possible - just press the number keys in order to get the desired letter. In order to clear the filter and to see all entries again just press the "1" key.<br>
<br>
<h3>Can I change the sort order of the movie list?</h3>
The default sort criteria for the entries in the movie list is "name of title", but it's possible to sort the movie list by different criteria, for example according to "aired" date or "file-creation" date. Just click the "red" key to switch sorting.<br>
<br>
<h3>A specific movie doesn't get played by PVMC!</h3>
PVMC doesn't come with its own movie player but utilizes the Enigma2 media player instead. Hence if some videos didn't get played-back correctly by PVMC the first step should be to check, whether this video is played correctly by the Enigma2 media player. If that doesn't succeed either then it's most probably a problem of the used video file in combination with the codecs installed on your box. Next step could be to check the file on your local PC, but please keep in mind, that your PC uses different codecs than your box!<br>
<br>
If your Enigma2 movie player is able to play the movie correctly then please open a bug report so we can have a closer look at this.<br>
<br>
<h3>The playback of a video jerks badly!</h3>
Since PVMC just uses the Enigma2 movie player there's not much we can do about it. In order to track down the issue please see also the previous chapter!<br>
<br>
<h3>How do I rewind / fast-forward?</h3>
Since PVMC utilizes the Enigma2 movie player you can just use the "usual" keys: "1", "4" und "7" Tasten (=> rewind) and "3", "6" und "9" keys for fast-forward.<br>
<br>
<br>
<h1>Help / support</h1>
<h3>What can I do in case of problems with PVMC?</h3>
In case of synchronization problems it is suggested to read the <a href='Sync#Synchronisation.md'>corresponding wiki pages</a>. Especially the chapter regarding <a href='Sync#Excludes_and_search_hints.md'>search hints</a> might be helpful in order to "guide" PVMC to the correct video. In case of all other problems, e.g. crashes or problems while using the web interface it is possible to check for example the linked <a href='http://www.i-have-a-dreambox.com/wbb2/thread.php?threadid=144265'>PVMC discussion thread</a> in order to submit your problem. But please consider the following points:<br>
<ul><li>general questions like "xyz doesn't work for me" are not very helpful, since at least your box and the used PVMC version should be mentioned<br>
</li><li>for crashes it's additionally important to know the exact steps you use in order to get the crash, since in the meanwhile several options exist to perform a specific action (either for example using the PVMC Enigma2 GUI or using the web interface)<br>
</li><li>finally the PVMC log file might be helpful - and, in case of crashes, additionally the Enigma2 crash log. Both types of log files can be obtained by using the web interface (see next question))<br>
Since the above mentioned discussion thread is frequently used it might happen that the a question doesn't get recognized. In that case it is suggested to open a bug report, but please avoid duplicate issues by first checking whether a corresponding issue for your problem already exists.</li></ul>

<h3>From where do I get the log files?</h3>
There are two different kind of logs that might be helpful for tracking down issues: first the so-called "Valerie"-log created by PVMC itself and next the Enigma2 crashlog, which is created by Enigma2 in case a crash / green screen occurred.<br>
<br>
Both logs can be displayed using the web interface: "WebIf Home" => "Logs" => "Valerie" or "Enigma2". Please keep in mind: both lists are sorted by date ascending, which means the latest log entry is contained at the end of the list.<br>
<br>
<b>Please consider the following points:</b>
<ul><li>in order to ease the problem tracking the debug mode for the valerie log should be set to "High". This mode can be configured using the web interface as follows: "WebIf Home" => "Options" => "Global Settings" => "<code>[Expert]</code> Valerie Debug Modus" - and afterwards clicking the <code>[Save]</code> button! Afterwards you'll have to restart Enigma2 in order to finally create a new log using that new debug mode!<br>
</li><li>additionally it's important to know that with each Enigma2 restart a new valerie log gets created! If you encounter for example a crash during the synchronization process and Enigma2 restarts automatically after a crash you'd need to check the previous logfile for possible information regarding the crash!</li></ul>

<h3>What's the difference between "Valerie-Log" and "E2-Crashlog"?</h3>
The valerie log mainly contains useful information while starting-up and running. Additionally in case of synchronization PVMC adds information related to the search strings used in order to identify the medias. By evaluating this log in case of sync problems one can check why PVMC doesn't detect the "correct" videos.<br>
<br>
The Enigma2 crashlog contains information why an Enigma2 application crashed. Thus it's nothing special of PVMC, but may be useful in the (rare ;-)  ) case of an PVMC crash...<br>
<br>
<h3>I already asked a question several times in the IHaD-Forum - but didn't get an answer!</h3>
Most probably there's nothing offending about that - instead it's very likely, that the forum was very busy and your question got lost. If the reason for your question was a crash / bug / special question, then just open a bug report (see below).<br>
<br>
Another possibility would be, that (currently) no-one has a clue about your specific problem / question - or it's not that easy to reproduce your problem (because of different hardware etc.).<br>
<br>
As a general rule it is supposed to give as much information as possible - also in the forum, for example used PVMC version, used hardware and performed steps prior the problem occurred.<br>
<br>
<h3>How can I open a bug report?</h3>
"Project Valerie Media Center" is hosted on Google Code. Besides the <a href='http://code.google.com/p/project-valerie/wiki/Welcome'>Wiki</a> and the <a href='http://code.google.com/p/project-valerie/downloads/list'>downloads</a> this platform offers additionally the possibility to <a href='http://code.google.com/p/project-valerie/issues/entry?template=Defect%20report%20from%20user'>report errors</a>, <a href='http://code.google.com/p/project-valerie/issues/entry?template=Question%20from%20user'>to ask questions</a> and to suggest <a href='http://code.google.com/p/project-valerie/issues/entry?template=Enhancement%20report%20from%20user'>enhancement and feature requests</a> for upcoming PVMC releases.<br>
<br>
In case of reporting errors please ensure that you really mentioned the used PVMC version and described all steps necessary in order to reproduce your problem. Additionally both valerie log and (if applicable) Enigma2 crash log have to be added!