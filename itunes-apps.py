from os.path import expanduser
import glob
import zipfile
import plistlib
import itunes

mobileApps = glob.glob(expanduser("~") + '/Music/iTunes/iTunes Media/Mobile Applications/*.ipa')

output = '<table><tr><th>Icon</th><th>Name</th><th>Genre</th><th>Developer</th><th>Description</th></tr>'

for app in mobileApps:
  currentIPA = file(app)
  ipaContents = zipfile.ZipFile(currentIPA)
  plistFile = ipaContents.read('iTunesMetadata.plist')
  plistContents = plistlib.readPlistFromString(plistFile)
  
  currentApp = itunes.lookup(plistContents['itemId'])
  
  description = currentApp.get_description().replace("\n","<br />\n")

  output += '<tr>'
  output += '<td><img src="' + currentApp.get_artwork()['60'] + '" height="57" width="57"></td>' 
  output += '<td><a href="' + currentApp.get_url() + '">' + currentApp.get_name() + '</a></td>'
  output += '<td>' + currentApp.get_genre() + '</td>'
  output += '<td>' + str(currentApp.get_artist()) + '</td>'
  output += '<td>' + description + '</td>'
  output += '</tr>'

  ipaContents.close()

output += '</table>'

print output
