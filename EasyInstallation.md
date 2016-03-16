
<br>
<h1>Installation of Project Valerie</h1>
<h2>Special hint for AAF-Image users</h2>
User of a "Don't Cry" AAF beta-image with SVN-version < M15000 should consider the following points:<br>
<ul><li>in order to install PVMC using the supposed method with <code>opkg</code> an additional library is needed that might be missing on your image<br>
</li><li>some AAF image versions are missing some additonal python libraries needed by PVMC in order to run correctly<br>
For more details on those issues and a possible solution for that please see <a href='http://www.i-have-a-dreambox.com/wbb2/thread.php?postid=1691077#post1691077'>here</a>. Additionally the final version of "Don't cry" should contain all necessary files.<br>
<br>
<h1>Installation of Project Valerie</h1>
<h2>Special hint for Newnigma2-lean-Image users (e.g. Dreambox DM800)</h2>
</li><li>in order to install PVMC using the supposed method with <code>opkg</code> an additional library is needed that might be missing on your image<br>
</li><li>Installing python-json (2.7.2-<a href='https://code.google.com/p/project-valerie/source/detail?r=2'>r2</a>.17-dream2-newnigma2_1) before installing PVMC</li></ul>

<h2>Setp-by-step installation guide</h2>
You want to install and use Project Valerie, but you don´t know how? Here you will find all necessary information!<br>
<br>
1. Depending on the architecture of your box download the latest version of Project Valerie from our <a href='http://code.google.com/p/project-valerie/downloads/list'>download-page</a>:<br>
<br>
<ul><li>for all mipsel based settop boxes (e.g. Dreambox DM800) with OpenEmbedded 1.6 (e.g. Newnigma2 v3xx):<br>
<blockquote><code>project-valerie_&lt;rev&gt;_mipsel_oe16.ipk</code>
</blockquote></li><li>for all mipsel based settop boxes with OpenEmbedded 1.5 (e.g. Newnigma2 v2xx):<br>
<blockquote><code>project-valerie_&lt;rev&gt;_mipsel_oe15.ipk</code>
</blockquote></li><li>for all other boxes (z.B. Kathrein UFS910)<br>
<blockquote><code>project-valerie_&lt;rev&gt;_sh4.ipk</code></blockquote></li></ul>

2. Upload <code>project-valerie_&lt;rev&gt;_&lt;version&gt;.ipk</code> to your box (e.g. with WinSCP or via FTP). <br>
Alternately you can download Project Valerie via command line in a Telnet or SSH session: <br><br>
<i><code>root@dm8000:~# wget http://project-valerie.googlecode.com/files/project-valerie_&lt;rev&gt;_&lt;version&gt;.ipk</code></i>  <br><br>
3. After that you are ready for installing Project Valerie. You can do it via the MediaScanner (Expansion panel), or via a SSH/Telnet Session:  <br><br>
<i><code>root@dm8000:~# opkg install &lt;path to file&gt;/project-valerie_&lt;rev&gt;_&lt;version&gt;.ipk</code></i>   <br><br>
(<b>Important:</b> do <i>not</i> install the package using "ipkg" since this might break your installation! Always install the package using "opkg" as shown above!)<br>
Finally reboot Enigma2 - the Project Valerie assistant will guide you through the first steps. Project Valerie is now ready for use!<br>
<br><br>
<b>Note</b><br>
Project Valerie will be installed in the following directory, which can currently <b>not</b> be configured:<br>
<ul><li><code>/usr/lib/enigma2/python/Plugins/Extensions/ProjectValerie</code> (the application itself)<br>
Additionally the following default directories for configuration files, database, log-files and cache are used, which can be adapted in the settings:<br>
</li><li><code>/hdd/valerie</code> (config and database)<br>
</li><li><code>/tmp/valerie</code> (log and cache)<br>
<br><br>
<h1>Remove of Project Valerie</h1>
You can remove Project Valerie by using one of the following ways:<br>
</li><li>select the de-installation option for Project Valerie through the Enigma2 extension panel<br>
</li><li>execute the following command through an SSH/Telnet-session:<br>
<i><code>root@dm8000:~# opkg remove project-valerie*</code></i>
<br><br>
<h1>Update Policy</h1>
Since PVMC <a href='https://code.google.com/p/project-valerie/source/detail?r=960'>r960</a> a new update policy has been introduced in order to avoid breaks and crashes for people who just want to use PVMC "as is" without the need of having the latest fancy development enhancements. You can now choose between the following options:<br>
</li><li>"Development builds" (a.k.a. "Nigtly builds") => these are builds based on the latest development enhancements, and hence contain the latest features. The major drawback of these builds is, that they may contain severe bugs and cause PVMC to crash<br>
</li><li>"Stable builds" (a.k.a. "Release builds") => such revisions have been found to be stable, but don't contain the latest enhancements</li></ul>

You can change the desired type of release to be used in the global PVMC settings:<br>
<ul><li>in the WebIf select "Options" => "Global Settings" => "Check for updates of type:"<br>
</li><li>in the PVMC E2 GUI select "System" => "Settings" => "Check for updates of type:"</li></ul>

<b>Please note:</b><br>
If you updated manually to a newer nightly build but your update setting is configured to use "Release" builds you currently will always be asked to "downgrade" to latest release build.