import urllib.request
from urllib.error import HTTPError,URLError
from bs4 import BeautifulSoup
import time
import re
from fake_useragent import UserAgent

def dump(target):
    imageExt = ["jpeg", "exif", "tiff", "gif", "bmp", "png", "ppm", "pgm", "pbm", "pnm", "webp", "hdr", "heif",
                "bat",
                "bpg", "cgm", "svg"]
    print("Searching emails... please wait")
    ua = UserAgent()
    print("This operation may take several minutes")
    try:
        count = 0
        listUrl = []
        req = urllib.request.Request(
            target,
            data=None,
            headers={
                'User-Agent': ua.random
            })

        try:
            conn = urllib.request.urlopen(req, timeout=5)

        except TimeoutError:
            raise ValueError('Timeout ERROR')

        except (HTTPError, URLError):
            raise ValueError(target + '--- Bad Url...')

        status = conn.getcode()
        contentType = conn.info().get_content_type()

        if (status != 200 or contentType == "audio/mpeg"):
            raise ValueError(target + '--- Bad Url...')

        html = conn.read().decode('utf-8')

        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", html)

        for email in emails:
            if (email not in listUrl and email[-3:] not in imageExt):
                count += 1
                print(str(count) + " - " + email)
                listUrl.append(email)
                print(email)

        soup = BeautifulSoup(html, "lxml")
        links = soup.find_all('a')

        print("They will be analyzed " + str(len(links) + 1) + " Urls...")
        time.sleep(2)

        for tag in links:
            link = tag.get('href', None)
            if link is not None:
                try:
                    if (link[0:4] == 'http'):
                        req = urllib.request.Request(
                            link,
                            data=None,
                            headers={
                                'User-Agent': ua.random
                            })

                        try:
                            f = urllib.request.urlopen(req, timeout=10)

                        except TimeoutError:
                            print(target + "--- Bad Url..")
                            time.sleep(2)
                            pass

                        except (HTTPError, URLError):
                            print(target + "--- Bad Url..")
                            time.sleep(2)
                            pass

                        status = f.getcode()
                        contentType = f.info().get_content_type()

                        if (status != 200 or contentType == "audio/mpeg"):
                            print(target + "--- Bad Url..")
                            time.sleep(2)
                            pass

                        s = f.read().decode('utf-8')

                        emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}", s)

                        for email in emails:
                            if (email not in listUrl and email[-3:] not in imageExt):
                                count += 1
                                print(email)
                                listUrl.append(email)
                except Exception:
                    pass

        print("")
        print("***********************")
        print("Finish: " + str(count) + " emails were found")
        print("***********************")


    except KeyboardInterrupt:
        pass

    except Exception as e:
        pass