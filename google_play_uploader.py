import gmusicapi
import glob
import requests


requests.packages.urllib3.disable_warnings()
mm = gmusicapi.Musicmanager()


#mm.perform_oauth(storage_filepath='/Users/lukehodgkinson/Documents/Scripts/oauth.cred', open_browser=False)
mm.__init__(debug_logging=True, validate=True, verify_ssl=True)



mm.login(oauth_credentials='/Users/lukehodgkinson/Documents/Scripts/oauth.cred')

def upload():
    for song in glob.glob("/Users/lukehodgkinson/Music/*.mp3"):
        mm.upload(song, transcode_quality='320k', enable_matching=True)



upload()
