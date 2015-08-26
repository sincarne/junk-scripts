from os.path import expanduser
import glob
import zipfile
import plistlib

mobileApps = glob.glob(expanduser("~") + '/Music/iTunes/iTunes Media/Mobile Applications/*.ipa')

for app in mobileApps:
  currentIPA = file(app)
  ipaContents = zipfile.ZipFile(currentIPA)
  plistFile = ipaContents.read('iTunesMetadata.plist')
  plistContents = plistlib.readPlistFromString(plistFile)
  print plistContents['bundleDisplayName']
  ipaContents.close()
