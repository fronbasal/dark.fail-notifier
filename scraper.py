from requests_html import HTMLSession


class DarkFailScraper:
    def __init__(self, site: str, initial_fetch=True):
        """
        Initialize a new DarkFailScraper
        :param site: site to fetch (e.g. empire)
        :param initial_fetch: whether to fetch initial data
        """
        self.url = f"https://dark.fail/{site}"
        self.session = HTMLSession()
        self.session.headers.update(
            {
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
            }
        )
        self.onion_link = None
        self.last_online = None
        self.is_online = False
        self.fetch()

    def fetch(self):
        """
        fetch the newest status from dark.fail
        :return: whether the value has changed
        """
        res = self.session.get(self.url)
        data = res.html.find(".status0") or res.html.find(".status2")
        if len(data) > 0:
            data_content = data[0].text
            onion_link, self.last_online = [
                s.strip() for s in str(data_content).split("- Last Online: ")
            ]
        else:
            onion_link = res.html.find(".status1", first=True).text.strip()
            self.last_online = None
        is_online = res.html.find(".site_online", first=True).text != "No."
        if self.is_online != is_online or self.onion_link != onion_link:
            self.onion_link = onion_link
            self.is_online = is_online
            return True
        return False
