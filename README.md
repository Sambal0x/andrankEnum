# andrankEnum
Purpose: Tool to get the top android apps on Google App store for bug bounty purpose (*cough playstore...*)

# How the tool works:
Scrap https://www.androidrank.org and finds the package name

With the package name, you can now use chrome extension (APK downloader) to get the direct APK download link
https://chrome.google.com/webstore/detail/apk-downloader/fgljidimohbcmjdabiecfeikkmpbjegm?hl=en

No more BS downloading APK from mobile device and extract it via ADB pull.

Thanks @initstring for the help with go.py


## Extra tools
* **go.py** - Extracts all the URLs to for downloading the APK files
* **deeplink_check.sh** - Extracts any handlers from AndroidManifest and search the decompiled APK folder for interesting deeplinks
