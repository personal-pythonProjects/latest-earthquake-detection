import requests
from bs4 import BeautifulSoup
import textdecor

def data_extraction():
    """
    Date: 02 Jan 2025
    Time: 04:42:15 WIB
    Earthquake Felt: The epicenter of the earthquake was in the sea 8 km south of Kairatu-SBB
    Magnitude: 3.5
    Depth: 10 Km
    Location Coordinates:
                            LS: 3.41
                            BT: 128.37
    BMKG advice: Be careful of possible aftershocks

    :return:
    """

    try:
        contents = requests.get('https://www.bmkg.go.id/')
    except Exception:
        return None

    if contents.status_code == 200:
        # print(contents.text)
        soup = BeautifulSoup(contents.text, 'html.parser')
        title = soup.find('title')
        result = soup.find('p', {'class': 'mt-2 text-sm leading-[22px] font-medium text-gray-primary'})

        result = result.text.split(', ')
        date = result[0]
        time = result[1]

        result = soup.find('span', {'class': 'bg-[#0099001A] text-[#009900] px-4 py-[5px] text-sm rounded-lg font-medium capitalize'})
        earthquake_felt = result.text.upper()
        result = soup.find('p', {'class': 'mt-4 text-xl lg:text-2xl font-bold text-black-primary'})
        location = result.text

        result = soup.find('div', {'class': 'mt-5 flex flex-wrap lg:flex-nowrap gap-3'})
        result = result.findChildren('span')

        magnitude = None
        depth = None
        location_coordinates = None
        ls = None
        bt = None

        for i, res in enumerate(result, start=1):
            if i == 1:
                magnitude = res.text
            elif i == 2:
                depth = res.text
            elif i == 3:
                location_coordinates = res.text.split(' - ')
                ls = location_coordinates[0]
                bt = location_coordinates[1]

        result = soup.find('p', {'class': 'text-sm font-medium text-black-primary'})
        result = result.text.split(': ')
        advice = result[1]



        result = dict()
        result['date'] = date
        result['time'] = time
        result['earthquake_felt'] = earthquake_felt
        result['location'] = location
        result['magnitude'] = magnitude
        result['depth'] = depth
        result['location_coordinates'] = {
            'ls': ls,
            'bt': bt
        }
        result['advice'] = advice


        # print(result)
        return result
    else:
        return None


def display_data(result):
    if result is None:
        print("Data is not found.")
        return

    print('Last Earthquake according to BMKG:')

    print(f"\nDate = {result['date']}")
    print(f"Time = {result['time']}")

    textdecor.separator('-', 100)

    print(f"Status: {result['earthquake_felt']}")
    print(f"Location: {result['location']}")

    textdecor.separator('-', 100)

    print(f"Magnitude: {result['magnitude']}")
    print(f"Depth: {result['depth']}")
    print(f"Coordinate: LS ({result['location_coordinates']['ls']}), "
          f"BT ({result['location_coordinates']['bt']})")

    textdecor.separator('-', 100)

    print(f"BMKG Advice: {result['advice']}.")


# if __name__ == '__main__':
#     print("Hello, I am init class")