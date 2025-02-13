<<<<<<< HEAD
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
=======
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
    # Add custom CSS
    st.markdown(
        """
        <style>
        .main {
            background-color: #ff5733;
            padding: 20px;
            border-radius: 20px;
        }
        .title {
            color: #4CAF50;
            font-family: 'Arial', sans-serif;
            text-align: center;
        }
        .input {
            margin-bottom: 10px;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 5px;
        }
        .result {
            background-color: #000000 ;
            padding: 10px;
            border-radius: 5px;
            margin-top: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="title">Weather App</h1>', unsafe_allow_html=True)
    
    api_key = "0387870ef1a8413e0ca6cd30bca3d94f"
    city = st.text_input("Enter city name:", key="city_input", help="Enter the name of the city you want to check the weather for.")
    
    if st.button("Get Weather", key="get_weather_button"):
        if api_key and city:
            weather_data = get_weather(city, api_key)
            if weather_data["cod"] != "404":
                main = weather_data["main"]
                wind = weather_data["wind"]
                weather_desc = weather_data["weather"][0]["description"]
                
                st.markdown(
                    f"""
                    <div class="result">
                        <p><strong>Temperature:</strong> {main['temp']}°C</p>
                        <p><strong>Humidity:</strong> {main['humidity']}%</p>
                        <p><strong>Pressure:</strong> {main['pressure']} hPa</p>
                        <p><strong>Weather Description:</strong> {weather_desc.capitalize()}</p>
                        <p><strong>Wind Speed:</strong> {wind['speed']} m/s</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.error("City Not Found!")
        else:
            st.error("Please enter both API key and city name.")

if __name__ == "__main__":
>>>>>>> debd3a2 (1st change)
    main()