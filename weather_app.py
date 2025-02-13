import streamlit as st
import requests

# Function to get weather data
def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    return response.json()

# Streamlit app
def main():
    st.title("Weather App")
    
    api_key = st.text_input("Enter your OpenWeatherMap API key:")
    city = st.text_input("Enter city name:")
    
    if st.button("Get Weather"):
        if api_key and city:
            weather_data = get_weather(city, api_key)
            if weather_data["cod"] != "404":
                main = weather_data["main"]
                wind = weather_data["wind"]
                weather_desc = weather_data["weather"][0]["description"]
                
                st.write(f"**Temperature:** {main['temp']}°C")
                st.write(f"**Humidity:** {main['humidity']}%")
                st.write(f"**Pressure:** {main['pressure']} hPa")
                st.write(f"**Weather Description:** {weather_desc.capitalize()}")
                st.write(f"**Wind Speed:** {wind['speed']} m/s")
            else:
                st.error("City Not Found!")
        else:
            st.error("Please enter both API key and city name.")

if __name__ == "__main__":
    main()