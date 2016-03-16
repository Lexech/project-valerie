
<br>
<h1>Hauptmenü</h1>
<b>Das Hauptmenü von Project Valerie:</b><br><br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/main_menu_small.png' />

<h2>Einstellungen</h2>
In den Einstellungen können alle Settings zur Benutzeroberfläche und Startoptionen vorgenommen werden.<br>
<br><br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/settings_small.png' /><br>
Informationen zu den einzelnen Optionen finden sich <a href='Options.md'>hier</a>.<br>
<br><br>
<h2>Synchronisieren</h2>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/sync_small.png' />
<br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/sync_options_small.png' />
<br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/sync_options2_small.png' />
<br><br>
Im "Synchronisieren"-Menü können die Filme und Serien verwaltet, sowie neue Titel eingelesen werden.<br>
Außerdem werden hier über die Einstellungen die Suchpfade festgelegt, die Suchsprache eingestellt, oder die DB zurückgesetzt.<br><br>
Die Spracheinstellung bezieht sich auf die Synchronisation mit den Media-Providern, also in welcher Sprache der Plot gelesen wird. Die Sprache in den Menüs usw. ist abhängig von der Systemsprache der Box. <br>
Weitere Infos zur Synchronisation findest du im <a href='Sync.md'>Sync</a>-Kapitel.<br>
<br><br>
<h2>Live TV</h2>
Hier gelangt man – wie der Name schon sagt – wieder zurück zum normalen Live-TV<br><br>
<h2>Filme</h2>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/movie_mini.png' /><br>
Falls der Plot nicht komplett in die Darstellung passt, kann über die INFO Taste der Plot extra dargestellt werden.<br>

Es können über die <b>rote Taste</b> verschiedene Filter zu Darstellung der Titelliste gesetzt werden <br> (sortiert nach Name, nach Release Jahr, nach Erstellungsdatum im Dateisystem und nach Beliebtheit.<br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/sort_red.png' /><br><br>

Über die <b>blaue Taste</b> können Filter für das Genre gesetzt werden. Diese erweitern sich, je nach Genre der gesyncten Titel automatisch.<br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/sort_blue.png' /><br><br>
<br><br>
<h2>TV Shows</h2>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/series_mini.jpg' /><br>
Es gelten die gleichen Tasten wie bei "Filme".<br>
<br><br>
<h1>Valerie-Log</h1>
Das Valerie Log ist über den Browser erreichbar. Einfach die Box IP + festgelegten Port in den Browser eingeben. Alle gefundenen Valerie Logs werden aufgelistet und können herunter geladen werden. <br>
Bsp: <br>
<a href='http://192.168.0.100:8888'>http://192.168.0.100:8888</a> <br><br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/Val_log.png' /><br>
Weitere Infos siehe Kapitel <a href='WebIF.md'>Webinterface</a>.<br>
<br><br>
<h1>Trakt.TV</h1>
Trakt.tv ist eine Internetplattform, die zu bereits gesehenen Filmen Empfehlungen zu ähnlichen Filmen abgibt. Projekt Valerie nutzt dies, um Titel als bereits gesehen zu markieren, sofern diese zu mindestens 75% angesehen wurden.<br>
Um Trakt.tv zu nutzen, ist eine separate Registrierung notwendig. Weiteres im Kaptitel <a href='TraktTV.md'>Trakt.TV</a>, sowie auf der Internet-Seite [www.trakt.tv Trakt.TV].<br>
<b>HINWEIS</b>
Projekt Valerie ist für die Inhalte und Nutzung von Trakt.TV nicht verantwortlich, sondern nutzt dies lediglich um Filme als gesehen zu markieren!<br>
<br><br>
<h1>Untertitel</h1>
In Projekt Valerie steht ein Subtitle Downloader zur Verfügung. Weitere Informationen findest du im Kapitel <a href='subtitles.md'>Untertitel</a>.<br>
<br><br>
<h1>Cover und Backdrops</h1>
Poster und Backdrops werden in „/…/valerie/media“ abgelegt. Falls man diese selbst erstellen möchte, sind folgende Tools nötig:<br><br>

Cover<br>
-	convert.exe aus dem <a href='http://www.imagemagick.org/script/binary-releases.php#windows'>Image-Magic Paket</a><br>
-	<a href='http://www.libpng.org/pub/png/apps/pngquant.html'>pngquant</a><br>
Die Wunsch JPG´s in einem bestimmten Verzeichnis richtig benannt (IMDB-ID<code>_</code>poster.jpg) ablegen.<br>
Den folgenden Code in einer <code>*</code>.bat, oder direkt in der Eingabeaufforderung ausführen, allerdings dann aus den doppelten Prozentzeichen nur eines machen:<br>
<pre><code>FOR /F "delims=." %%a IN ('dir /b &lt;path_to_jpg&gt;\*_poster.jpg') do (&lt;path_to_convert&gt;\convert.exe -resize 156x214! -depth 256 &lt;path_to_jpg&gt;\%%a.jpg &lt;export_path_for_png&gt;\%%a.png &amp; &lt;path_to_pngquant&gt;\pngquant.exe 256 &lt;export_path_for_png&gt;\%%a.png &amp; del &lt;export_path_for_png&gt;\%%a.png &amp; move &lt;export_path_for_png&gt;\%%a-fs8.png &lt;ready_to_use_png&gt;\%%a.png)<br>
</code></pre>
<br><br>
Backdrops<br>
-	ffmpeg von <a href='http://ffmpeg.arrozcru.org/autobuilds/ffmpeg/mingw32/static/'>ffmpeg.arrozcru.org</a><br>
Vorgehen ist das Gleiche wie bei den Covers, allerdings als IMDB-ID<code>_</code>backdrop.jpg ablegen.<br>
Den folgenden Code in einer <code>*</code>.bat, oder direkt in der Eingabeaufforderung ausführen, allerdings dann aus den doppelten Prozentzeichen nur eines machen:<br>
<br>
Die Backdrops in das richtige Format bringen <br><br>
(1280x720)<br>
<pre><code>FOR /F "delims=." %%a IN ('dir /b &lt;path to image&gt;\*_backdrop.jpg') do (&lt;path to convert&gt;\convert.exe &lt;path to image&gt;\%%a.jpg -colorspace YUV -resize 1280x720! -gravity Center -crop 1280x720+0+0 +repage &lt;output&gt;\%%a.jpg)<br>
</code></pre>
<br>
ODER (1920x1080)<br>
<pre><code>FOR /F "delims=." %%a IN ('dir /b &lt;path to image&gt;\*_backdrop.jpg') do (&lt;path to convert&gt;\convert.exe &lt;path to image&gt;\%%a.jpg -colorspace YUV -resize 1920x1088! -gravity Center -crop 1920x1080+0+0 +repage &lt;output&gt;\%%a.jpg)<br>
</code></pre>
<br>
Umwandeln in eine <code>m1v</code> Datei:<br>
<pre><code>FOR /F "delims=." %%a IN ('dir /b &lt;path_to_jpg&gt;\*_backdrop.jpg') do ("&lt;path_to_ffmpeg&gt;\ffmpeg" -i &lt;path_to_jpg&gt;\%%a.jpg -an -f mpeg2video -r 25.0 -vcodec mpeg2video -intra -sc_threshold 1000000000 -flags +mv0+cgop -dc 8 -g 1 -me_method zero -qscale 5 -bf 0 -aspect 16:9 &lt;path_for_output&gt;\%%a.m1v)<br>
</code></pre>
<br><br>
Die erstellten Dateien können dann in das Verzeichnis in <code>/hdd/valerie/media</code> auf der Box kopiert werden.<br><br>