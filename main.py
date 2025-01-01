"""
Earthquake detection application
Modularization with Functions
"""


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

    result = dict()
    result['date'] = '02 Jan 2025'
    result['time'] = '04:42:15 WIB'
    result['earthquake_felt'] = 'The epicenter of the earthquake was in the sea 8 km south of Kairatu-SBB'
    result['magnitude'] = 3.5
    result['depth'] = 10
    result['location_coordinates'] = {
        'ls': 3.41,
        'bt': 128.37
    }
    result['advice'] = "Be careful of possible aftershocks"


    # print(result)
    return result


def display_data(result):
    print('Last Earthquake according to BMKG')
    print(f"Date {result['date']}")
    print(f"Time {result['time']}")
    print()
    print(f"--- Earthquake Felt ---")
    print(f"{result['earthquake_felt']}")
    print()
    print(f"Magnitude: {result['magnitude']}")
    print(f"Depth: {result['depth']}")
    print(f"Location: LS ({result['location_coordinates']['ls']}), "
          f"BT ({result['location_coordinates']['bt']})")
    print(f"BMKG Advice: {result['advice']}")


if __name__ == '__main__':
    print('Main Application')

    result = data_extraction()

    display_data(result)
