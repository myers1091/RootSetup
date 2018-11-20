setupATLAS #setup atlas
showVersions root > RootSetup/setuproot.txt #Dump output of Version list to a dummy file
value=$(./RootSetup/setuproot.py) #Reads in dummy file parses to find "recommended" and dumps that version string
eval $(echo lsetup \"root "$value"\") #feed version string into lsetup root <version> 
rm -f RootSetup/setuproot.txt

