

---

# Database files #
Valerie uses Python Pickle files located in `/hdd/valerie` (editable in the [main-settings](Options.md)) in order to manage information for both movies and TV shows:
  * `mediafiles.db`
  * `tables.db`
**Please note** (since it has been asked every now and then):<br>These files don't contain "database tables", but serialized Python objects used by PVMC - and thus can neither get edited by using a text-editor nor by any other database application / SQL editor / whatever.<br>
<h1>Configuration files</h1>
The configuration files of Valerie are located in <code>/hdd/valerie</code> and can be edited by using the PVMC <a href='Options.md'>main-settings</a>) or - more comfortable - through the <a href='WebIF.md'>"Webinterface"</a>.<br>
<ul><li><code>sync.xml</code>:<br>
<ul><li>language used for synchronisation of titles, plots etc.<br>
</li><li>flag how to handle media files not found any more<br>
</li></ul></li><li><code>paths.xml</code>:<br>
<ul><li>contains all search paths to be considered for synchronisation<br>
</li><li>list of file extansions to be considered during synchronisation (=> <code>avi</code>, <code>mkv</code>, ...)<br>
</li><li>categorization of folders contained in the search path => "Movie", TV-show" or both<br>
</li><li>dedicated setting for each folder whether to use foldername or filename for synchronisation<br>
</li><li>it's possible to switch on / off each search path seperately!<br>
</li></ul></li><li><code>paths.conf</code> (=> see <code>paths.xml</code>):<br>
<ul><li><i>old, but still supported file in case paths.xml is not present for whatever reason</i>
</li><li>it's not possible to switch on / off search paths using this file!<br>
</li></ul></li><li><code>pre.conf</code>:<br>
<ul><li>contains regular expressions allowing for the manipulation of the search string used for synchronisation<br>
</li><li>regular expressions taken from this file will be applied for both movies and TV-shows<br>
</li><li><b>Hint:</b> if you messed-up this file while experimenting with your own regular expressions, just delete it and restart PVMC in order to re-create it with its default content<br>
</li><li>for more information on using regular expressions in order to enhance synchronisation results please see also the related chapter in the <a href='Sync#Regular_expressions.md'>"Synchronisation" wiki page</a>
</li></ul></li><li><code>post_movie.conf</code>:<br>
<ul><li>regular expressions applicable for the search string used for movies<br>
</li></ul></li><li><code>post_tv.conf</code>:<br>
<ul><li>regular expressions applicable for the search string used for TV shows<br>
</li></ul></li><li><code>blacklist.conf</code>:<br>
<ul><li>movies manually removed from the database<br>
<br>
<h1>Special files</h1>
<h2>valerie.info</h2>
This file can be used to ignore directories from synchronisation - or to enhance the search results by providing the IMDB-Link for a special movie or TV-Show.<br>
For more details on this file check section <a href='Sync#Excludes_and_search_hints.md'>"excludes and search hints"</a>.<br>
<br>
<h1>Skins</h1>
Currently the following skins are available:<br>
</li></ul></li><li>Default<br>
</li><li>BlackSwan<br>
</li><li>GreySkies<br>
See also chapter <a href='skin.md'>"Skin"</a> for details.<br>
<br>
<h1>Log files</h1>
The log files of Valerie are located in <code>/tmp/valerie/</code> (editable in the <a href='Options.md'>main-settings</a>). The files can be retrieved additionally by using the corresponding option within the <a href='WebIF.md'>"Webinterface"</a>.