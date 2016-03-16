# Introduction #

NOTE: This Guide is not up to date!


# Before we start #

  * All: Java Runtime 6 SE is required.

  * Windows: No extra packages are required.
  * Linux: "mencoder" and "pngquant (Version 1.1, newer ones dont work proberly)" have to be installed.
  * Mac: ???

> Valerie consists of a frontend for you enigma2-receiver and a backend for your PC. <br>
<blockquote>The frontend displays all your movies and titles with coverarts and movie information <br>
and the PC-application collects all the information to your movies from the www.<br></blockquote>

<h1>Installation</h1>

<h2>PC-Application</h2>
Download the newest version of valerie_pc_revXXX.zip where XXX is the version number.<br>
This archive contains the application running on your pc.<br>
Extract the content to a folder of your choice. The main executable is "Valerie.jar"<br>
<br>
<h2>Kathrein/Topfield/Cubrevo/Ipbox/Octagon</h2>
Download the newest version of<br>
enigma2-plugin-extensions-mediacenter_V.V.V_CPU.tar.gz<br>
where V.V.V is the version number and CPU is the string for your box:<br>
<br>
<b>sh</b> = Kathrein ufs910 + ufs922, Topfield HDPVR7700, Cubrevo xx, Ipbox xx, Octagon 10xx<br>
<br>
Extract the folder "<code>MediaCenter</code>" in the tar.gz to the plugin directory "Extensions" on your box. <br>
For example:  /usr/lib/enigma2/python/Plugins/Extensions/<br>
<br>
<h2>Dreambox</h2>
Download the newest version of<br>
project-valerie_V.V.V-DM8XXX_mipsel.ipk<br>
where V.V.V is the version number and XXX is the box type. <br>
The package is available for DM8000 and DM800. <br>
Copy the ipk-file to the box by FTP (/hdd or /var/tmp) <br>
Perform a manual package install. (Newnigma: blue button) <br><br>
Alternative: Use the command line by typing <code>ipkg install "packagename".ipk</code><br>
Example: Dreambox:> ipkg install /temp/project-valerie_1.0.3-DM8000_mipsel.ipk <br>
Reboot the box.<br>
<br>
<h1>Finishing up</h1>
Valerie starts automatically with enigma!<br>
You are now ready to use Project Valerie <br>
How to get your Movie/Series database filled see chapter "PC-Application"