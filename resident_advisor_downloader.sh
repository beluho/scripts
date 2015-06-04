wget -q -O-  "http://www.residentadvisor.net/xml/podcast.xml"  | grep -o '<enclosure url="[^"]*' | grep -o '[^"]*$' | xargs wget -c -P /Users/lukehodgkinson/Music/

