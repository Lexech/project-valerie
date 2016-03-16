

# Global Settings #
The global settings are accessible from both PVMC's Enigma2 main menu and from the [Web-Interface](WebIF.md) ("Home" => "Options" => "Global Settings"). They allow for the configuration of PVMC start-up behavior, skin-selection, auto-update functionality and many more.

The following chapters describe the different settings together with their possible values. Default values are displayed **bold**. Additionally where possible the key used to store the settings in the Enigma2 settings file (`/etc/enigma2/settings`) is given.

**Note**<br>
The Enigma2 settings file should not be edited while Enigma2 is running, since otherwise the modified settings will be overwritten with their original values when Enigma2 gets shut-down!<br>
<br>
<h3>Show wizard on next start</h3>
{"yes", <b>"no"</b>}<br>
<code>config.plugins.pvmc.showwizard</code>

Configures whether the PVMC installation wizard is displayed after start-up.<br>
<br>
<h3>Start Valerie on e2 start</h3>
{<b>"yes"</b>, "no"}<br>
<code>config.plugins.pvmc.autostart</code>

Allow for the automatic start-up of PVMC if Enigma2 is started. In that case you will see PVMC main menu instead of the TV picture after reboot of your box.<br>
<br>
<h3>Check for updates on Valerie start</h3>
{<b>"yes"</b>, "no"}<br>
<code>config.plugins.pvmc.checkforupdate</code>

Determines whether PVMC shall check for updates right after start-up. If so a message box is displayed for 120 sec. asking whether the new version shall be downloaded and installed or not.<br>
Please note: since an Enigma2 restart is required after a new version has been installed the default for the message box is "no" in order to not disturb use-cases where an automatic start-up of your box is needed.<br>
<br>
<h3>Backdrop quality</h3>
{<b>"High"</b>, "Low"}<br>
<code>config.plugins.pvmc.backdropquality</code>

Defines the quality of the backdrops used in both movie and TV shows list.<br>
<br>
<h3>Skin</h3>
{<b>"default"</b>, "blackSwan", "greySkies"}<br>
<br>
Select the skin used by PVMC.<br>
<br>
<h3>On Power press</h3>
{<b>"DeepStandby"</b>, "Standby"}<br>
<code>config.plugins.pvmc.onpowerpress</code>

Configures how your box shall behave if you click the Power button.<br>
<br>
<h3>Show Movie and TVShow in main menu</h3>
{"yes", <b>"no"</b>}<br>
<code>config.plugins.pvmc.showmovieandtvinmainmenu</code>

Determines whether the entries for "Movies" and "Tv Shows" shall be displayed in PVMCs main menu.<br>
<br>
<h3>Synchronize: Fast Sync on autostart</h3>
{<b>"yes"</b>, "no"}<br>
<br>
This option configures, whether an automatic "fast sync" run shall be performed after PVMC starts-up.<br>
<br>
<h3>myEpisodes: Eingeschaltet</h3>
{"yes", <b>"no"</b>}<br>
<br>
Switch on / off usage of "myEpisodes" TV shows tracking functionality.<br>
<br>
<h3>myEpisodes: Benutzername</h3>
{<b>"username"</b>}<br>
<br>
Specify the myEpisodes username to be used when tracking your TV shows.<br>
<br>
<h3>myEpisodes: Passwort</h3>
{<b>"password"</b>}<br>
<br>
Specify the myEpisodes password to be used when tracking your TV shows.<br>
<br>
<h3>Webinterface: Port</h3>
{<b>08888</b>}<br>
<br>
The port to be used by the <a href='WebIF.md'>Web-Interface</a>.<br>
<br>
<h3>Use Trakt.tv</h3>
{"yes", <b>"no"</b>}<br>
<br>
Switch on / off usage of "Trakt.tv" movies tracking functionality.<br>
<br>
<h3>Trakt.tv - Username</h3>
{<b>"username"</b>}<br>
<br>
Specify the "Trakt.tv" username to be used when tracking your movies.<br>
<br>
<h3>Trakt.tv - Password</h3>
{<b>"password"</b>}<br>
<br>
Specify the "Trakt.tv" password to be used when tracking your movies.<br>
<br>
<h3>SubtitleDownloader: Provider</h3>
{<b>"Opensubtitles"</b>, "Bierdopje", "Napiprojekt", "Ondertitel", "Sratim", "Subdivx", "Swesub", "Titlovi", "Undertexter"}<br>
<br>
Specify the subtitle provider to be used by PVMCs subtitle download functionality. Find out more about PVMC subtitle functionality by checking the corresponding <a href='subtitles.md'>wiki page</a>.<br>
<br>
<h3>SubtitleDownloader: Language 1</h3>
{}<br>
<br>
Find out more about PVMC subtitle functionality by checking the corresponding <a href='subtitles.md'>wiki page</a>.<br>
<br>
<h3>SubtitleDownloader: Language 2</h3>
{}<br>
<br>
Find out more about PVMC subtitle functionality by checking the corresponding <a href='subtitles.md'>wiki page</a>.<br>
<br>
<h3>SubtitleDownloader: Language 3</h3>
{}<br>
<br>
Find out more about PVMC subtitle functionality by checking the corresponding <a href='subtitles.md'>wiki page</a>.<br>
<br>
<h3>{EXPERT} Valerie Config folder (Database, ...)</h3>
{<b>/hdd/valerie/</b>}<br>
<code>config.plugins.pvmc.configfolderpath</code>

Option to specify the folder where PVMC shall store its configuration and database files.<br>
<br>
<h3>{EXPERT} Valerie media folder (Poster, Backdrops)</h3>
{<b>/hdd/valerie/media</b>}<br>
<code>config.plugins.pvmc.mediafolderpath</code>

Option to specify the folder where PVMC shall store the media files.<br>
<br>
<h3>{EXPERT} Valerie tmp folder (Logs, Cache)</h3>
{<b>/tmp/valerie</b>}<br>
<code>config.plugins.pvmc.tmpfolderpath</code>

Option to specify the folder where PVMC shall store its temporary files.<br>
<br>

<h1>Synchronization-Settings</h1>
TODO<br>
<br>
<h1>Screenshots</h1>
<h2>Main settings</h2>
The screenshots below show the main settings screens of PVMC:<br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/settings_small.png' /><br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/settings2_small.png' /><br><br>
<h2>Synchronization Settings</h2>
The screenshots below show the synchronization settings screens of PVMC:<br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/sync_options_small.png' /><br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/sync_options2_small.png' /><br>
<br><br>