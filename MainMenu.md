# Datenbank Dateien #
Valerie verwaltet die Film und Serieninformationen in einer internen Datenbank (Python Pickle Dateien). Diese befindet sich im fest definierten Verzeichnis "/hdd/valerie" und besteht aus den Dateien:<br>
<ul><li>movies.db	(alle Filme)<br>
</li><li>tvshows.db	(alle Serien)<br>
</li><li>episodes.db	(alle Episoden der Serien)<br>
</li><li>failed.db	(alle fehlgeschlagenen Syncs sowie multipart Filme, wie z.B. <code>*</code><i>cd2, <code>*</code></i>part2, etc.)<br>
<br>
<h1>Config Dateien</h1>
Die Konfigurationsdateien von Valerie befinden sich im Verzeichnis /hdd/valerie:<br>
</li><li>valerie.conf		(Suchsprache und Verhalten bei nicht mehr vorhanden Medien-Files im Suchpfad)<br>
</li><li>paths.conf		(Suchpfad, Filter für Dateierweiterung [z.B. avi,mkv, etc ], und flaggen von Suchordnern)<br>
</li><li>pre.conf			(Regular Expressions für den Suchstring)<br>
</li><li>post_movie.conf	(Regular Expressions für den Suchstring - nur Filme)<br>
</li><li>post_tv.conf		(Regular Expressions für den Suchstring - nur Serien)<br>
</li><li>blacklist.conf	(aus der DB ausgeblendete/gelöschte Filme)<br>
<br>
<h1>Startup Datei</h1>
Das Shellskript /hdd/valerie/start.sh kann verwendet werden um mit Valerie weitere Dienste oder Skripte zu starten.<br>
<h1>spezielle Dateien</h1>
</li><li>valerie.info (für Excludes oder Suchhilfen)</li></ul>

<h1>Skins</h1>
Derzeit stehen folgende Skins zur Verfügung:<br>
<ul><li>Default<br>
</li><li>BlackSwan<br>
</li><li>GreySkies<br>
Weitere Infos zu Skins im  Kapitel "Skin"<br>
<h1>Log Files</h1>
Die Logfiles von Valerie befinden sich in /tmp/valerie/ und können auch über den Browser aufgerufen werden. Weitere Infos siehe Kapitel <a href='WebIf.md'>"Webinterface"</a>.