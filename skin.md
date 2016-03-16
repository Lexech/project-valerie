
<br>
<h1>Skins</h1>
This chapter contains short descriptions and screen shots of all skins currently available for Project Valerie. New skins can be added by manually copying the related folder to the following directory on your box:<br>

<code>/usr/lib/enigma2/python/Plugins/Extensions/ProjectValerie/skins</code>

<b>Afterwards a restart of Enigma2 is necessary in order to make the new skin available for selection in the settings!</b>
<br><br>

<h2>Default skin</h2>
This is the default skin of Project Valerie<br>

<img src='http://project-valerie.googlecode.com/svn/trunk/images/movie_mini.png' /><br>

<h2>Skin blackSwan</h2>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/blackswan_small.png' /><br>

<h2>Skin greySkies</h2>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/greyskies_small.png' />
<br><br>
<h1>Animated Main-Menu</h1>
Currently only the "blackSwan" skin supports this feature. In order to have an animated main menu just place a file containing the animation as <b>blackSwan.mp4</b> in the following directory:<br>
<blockquote><code>/hdd/valerie/dreamscene/</code><br>
Please check the download-link below for animation files.<br>
<br>
With some manual editing this feature is also available for other skins. To do so please modify the <code>skin.xml</code> contained in the directory of the desired skin, for example <code>../ProjectValerie/skins/default/1280x720/skin.xml</code> as follows:<br></blockquote>

1. Within the section "<!-- PVMC Main Menu -->" the following line has to be adapted:<br>
original:<br>
<pre><code>    &lt;widget name="API" text="2" position="0,0" zPosition="0" size="1,1"/&gt;<br>
</code></pre>
<br>
modified:<br>
<pre><code>    &lt;widget name="API" text="3" position="0,0" zPosition="0" size="1,1"/&gt;<br>
</code></pre>
<br><br>
2. Additionally the following line has to be added afterwards:<br>
<pre><code>    &lt;widget name="stillpicture_usedreamscene" text="/hdd/valerie/dreamscene/&lt;Dateiname&gt;.mp4" position="0,0" zPosition="0" size="1,1"/&gt;<br>
</code></pre>
<br>

The complete "<!-- PVMC Main Menu -->" section should now look similar to the following:<br>
<pre><code>&lt;screen name="PVMC_MainMenu" position="0,0" size="1280,720" title=" " backgroundColor="#FF000000" flags="wfNoBorder"&gt;&lt;br&gt;<br>
    &lt;widget name="API" text="3" position="0,0" zPosition="0" size="1,1"/&gt;&lt;br&gt;<br>
    &lt;widget name="stillpicture_usedreamscene" text="/hdd/valerie/dreamscene/blackSwan.mp4" position="0,0" zPosition="0" size="1,1"/&gt;&lt;br&gt;<br>
    &lt;widget name="showiframe" position="0,0" zPosition="0" size="1280,720" text="/usr/lib/enigma2/python/Plugins/Extensions/ProjectValerie/skins/blackSwan/background.m1v"/&gt;&lt;br&gt;<br>
<br>
</code></pre>
<br><br>
3. Finally the file containing the animation has to be renamed according to the used skin. A choice of different animated main menu files can be found here:<br>
<a href='http://uploaded.net/file/pwkl86yv'>http://uploaded.net/file/pwkl86yv</a>
<br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/dreamscene-banner.jpg' />
<br>
<br>
Here some <code>Valve´s - Portal 2</code> styled dreamscenes:<br>
<br>
<a href='http://www.megaupload.com/?d=PQ977SQD'>http://www.megaupload.com/?d=PQ977SQD</a>
<br>
<img src='http://project-valerie.googlecode.com/svn/trunk/images/portal2_dreamscene.png' />
<br>
<br>
With special thanks to Rocketcheeta! -- <a href='http://rocketcheetah.com'>http://rocketcheetah.com</a>
<br>