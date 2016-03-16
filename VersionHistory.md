# Version History #
This wiki page lists the features introduced with each version of project valerie.
Not every revision will be noted here but only the for the end-user important ones like NEW, REMOVED, FIX\_CRASH.
Also major version will be noted here, e.g. Version 1.1, 1.2 and so on.

  * rev1239 **v1.8.0**
    * NEW: added support for start / stop sync over WebIF
    * NEW: added italian translation
    * NEW: added support for SEEN / UNSEEN in WebIF
    * NEW: assignment of episodes to wrong TV show can now be fixed in WebIF by editing "ParentID"
    * NEW: added date and clock to blackDon / support german special characters in font used by blackDon
    * NEW: eased specification of user-arts in WebIF (no leading "user://" needed any more)
    * NEW: create backup of current database prior making any modifications
    * NEW: improve sync performance up to 20% by skipping sync of english attributes if sync language != english
    * NEW: in case of "useFolder" consider both `IMDb-ID` and `TheTvDb-ID` specified as sync hints in directory name
    * NEW: for E2 recorded TV show only fall-back to sync as movie if containing folder is explicitly set to "MOVIE\_AND\_TV"
    * NEW: for E2 recorded TV show consider season and episode numbers in file name in order to overcome rubbish stored in related meta files
    * NEW: enhanced logfile structure in case of debug mode = "high"
    * FIX: sync of all TV shows should be possible again (workaround for new IMDb result format)
    * FIX: revised german tranlsation
    * FIX: avoid crash on startup in case no internet connection is available
    * FIX: fixed update mechanism
    * FIX: configuration of show / hide plugins considered again
    * FIX: don't try to sync E2 recorded movie contained in a "MOVIE" directory as TV show
    * FIX: support TV show specials (stored with season "0" in TheTvDB) correctly
    * FIX: support season / episode located at the very beginning of a file name correctly
    * FIX: dozens more... :-)
  * rev1162 **v1.7.0**
    * NEW: Add support for global enigma2 Skins (e.g. dmm-HDr2 für gp3 by `JackDaniel`)
    * NEW: Add support for Bluray movie detection
    * NEW: Add support for User ID in regards to SEEN/UNSEEN
    * FIX: Fix m2ts playback
    * FIX: Update German Language translation
  * rev1145 **v1.6.0**
    * NEW: A lot e.g. Sync in WebIf
    * FIX: Many ;-)
  * rev1001 **v1.5.1**
    * NEW: This is a temporary release to update all version to rev1000 so the db is converted. A real release will follow.
  * rev984 **v1.4.0**
    * NEW: The Sync plugin has been moved to the dmc\_plugin dir
    * NEW: The webif has been reworked
    * FIX: Many fixes ;-)
  * rev960 **v1.3.0**
    * NEW: Initial version with the new update mechanism
  * rev887 **v1.2.3**
    * NEW: Adding a trailerplugin to the mix (YYTrailer by Dr. Best)
  * rev881 **v1.2.2**
    * NEW: Coverflow displays the plot on press KEY\_INFO



Note to developers:
It would make sense that this page is being displayed when valerie detects a new version. And also that this page is being parsed to only present users the major versions instead of every nightly build.
For that it would be important that the syntax remains the same for every entry.