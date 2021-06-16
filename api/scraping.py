import requests
from bs4 import BeautifulSoup
from .models import Mushroom, WikiUrl, CAP_SHAPES, HYMENIUM_TYPES, GILL_TYPES, STIPE_CHARACTERS, SPOREPRINT_COLORS, \
    ECOLOGIES, EDIBILITY_TYPES

class Scraper:
    """A class to handle scraping mushroom data from Wikipedia"""
    wikiUrls = []

    def __init__(self):
        self.wikiUrls = WikiUrl.objects.all()

    def create_fungus(self, my_url):
        soup = self.parse_page(my_url)

        fungus = Mushroom(
            name=self.get_name(soup),
            image_link=self.get_image_url(soup),
            wiki_link=my_url,
            kingdom=self.get_kingdom(soup),
            division=self.get_division(soup),
            cclass=self.get_class(soup),
            order=self.get_order(soup),
            family=self.get_family(soup),
            genus=self.get_genus(soup),
            species=self.get_species(soup),
            cap_shapes=self.get_cap_shapes(soup),
            hymenium_types=self.get_hymenium_types(soup),
            gill_types=self.get_gill_types(soup),
            stipe_characters=self.get_stipe_characters(soup),
            sporeprint_colors=self.get_sporeprint_colors(soup),
            ecologies=self.get_ecologies(soup),
            edibility=self.get_edibility(soup)
        )
        return fungus

    def get_random_fungus(self):
        return self.create_fungus(self.get_random_url())

    def get_random_url(self):
        return WikiUrl.objects.order_by("?").first()

    def parse_page(self, myurl):
        print(myurl)
        page = requests.get(myurl)
        print(page)
        soup = BeautifulSoup(page.content, 'html.parser')
        return soup

    def get_image_url(self, soup):
        img = None
        table = soup.find('table', {'class': 'infobox biota'})

        hits = table.findAll('img')
        if hits:
            hit = hits[0]['src']
            img = 'https:' + hit
        return img

    def get_image_page(self, soup):
        base = 'http://en.wikipedia.com'
        img_page = base + soup.find('a', class_='image')['href']
        img_page = requests.get(img_page)
        return img_page

    def get_photographer(self, soup):
        base = 'http://en.wikipedia.com'
        img_page = base + soup.find('a', class_='image')['href']
        img_page = requests.get(img_page)

        photo_soup = BeautifulSoup(img_page.content, 'html.parser')
        photog = photo_soup.find('td', {'id': 'fileinfotpl_aut'})

        if photog is not None:
            photographer = photog.findNext('td').text
        else:
            photographer = "unknown"
        return photographer.strip()

    def get_name(self, soup):
        try:
            name = soup.find('h1', {'id': 'firstHeading'}).text
        except:
            try:
                name = soup.select('h1#firstHeading i')[0].text
            except:
                name = ""

        return name

    def get_species(self, soup):
        species = soup.find('h1', {'id': 'firstHeading'}).text

        return species

    def get_genus(self, soup):
        hit = soup.find('span', {'class': 'genus'})
        if hit:
            genus = hit.find('a')
            if genus:
                return genus.text
            else:
                genus = hit.find('b')
                if genus:
                    return genus.text
        else:
            table = soup.find('table', {'class': 'infobox biota'})
            if table:
                tds = table.find_all('td')
                if tds:
                    for td in tds:
                        if 'Genus' in td.text:
                            links = td.find('a')
                            if links:
                                return links.text
                            else:
                                bs = td.find('b')
                                if bs:
                                    return bs.text

    def get_family(self, soup):

        family = soup.find('table', {'class': 'infobox biota'}).find_all('tr')[
            8].find('a')
        if family:
            return family.text
        else:
            family = soup.find(
                'table', {'class': 'infobox biota'}).find_all('tr')[8]
            if family:
                return family.text
            else:
                family = soup.find('table', {'class': 'infobox biota'}).find_all('tr')[
                    8].find('span', {'class': 'genus'}).find('b')
                if family:
                    return family.text
                else:
                    return ""

    def get_order(self, soup):
        order = soup.find('span', {'class': 'order'})
        if order:
            order = order.find('a').text
        else:
            order = soup.find('table', {'class': 'infobox biota'}).find_all('tr')[
                7].find('a').text
            if order:
                return order
            else:
                order = "unknown"
        return order

    def get_class(self, soup):
        class_ = soup.find('table', {'class': 'infobox biota'}).find_all('tr')[
            6].find('a').text
        return class_

    def get_division(self, soup):
        try:
            division = soup.find('table', {'class': 'infobox biota'}).find_all('tr')[
                5].find('a').text
        except:
            division = "unk"
        return division

    def get_kingdom(self, soup):
        try:
            kingdom = soup.find('table', {'class': 'infobox biota'}).find_all('tr')[
                4].find('a').text
        except:
            kingdom = "unk"
        return kingdom

    def get_hymenium_types(self, soup):
        hymeniums = []
        hits = soup.find('a', {'title': 'Hymenium'})
        if hits:
            # print("found hymenium...")
            bs = hits.parent.find_all('b')
            if len(bs) > 0:
                # print("found bolded items...")
                for b in bs:
                    if b.text in HYMENIUM_TYPES:
                        # print(b.text)
                        hymeniums.append(b.text)

        return hymeniums

    def get_cap_shapes(self, soup):
        shapes = []
        hits = soup.find('a', {'title': 'Pileus (mycology)'})
        if hits:
            bs = hits.parent.parent.find_all('b')
            for b in bs:
                if b.text in CAP_SHAPES:
                    shapes.append(b.text)
        else:
            shapes = []
        return shapes

    def get_gill_types(self, soup):
        gill_types = []
        hymenium_hits = soup.find_all('a', {'title': 'Hymenium'})
        if hymenium_hits:
            for hit in hymenium_hits:
                if " is " in hit.parent:
                    hits = hit.parent.find_all('b')
                    for hit in hits:
                        if hit.text in GILL_TYPES:
                            gill_types.append(hit.text)
        return gill_types

    def get_stipe_characters(self, soup):
        stipe_characters = []

        link = soup.find('a', {'title': 'Stipe (mycology)'})
        if link:
            link_parent = link.parent
            if link_parent:
                bs = link_parent.find_all('b')
                if len(bs) > 0:
                    for b in bs:
                        if b.text in STIPE_CHARACTERS:
                            stipe_characters.append(b.text)
        return stipe_characters

    def get_sporeprint_colors(self, soup):
        sporeprint_colors = []
        hits = soup.find('a', {'title': 'Spore print'})
        if hits:
            colors = hits.parent.find_all('b')
            if len(colors) > 0:
                for color in colors:
                    if color.text in SPOREPRINT_COLORS:
                        sporeprint_colors.append(color.text)
        return sporeprint_colors

    def get_ecologies(self, soup):
        ecologies = []
        hits = soup.find_all("td")
        if hits:
            for col in hits:
                if 'ecology is ' in col:
                    ecologies.append(col.text.split()[-1])

        return ecologies

    def get_edibility(self, soup):
        edibilities = []
        # row = soup.find('table', {'class': 'infobox biota'}).findNext('table', class_="infobox").find_all('tr')[8]
        #
        # table = soup.find('table', {'class': 'infobox biota'})

        ps = soup.find_all('p')
        for p in ps:
            if 'edibility' in p.text:
                bs = p.parent.find_all('b')
                if len(bs) > 0:
                    for ed in bs:
                        edibilities.append(ed.text)
        if len(edibilities) < 1:
            table = soup.find_all('table', {'class': 'infobox'})[-1]
            tds = table.find_all('td')
            if tds:
                for td in tds:
                    if "edibility" in td.text:
                        bs = td.parent.find_all('b')
                        if len(bs) > 0:
                            for b in bs:
                                edibilities.append(b.text)
        return edibilities
