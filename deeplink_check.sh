#!/bin/bash
#
# Purpose: To quickly find any interesting deep links across in a large folder of decompiled APK directories
#
# Note: After extracting all APKs in the same directory, drop this script in the directory
#!/bin/bash

OUTFILE=deeplink_out.txt

for directory in $(ls); do
	if [[ -d $directory ]]; then
		echo [+] Checking $directory | tee -a $OUTFILE
		for i in $(cat $directory/AndroidManifest.xml | grep -o 'android:scheme=".*"' --color | grep -o '".*"' | grep -v "http.*" | tr -d '"' | sort | uniq ); do 
			(echo [+] Found Handler = \"$i\"; unbuffer grep -irn $i:// --color $directory) | tee -a $OUTFILE; 
		done
		echo ----------------------- | tee -a $OUTFILE
	fi
done
