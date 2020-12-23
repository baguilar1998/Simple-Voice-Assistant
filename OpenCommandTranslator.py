import webbrowser
import subprocess


class OpenCommandTranslator:

    __software_map = {
        "GOOGLE CHROME": 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe',
        "FL STUDIO": 'C:\\Users\\Brian Kenji Aguilar\\Desktop\\FL Studio\\FL64 (scaled).exe',
    }

    __web_map = {
        "FACEBOOK": 'www.facebook.com',
        "YOUTUBE": 'www.youtube.com',
        "INSTAGRAM": 'www.instagram.com',
        "MESSENGER": 'www.messenger.com/',
        "SPOTIFY": 'https://open.spotify.com/'
    }

    @staticmethod
    def open(name):
        if name in OpenCommandTranslator.__software_map:
            program_path = OpenCommandTranslator.__software_map[name]
            subprocess.call([program_path])
        elif name in OpenCommandTranslator.__web_map:
            website = OpenCommandTranslator.__web_map[name]
            webbrowser.open(website)

    @staticmethod
    def program_exists(name):
        return name in OpenCommandTranslator.__software_map \
               or name in OpenCommandTranslator.__web_map
