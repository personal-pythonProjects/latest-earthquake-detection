"""
Earthquake detection application
Modularization with Functions
Modularization with Package
"""
import latest_earthquake
import textdecor

if __name__ == '__main__':
    textdecor.separator('*', 100)
    print('Main Application')
    textdecor.separator('*', 100)

    result = latest_earthquake.data_extraction()
    latest_earthquake.display_data(result)
