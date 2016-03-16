#summary Everything about synchronisation


---

# Synchronisation #
## Basics ##
PVMC differs from a "regular" video player mainly because of the fact, that for all the videos several additional information will be displayed on your TV while digging around your video collection - for example: movie poster, description / plot, release year or genre the video belongs to. Since this additional information can not be retrieved just from the video's file name and since PVMC has not the capability to somehow "analyze" the video content this information needs to be retrived from somewhere else - and in order to do so PVMC needs to somehow "identify" your locally stored video files. This (unique) process of ientifying your videos and retrieving the necessary information is called "synchronisation": if a video has been successfully identified and the related information has been successfully retrieved this data will be stored in a local database and can be displayed later on in the movie list without a new synchronisation run.

In order to understand why PVMC doesn't always manage it to identify 100% of your videos - or maybe sometimes identifies a wrong video - it's important to understand how the synchronisation process works in principle. This helps, to identify problems and to help PVMC by so-called "synchronisation hints" to identify your videos corrrectly with the next synchronisation run (see below).

As mentioned previously PVMC has to retrieve the additional video data from external sources. Hence it is necessary to have an active internet connection during any synchronisation run. The following online database are used as sources during a synchronisation run:
  * [IMDB.com](http://www.imdb.com) => used to retrieve the unique IMDb-ID (see below)
  * [TheMovieDB.org (TMDB)](http://www.themoviedb.org) => additionally for movies
  * [TheTVDB.org (TVDB)](http://www.thetvdb.org) => additionally for TV shows
These databases are free of charge and can be edited / enhanced with new movies and TV shows / episodes by creating a feee account!

**Please note**<br>
It is important to understand, that PVMC can sync only such movies that are contained in <b>both</b> IMDb.com and TheMovieDb.org databases. Similarly PVMC can only sync such TV shows that are contained in <b>both</b> databases IMDb.com and TheTvDb.com!<br>
<b>It is not sufficient, that for example a movie is contained in IMDb.com - but the corresponding entry in TheMovieDb is missing!</b><br>
In such a case the most easiest way is to create a free account for the corresponding database and to just add the needed information. This won't take long and you'll support the whole community by contributing some stuff!<br>
<br>
For the upcoming chapters and examples we use the following assumptions for the structure of our video collection:<br>
<br>
<pre><code><br>
/hdd/videos/movies/A_Beautiful_Mind.avi<br>
/hdd/videos/movies/Matrix.avi<br>
/hdd/videos/movies/TopGun.avi<br>
/hdd/videos/movies/X-Men.avi<br>
...<br>
/hdd/videos/tv/Breaking Bad/breaking_bad_s01e01_Titel.avi #Season #1 / Episode #1<br>
/hdd/videos/tv/Breaking Bad/breaking_bad_s01e02_Titel.avi #Season #1 / Episode #2<br>
...<br>
/hdd/videos/tv/Breaking Bad/breaking_bad_s02e01_Titel.avi #Season #2 / Episode #1<br>
/hdd/videos/tv/Breaking Bad/breaking_bad_s02e02_Titel.avi #Season #2 / Episode #2<br>
...<br>
/hdd/videos/tv/Criminal Minds/criminal_minds_s01e01_Titel.avi<br>
...</code></pre>
and so on.<br>
<br>
Of course there are countless ways on how a video collection can be structured and is ureley depends on the number of TV shows and movies one has, but my personal experience with the above described structure is quite good, so my best guess on that is, that it shouldn't be that bad.... :-)<br>
<br>
<h3>Synchronisation of movies</h3>
This chapter will describe the principle workflow while synchronizing our "movie" folder shown above - the upcoming chapter will then take a closer look on the synchronisation process of TV shows.<br>
<br>
Now for movies PVMC performs the following steps:<br>
<ul><li>the names of all files contained in that "movies" directory will be loaded<br>
</li><li>afterwards PVMC tries to detect, if those files represent a movie or a TV show. You know, that those are movies (at least you are supposed to do so ;-)  ) - but PVMC has only some indications, for example the folder type you specify in the synchronisation settings or the filename itself, which can be helpful by evaluating if the name contains some typical patterns used to enumerate season and episodes of TV show episodes (for example the typical "s01e01" or "1x01" stuff)<br>
</li><li>next PVMC will start a search at IMDb by using the filename of the video file - but prior starting the query we need to clean-up the video's filename from characters and strings usually used to indicate the video quality or the used audio / video codec (for example stuff like "h264", "720p", "1080i" or "1080p" and so on), since these might badly influence the search results at IMDb!<br>
</li><li>IMDb will then (hopefully) return a list of movies matching the words used in the search query - or an empty result set in case no movie was found that matches our search.<br>
</li><li>assuming that we do get a list of possible movies PVMC will then apply further plausibility checks and if a movie is assumed to be the correct one it takes the "famous" unique IMDb-ID out of that movie list.<br>
</li><li>this IMDb-ID is then used to retrieve Title, Plot, Poster and so on from TheMovieDB</li></ul>

As can be seen from the sreps above it mainly depends from the name of the video file whether the try to identify the "correct" movie will be successful or not: for example PVMC does not know, if the current video file contains to original film (from for example 1955) - or if the video file contains the remake from 1988, which has the same name. Another problem could rise, if the search at IMDb-ID returns multiple results and the correct movie is not listed at first place (and also the year information was missing in the file name).<br>
<br>
Now back to our sample video collection it is important to choose the correct folder type for both "movies" and "tv" in the synchronisation settings: the folder "movies" should be flagged as "MOVIE" and the folder "tv" should be flagged as "TV". In that case there's no need for the third folder type "MOVIE_AND_TV" since we strictly seperated movies and TV shows.<br>
<br>
For the first video file "<code>A_Beatiful_Mind.avi</code>" PVMC will assume a "movie" because the containing directory is of type "MOVIE". Next it is checked whether for this file some synchronisation hints exist or not, for example a <code>valerie.info</code> (see <a href='Sync#Excludes_and_search_hints.md'>"Excludes and search hints"</a>). Since we don't have any search hints the file name will be parsed in order to remove unnecessary phrases and characters that could disturb our upcoming search query. For example all "<code>_</code>" chars get replaced by " " and things like "divx" or "h.264" will be dropped. Finally an IMDb-Query with the following search string will be started:<br>
<br>
<blockquote>"a beautiful mind"</blockquote>

As a result we get a list with all videos available at IMDb matching that query. For heavens sake the "correct" film is located at position #1: "A beautiful mind" with Russell Crowe, released in 2001:<br>
<br>
<blockquote><a href='http://m.imdb.com/title/tt0268978/'>http://m.imdb.com/title/tt0268978/</a></blockquote>

In this link we find additionally the famous "IMDb-ID" of that movie: <code>tt0268978</code>. Now what would have happened, if our video in our collection would be the TV-Special "A Beautiful Mind: Creation of the Special Effects" released in 2002:<br>
<br>
<blockquote><a href='http://m.imdb.com/title/tt0780995/'>http://m.imdb.com/title/tt0780995/</a></blockquote>

?<br>
<br>
In that case we'd the video still sync as the movie "A beautiful mind", but by using the previously mentioned "search hints" it would be possible to guide PVMC to the correct IMDb-entry, for example by adding the correct IMDb-ID <code>tt0780995</code> to the file:<br>
<br>
<blockquote><code>/hdd/videos/filme/A_Beautiful_Mind_tt0780995.avi</code></blockquote>

Additional search hints are described more detailed in the upcoming chapter <a href='Sync#Excludes_and_search_hints.md'>"Excludes and search hints"</a>!<br>
<br>
Now back to our original example: we have found our movie "A beautiful mind" and get the correct IMDb-ID <code>tt0268978</code> from IMDb. Next we need to get "official" title, plot and poster / backdrop for that movie, which will be shown later on in the PVMC movie list. This is done by submitting a corresponding query to online database "TheMovieDB". The following attributes will then be loaded from there:<br>
<ul><li>the official title of the film<br>
</li><li>the release year<br>
</li><li>runtime of the movie<br>
</li><li>one or more genres<br>
</li><li>the plot of the movie<br>
</li><li>user ratings<br>
Additionally also the poster and backdrop will be retrieved, which could be displayed in the PVMC video list, depending on the used skin.</li></ul>

Besides the already shown problems that could rise during the IMDb-query we could face additional errors by asking TheMovieDB about the current movie, that might result in a failed sync of the video - for example:<br>
<ul><li>the searched movie is not contained in "TheMovieDB" at all<br>
</li><li>the searched movie is contained in "TheMovieDB", but the entry is not linked to the related IMDb-ID. If that's the case then the PVMC-query doesn't return any results!<br>
</li><li>title and / or plot are not available in the desired sync language<br>
</li><li>there are no poster / backdrops available for that movie - or the posters are only available in the "wrong" language<br>
In all cases listed above it is suggested to create a new TheMovieDB account (for free) and to add / correct the information for the corresponding movie. Normally the adapted record is then available for new PVMC queries within a few days!</li></ul>

<h3>Synchronisation of TV-shows</h3>

TODO<br>
<br>
<br><br>
<h2>Starting a sync run</h2>

The synchronisation can be started by either using the Web Interface ("Home" => "Sync") or by using the synchronisation manager of PVMC E2 GUI, which can be entered by performing the following steps from the main menu: "System" => "Synchronize".<br>
<br>
In any case there are two different synchronisation types available:<br>
<ul><li>a full synchronisation (when using the PVMC Enigma2 sync manager available through the "green" option key - in the WebIF labeled "normal Sync")<br>
</li><li>a fast synchronisation (when using the PVMC Enigma2 sync manager available through the "yellow" option key - in the WebIF labeled "fast Sync")</li></ul>

The full synchronisation option is suggested if you're running PVMC for the first time. By doing so the directories defined in the search path are scanned and the contained movie files will be added to the database. If the option "Delete movie if file not found" from the main settings is selected, the related entries from the database will be removed if the related media files are not found any more.<br>
<br>
Please note, that you can leave the synchronisation manager while the synchronisation process is still in progress: just press the "Exit" key after you initiated a synchronisation run and the synchronisation process will be performed in the background. A pop-up message is displayed in order to notify you right after the synchronisation process has been finished!<br>
<br>
The "fast synchronisation" will only add new titles to the database. hence this option is much faster compared to the full synchronisation option.<br><br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/sync_small.png' />
<br><br>
<h2>Settings</h2>
The synchronisation manager settings can be entered using the <a href='blue.md'>blue</a> key. There you can specify the search path and the language to be used for both the plots and titles. Additionally you can reset / delete the database, cache and filters.<br>
<br>
<b>Note: after modification of any synchronisation setting (especially after change of synchronisation language) a new sync-run has to be performed!</b>
<br><br>
<h2>Media provider</h2>
The data for plot, title, genre etc. is retrieved from <a href='http://www.imdb.com'>IMDB.com</a>, <a href='http://www.themoviedb.org'>TheMovieDB.org (TMDB)</a> and <a href='http://www.thetvdb.org'>TheTVDB.org (TVDB)</a>. While IMDB is used to uniquely identify the movie (and hence for retrieving the unqiue IMDb-ID) the two remaining sources are used to retrieve Plots, Poster, Backdrops etc.<br>
The search order used by PVMC is as follows:<br>
<ul><li>first of all TMDB, resp. TVDB are asked for the plot in the language defined in the synchronisation manager options (= local language)<br>
</li><li>if no plot for the local language is found, PVMC will check IMDB for a plot in the local language<br>
</li><li>if the IMDB search fails, too PVMC will check TMDB / TCVDB for the english plot<br>
</li><li>finally PVMC will check IMDB for an english plot<br>
Please note, that poster and backdrops will only be retrieved from TMDB and TVDB. If there are no poster and backdrops available for your movie, then no arts will be displayed later on in the movie lists! If this happens for one some of your movies then it is suggested to just open an account at TMDB and 7 TVDB in order to upload some arts for the desired movies. By doing so everyone has a benefit! :-)<br>
<br><br>
<h2>Search structures</h2>
The file <code>paths.xml</code> is used to define both the file extensions to be used in order to detect media files (for example "<code>mkv|ts|avi|m2ts</code>") and the directories that should be searched together with their categories (movies => category "MOVIE", TV-shows => category "TV" or both => category "MOVIE_AND_TV").</li></ul>

There are three ways on how the mentioned settings can be done:<br>
<ul><li>editing the file manually (a file containing some default values will be copied during installation to <code>/hdd/valerie</code> - see also => <a href='Resources#Configuration_files.md'>configuration files</a>)<br>
</li><li>by using the corresponding setting in the synchronisation manager options<br>
</li><li>by editing the corresponding settings in the WebIF ("Home" => "Options" => "Sync Settings")</li></ul>

Besides the above mentioned options it can als be specified for every directory in the <code>paths.xml</code>, if the file names or the name of the corresponding directories shall be used for the sync.<br>
<br>
The video collection could look for example like the following:<br>
<ul><li><code>/hdd/movie</code> => category "MOVIE"<br>
</li><li><code>/hdd/series</code> => category "TV"<br>
</li><li><code>/hdd/mixed</code> => category "MOVIE_AND_TV"<br>
After a full synchronisation the files contained in directory "<code>/hdd/movie</code>" will be added to the "Movie"-list. The files contained in directory "<code>/hdd/series</code>" will be recognized as episodes for series / TV shows and the files contained in the "<code>mixed</code>" directory will be parsed as movie - and if that doesn't succeed another try will be started as TV-show.</li></ul>

Wrong parsed entries can be corrected manually later on by either using the PVMC GUI or WebIf (<a href='Sync#Fix_wrong_parsed_media.md'>see below</a>).<br>
<br>
<h3>DVDs</h3>
Normally PVMC detects movies split into several files by name. An exception to this rule are directories containing a DVD structure (<code>*</code>.vob, <code>*</code>.ifo). Since it is not possible to built a search string out of the file name the directory name is used instead.<br>
<br>
<h3>Fix wrong parsed media</h3>
One can manually correct videos that has not been synced at all - or in case they have been identified as a different video. Additionally all attributes of a database entry can be modified, for example title, plot, genres, user-rating, poster and backdrops etc. The suggested way of doing things is by using the web interface!<br>
<br>
<h4>Video has not been identified at all</h4>
In that case PVMC was not able to find any information for the current video and hence the video has been added to the "failed" section of the Web interface. Hence please open the web interface and click "Home" => "Failed". Identify the desired in the list of all failed entries and proceed as follows:<br>
<ul><li>if the video is a movie, please click "M" in order to add it as a movie. On the next page you can now enter all relevant data for a movie such as title, plot IMDb-ID, poster, backdrop etc. manually.<br>
</li><li>if the video is an episode of a TV show please click the "E" button. On the next page you can enter all relevant data suitable for an Episode mahually.</li></ul>

<b>Important</b> After entering all data you'll have to save your modifications by clikcing the red "Save to Database" button in the upper left corner!<br>
<br>
<b>Please note</b>
Currently all manually edited data gets lost after a new full sync. hence it is suggested to use one of the search hints described in chapter <a href='Sync#Excludes_und_Suchhilfen.md'>"Excludes und Suchhilfen"</a> since PVMC will then detect the movie correctly with every sync run - without the need of manually editing stuff again and again.<br>
<br>
<h4>Video has been identified as a different one</h4>
In that case PVMC identified the video as a different video and thus has retrieved the wrong information from the online database. Hence one has a "wrong" entry in the Movie / TV show list, which makes it hard especially in large video collections to identify such a wrong entry!...<br>
<br>
In order to fix that problem by using the web interface one has to first open the corresponding video list in the Web-Interface, i.e. either "Home" => "Movie" or "Home" => "TV show" / "Home" => "TV show" => "Episodes" and then to identify the wrong entry.<br>
<br>
Next look at the column "Actions" located at the right side of the table and notice the tiny little pencil icon. Click that one in order to get to the "Edit" page where you can proceed with your modifications.<br>
<br>
<b>Important</b> After entering all data you'll have to save your modifications by clikcing the red "Save to Database" button in the upper left corner!<br>
<br>
<h4>Manually fixing wrong entries using the synchronisation manager</h4>
TODO<br>
<br>
<br><br>
<h2>Excludes and search hints</h2>
PVMC offers several options in order to affect the parse process and thus to control what is synced and how:<br>
<br>
<ul><li>add release year to file name<br>
</li><li>provide the IMDb-Id within the media file name<br>
</li><li>provide the IMDb-Id in a dedicated <code>*.nfo</code>-file<br>
</li><li>exclude whole folders from search process - even if they are contained in the search path<br>
</li><li>define search phrases for whole directories<br>
</li><li>define meta information in a dedicated (XBMC-sytle) <code>*.nfo</code>-file<br>
</li><li>using regular expressions</li></ul>

The upcoming chapters will describe these options more detailed. But please keep in mind, that it is suggested to always perform a full sync after you added / modified search hints in order to rebuilt the database - perhaps also deleting the database would be helpful to eliminate the risk of getting side effects caused by old entries.<br>
<h3>Add release year to file name</h3>
Especially in case of syncing a remake it's important to tell PVMC which movie ist the correct one to sync. The IMDb search for "Bangkok Dangerous" for example returns multiple results with exact the same name:<br>
<br>
<blockquote><a href='http://m.imdb.com/find?q=bangkok+dangerous'>http://m.imdb.com/find?q=bangkok+dangerous</a></blockquote>

<ul><li>"Bangkok Dangerous" released in 2008<br>
</li><li>"Bangkok Dangerous" released in 1999</li></ul>

Without any hints regarding the year PVMC would use the movie released in 2008 since this one is the first movie returned by IMDb. But what to do if one has the second movie released in 1999? In order to get PVMC back on track you just need to rename your video file as described below:<br>
<br>
<b>file name of the media file (old):</b> <code>Bangkok_Dangerous.avi</code>

<b>file name of the media file (new):</b> <code>Bangkok_Dangerous_(1999).avi</code>

=> It is important to specify the year with four digits and enclosed by braces - if everything's OK then PVMC will retrieve the year from the filename and uses that year specification later on in the sync process as additional search criteria!<br>
<br>
<h3>Provide IMDb-ID within the file name</h3>
It is possible to provide the IMDb-ID for a video by specifying the ID in the file name of the related media file:<br>
<br>
<b>file name of the media file (old):</b> <code>WrongDetectedMovie.avi</code>

<b>file name of the media file (new):</b> <code>WrongDetectedMovie_tt1234567.avi</code>

<b>Please note:</b> the underscore "<code>_</code>" given in the example above is not mandatory. Additionally the location of the IMDb-ID doesn't matter at all, but it has to be ensured, that the ID starts with "<code>tt</code>", followed by seven digits. besides that it is important to know, that an IMDb-ID provided by the file name, will be overwritten by the IMDb-ID provided by nfo-file (see upcoming chapter).<br>
<br>
<h3>IMDb ID provided by nfo-file</h3>
Another possibility to provide the correct IMDb-ID for wrong parsed media is a so-called "nfo"-file. Such a file has to be located in the same directory as the media file and it has to have the same name as the media file, but the extension has to be "<code>nfo</code>". The content of the file is just the IMDb-ID, but it is important that currently <i>two lines</i> have to be contained in the file! For example:<br>
<br>
<b>file name of the video file:</b> <code>WrongDetectedMovie.avi</code>

<b>file name of the nfo-file:</b> <code>WrongDetectedMovie.nfo</code>

<b>content of the nfo-file:</b>

<pre><code>tt1234567<br>
</code></pre>

Please note: it doesn't matter if there is additional text preceding the IMDb-ID, for example the complete link for this movie to IMDb could be contained in the nfo and it would still work:<br>
<br>
<b>Alternative content of the nfo-file:</b>

<pre><code>http://www.imdb.com/title/tt1234567/<br>
<br>
</code></pre>

<h3>Exclude folders from parsing</h3>
A whole folder and his subfolders can be excluded from the parse process by simply adding to the folder which should be excluded a new file <code>valerie.info</code> simply containing the word <code>ignore</code>:<br>
<br>
<pre><code>ignore<br>
</code></pre>

<h3>Search string for whole directories</h3>
Besides the above mentioned possibilities another option would allow for the definition of search strings used for the whole directory. This is especially helpful in case of TV-shows since otherwise you'd have to provide a nfo-file for each single episode.<br>
To do so, just add a new <code>valerie.info</code> file to the corresponding directory of the TV show, containing the word to be used for search. As mentioned above the search query should return an ambiguous result in order to enhance the parse results.<br>
<br>
<b>Please note:</b>
The search string provided using this way is only valid for the current directory, but not for contained sub-directories.<br>
<br>
Using a <code>valerie.info</code> it's additionally possible to define the following IDs for the whole folder:<br>
<ul><li>the IMDb-ID<br>
</li><li>the TheTvDB-ID<br>
</li><li>or both IDs together</li></ul>

<b>Please note:</b>
Currently an empty line is needed at the end of the file - otherwise it is possible, that the last number of the specified ID may be cut-off!<br>
<br>
Sample content for <code>valerie.info</code> used to specify the IMDb-ID for the current directory:<br>
<br>
<pre><code>tt1234567<br>
</code></pre>

Sample content for <code>valerie.info</code> used to specify the TheTvDB-ID for the current directory:<br>
<br>
<pre><code>&lt;tvdb&gt;tvdb12345<br>
</code></pre>

Sample content for <code>valerie.info</code> used to specify both the IMDb-ID and the TheTvDB-ID for the current directory::<br>
<br>
<pre><code>tt1234567 &lt;tvdb&gt;tvdb12345<br>
</code></pre>

<h3>XBMC-style nfo-files</h3>
Additionally to the previously mentioned nfo-files used to provide just the IMDb-ID it's planned to support nfo files containing the whole set of meta attributes used by XBMC. Currently at least the following attributes are supported:<br>
<ul><li><code>&lt;id&gt;</code> => IMDb-ID for movies<br>
</li><li><code>&lt;episodedetails&gt;</code> => IMDb-ID for episode<br>
</li><li><code>&lt;season&gt;</code> => season # for TV-shows<br>
</li><li><code>&lt;episode&gt;</code> => episode # for TV-shows<br>
</li><li>`<br>
<br>
<title><br>
<br>
 => title of movie / Tv show<br>
</li><li><code>&lt;year&gt;</code> => year<br>
</li><li><code>&lt;plot&gt;</code> => plot of video<br>
</li><li><code>&lt;runtime&gt;</code> => total runtime in minutes<br>
</li><li><code>&lt;genre&gt;</code> => genre<br>
</li><li><code>&lt;rating&gt;</code> => user rating<br>
</li><li><code>&lt;tagline&gt;</code> => tagline of movie<br>
</li><li><code>&lt;codec&gt;</code> => used video codec<br>
</li><li><code>&lt;width&gt;</code> => resolution<br>
<b>Please note:</b> The implementation of this functionality is somehow "experimental" - hence you should expect problems, especially when parsing complex NFO's...</li></ul>

<h3>Regular expressions</h3>
Before a search query is started the used search string can be adapted using regular expressions. These regular expressions can be defined in the following configuration files: "<code>pre.conf</code>", "<code>post_movie.conf</code>" and "<code>post_tv.conf</code>":<br>
<ul><li><code>pre.conf</code> is used for both movie and TV shows<br>
</li><li><code>post_movie.conf</code> is only applicable for movies<br>
</li><li><code>post_tv.conf</code> is only applicable for TV shows.<br>
Example:<br>
Assuming a media file has the following file name:<br> "<code>The.Beach.2000.720p.HDTV.x264-ESiR.mkv</code>"<br>
By default PVMC would use the following string as search string: "<code>The Beach 2000 ESiR</code>"<br>
Since the returned result is ambiguous PVMC would use the first result returned (i.e. the "best match") which in this case is "<code>Beach Tennis USA: The Road to Long Beach 2009</code>". In order to avoid such wrong parse-results it is possible to filter specific words by using regular expressions to get the correct media returned as first result.<br>
More on regular expressions can be found on <a href='http://www.zdnet.de/anwendungsentwicklung_regular_expressions_syntax_entraetselt_story-20000201-20000839-1.htm'>ZDNET</a>. In order to check and test regular expressions written on your own the following online tool is very helpful: <a href='http://gskinner.com/RegExr'>RegEx Tool</a><br>
<br>