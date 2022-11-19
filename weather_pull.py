import pandas as pd


def pull_weather_data( location, date_start, date_end ):

    #url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/" + location + "/" + date_start + "/" + date_end + "?unitGroup=us&include=days&key=BR6TWPCFMB74JTBPC2BL8RABT&contentType=csv"
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Calistoga/2022-11-29/2022-12-02?unitGroup=us&include=days&key=BR6TWPCFMB74JTBPC2BL8RABT&contentType=csv"
    print(url)

    weather_data = pd.read_csv(url)

    return weather_data