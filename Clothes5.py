import streamlit as st
import requests
import json

API_key_OpenWeather = 'fd52fa375b7a291780785bd3a1b46caa'

# Function to get geolocation ID and weather data, then provide clothing recommendation
def get_weather_and_clothing(city):
    # Geolocation ID
    url_geocoding = f'http://api.openweathermap.org/geo/1.0/direct?q={city},CH&limit=5&appid={API_key_OpenWeather}'
    r1 = requests.get(url_geocoding)
    geocoding_data = r1.json()
    lat = geocoding_data[0]['lat']
    lon = geocoding_data[0]['lon']

    # Weather Data
    url_forecast = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_key_OpenWeather}&units=metric'
    r2 = requests.get(url_forecast)
    weather = r2.json()
    weather_text = weather['list'][0]['weather'][0]['main']
    weather_temp = weather['list'][0]['main']['temp']

    # Initialize clothing recommendation variables
    outer_layer = ""
    upper_body = ""
    lower_body = ""
    shoes = ""
    accessories = []  # Accessories as a list for easier use

    # Example clothing recommendation logic based on weather_temp and weather_text
    if weather_temp < -10:  # first if for distinction of temperatire brackets
        if weather_text in ["Rain", "Thunderstorm", "Drizzle",
                            "Snow"]:  # if and else in the if loop to see if Waterproof clothes are needed
            outer_layer = "Heavy insulated waterproof and windproof jacket/parka/coat"
            upper_body = "Heavy sweater/fleece, thermal layer"
            lower_body = "Insulated pants, thermal leggings"
            shoes = "Insulated waterproof boots"
            accessories.extend(["Insulated gloves", "Thermal socks", "Warm hat", "Scarf"])
        else:
            outer_layer = "Heavy insulated windproof jacket/parka/coat"
            upper_body = "Heavy sweater/fleece, thermal layer"
            lower_body = "Insulated pants, thermal leggings"
            shoes = "Insulated boots"
            accessories.extend(["Insulated gloves", "Thermal socks", "Warm hat", "Scarf"])

    elif -10 <= weather_temp < 0:
        if weather_text in ["Rain", "Thunderstorm", "Drizzle", "Snow"]:
            outer_layer = "Heavy insulated waterproof and windproof jacket/parka/coat"
            upper_body = "Heavy sweater/fleece, thermal layer"
            lower_body = "Insulated pants/thick jeans/thermal leggings"
            shoes = "Insulated waterproof boots"
            accessories.extend(["Insulated gloves", "Thermal socks", "Warm hat", "Scarf"])
        else:
            outer_layer = "Heavy insulated windproof jacket/parka/coat"
            upper_body = "Heavy sweater/fleece, thermal layer"
            lower_body = "Insulated pants/thick jeans/thermal leggings"
            shoes = "Insulated boots"
            accessories.extend(["Insulated gloves", "Thermal socks", "Warm hat", "Scarf"])

    elif 0 <= weather_temp < 5:
        if weather_text in ["Rain", "Thunderstorm", "Drizzle", "Snow"]:
            outer_layer = "Medium-weight waterproof jacket/coat"
            upper_body = "Heavy sweater/fleece/thermal layer"
            lower_body = "Jeans/insulated pants"
            shoes = "Boots/other shoes"
            accessories.extend(["Gloves", "Hat", "Scarf"])
        else:
            outer_layer = "Medium-weight jacket/coat"
            upper_body = "Heavy sweater/fleece/thermal layer"
            lower_body = "Jeans/insulated pants"
            shoes = "Boots/other shoes"
            accessories.extend(["Gloves", "Hat", "Scarf"])

    elif 5 <= weather_temp < 10:
        if weather_text in ["Rain", "Thunderstorm", "Drizzle", "Snow"]:
            outer_layer = "Medium-weight waterproof jacket/coat"
            upper_body = "Heavy sweater/fleece/thermal layer"
            lower_body = "Jeans/insulated pants"
            shoes = "Sneakers/other shoes/boots"
            accessories.extend(["Gloves", "Hat", "Scarf"])
        else:
            outer_layer = "Medium-weight jacket/coat"
            upper_body = "Heavy sweater/fleece/thermal layer"
            lower_body = "Jeans/insulated pants"
            shoes = "Sneakers/boots/other shoes"
            accessories.extend(["Gloves", "Hat", "Scarf"])

    elif 10 <= weather_temp < 20:
        if weather_text in ["Rain", "Thunderstorm", "Drizzle", "Snow"]:
            outer_layer = "Light waterproof jacket/hoodie"
            upper_body = "Light sweater/long-sleeved shirt"
            lower_body = "Jeans/light pants/pants"
            shoes = "Sneakers/other shoes"
            accessories.extend(["Light scarf"])
        else:
            outer_layer = "Light waterproof jacket/hoodie"
            upper_body = "Light sweater/long-sleeved shirt"
            lower_body = "Jeans/light pants/pants"
            shoes = "Sneakers/other shoes"
            accessories.extend(["Light scarf"])

    elif 20 <= weather_temp < 25:
        if weather_text == "Clear":
            upper_body = "T-shirt/shirt/light sweater/long-sleeved shirt"
            lower_body = "Light pants/pants/shorts"
            shoes = "Sneakers/sandals"
            accessories.extend(["Hat"])
        else:
            upper_body = "T-shirt/shirt/light sweater/long-sleeved shirt"
            lower_body = "Light pants/pants/shorts"
            shoes = "Sneakers/sandals"


    elif 25 <= weather_temp < 30:
        if weather_text == "Clear":
            upper_body = "Short-sleeved shirt/tank top/dress"
            lower_body = "Shorts/skirt/light pants"
            shoes = "Sneakers/sandals"
            accessories.extend(["Hat"])
        else:
            upper_body = "Short-sleeved shirt/tank top/dress"
            lower_body = "Shorts/skirt/light pants"
            shoes = "Sneakers/sandals"


    elif weather_temp >= 30:
        if weather_text == "Clear":
            upper_body = "Short-sleeved shirt/tank top/dress"
            lower_body = "Shorts/skirt"
            shoes = "Open-toed shoes/sandals"
            accessories.extend(["Hat"])
        else:
            upper_body = "Short-sleeved shirt/tank top/dress"
            lower_body = "Shorts/skirt"
            shoes = "Open-toed shoes/sandals"

    # Additional accessories based on weather condition
    if weather_text == "Clear":
        accessories.append("Sunglasses")
    elif weather_text in ["Rain", "Thunderstorm", "Drizzle"]:
        accessories.append("Umbrella")
    elif weather_text == "Snow":
        accessories.append("Snow boots")

    # Return the results
    return weather_text, weather_temp, outer_layer, upper_body, lower_body, shoes, accessories


# Initialize session state
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False

# Making a button with a text field that you can submit the city in.
def submit():
    st.session_state['submitted'] = True
    # Make sure to set 'city' key here
    st.session_state['city'] = st.session_state['city_input']
    results = get_weather_and_clothing(st.session_state['city_input'])
    st.session_state['results'] = results

# Streamlit app
def main():
    st.title("NimbusWardrobe")

    # Input of the wardrobe items (Source: https://docs.streamlit.io/library/api-reference/widgets/st.multiselect)
    outer_layer_selections = st.multiselect(
        'Outer Layer',
        ['Heavy insulated waterproof and windproof jacket/parka/coat', 'Heavy insulated windproof jacket/parka/coat',
         'Medium-weight waterproof jacket/coat', 'Medium-weight jacket/coat', 'Heavy sweater/fleece/thermal layer',
         'Light waterproof jacket/hoodie'])
    st.session_state['outer_layer_selections'] = outer_layer_selections

    # Upper Body Selection
    upper_body_selections = st.multiselect(
        'Upper Body',
        ['Heavy sweater/fleece, thermal layer', 'Heavy sweater/fleece/thermal layer', 'Light sweater/long-sleeved shirt',
         'T-shirt/shirt/light sweater/long-sleeved shirt', 'Short-sleeved shirt/tank top/dress'])
    st.session_state['upper_body_selections'] = upper_body_selections

    # Lower Body Selection
    lower_body_selections = st.multiselect(
        'Lower Body',
        ['Insulated pants, thermal leggings', 'Insulated pants/thick jeans/thermal leggings', 'Jeans/insulated pants',
         'Jeans/light pants/pants', 'Light pants/pants/shorts', 'Shorts/skirt/light pants', 'Shorts/skirt'])
    st.session_state['lower_body_selections'] = lower_body_selections

    # Shoes Selection
    shoes_selections = st.multiselect(
        'Shoes',
        ['Insulated waterproof boots', 'Insulated boots', 'Boots/other shoes', 'Sneakers/other shoes/boots',
         'Sneakers/boots/other shoes', 'Sneakers/other shoes', 'Sneakers/sandals', 'Open-toed shoes/sandals'])
    st.session_state['shoes_selections'] = shoes_selections

    # Accessories Selection
    accessories_selections = st.multiselect(
        'Accessories',
        ['Sunglasses', 'Umbrella', 'Scarf', 'Light Scarf', 'Hat', 'Warm hat', 'Gloves',
         'Insulated gloves', 'Thermal socks', 'Snow boots'])
    st.session_state['accessories_selections'] = accessories_selections


    if not st.session_state['submitted']:
        # First "Page": City Input
        first_page_background = "https://wallpapercave.com/wp/wp11789974.jpg"
        set_background_image(first_page_background)

        st.session_state['city_input'] = st.text_input("Enter the name of the city:")
        submit_button = st.button("Submit", on_click=submit)


    if st.session_state['submitted']:
        city_name = st.session_state.get('city', '')  # Provide a default empty string if 'city' key doesn't exist
        weather_text, weather_temp, outer_layer, upper_body, lower_body, shoes, accessories = st.session_state.get(
            'results', ('', '', '', '', '', '', []))


    # Set the background image based on the weather_text
    set_background_image(weather_text)

    # Prepare user wardrobe selections for filtering
    user_wardrobe = {
        'Outer Layer': st.session_state.get('outer_layer_selections', []),
        'Upper Body': st.session_state.get('upper_body_selections', []),
        'Lower Body': st.session_state.get('lower_body_selections', []),
        'Shoes': st.session_state.get('shoes_selections', []),
        'Accessories': st.session_state.get('accessories_selections', [])
    }

    # Prepare recommendations for filtering
    weather_recommendations = {
        'Outer Layer': outer_layer,
        'Upper Body': upper_body,
        'Lower Body': lower_body,
        'Shoes': shoes,
        'Accessories': accessories
    }

    # Filter recommendations
    filtered_recommendations = filter_recommendations(weather_recommendations, user_wardrobe)

    # Display filtered recommendations in a semi-transparent text box
    st.markdown(
        f"""
            <div class="textbox">
                <h2>Weather in {city_name}</h2>
                <p>Condition: {weather_text}</p>
                <p>Temperature: {weather_temp}°C</p>
                <h2>Clothing Recommendations</h2>
                <ul>
                    <li>Outer Layer: {filtered_recommendations['Outer Layer']}</li>
                    <li>Upper Body: {filtered_recommendations['Upper Body']}</li>
                    <li>Lower Body: {filtered_recommendations['Lower Body']}</li>
                    <li>Shoes: {filtered_recommendations['Shoes']}</li>
                    <li>Accessories: {filtered_recommendations['Accessories']}</li>
                </ul>
            </div>
            """,
        unsafe_allow_html=True
    )

    if st.button("Back"):
        st.session_state['submitted'] = False


def set_background_image(weather_text):
    # Define background images for different weather conditions
    background_images = {
        "Clear": "https://clarksvillenow.sagacom.com/files/2020/11/shutterstock_286242953-1200x768.jpg",
        "Rain": "https://dgiqb6oe6guf5.cloudfront.net/wp-content/uploads/2023/01/rain-allergies-1280x853.jpg",
        "Snow": "https://static01.nyt.com/images/2019/11/26/us/26holiday-weather01sub/26holiday-weather01sub-superJumbo.jpg",
        "Clouds": "https://cdn.agriland.ie/uploads/2020/05/FS2E5-18_25_18-Clouds-Sky-Agriland20.jpg",
        "Thunderstorm": "https://www.kentonline.co.uk/_media/img/YT98G6JK5O7BHGPRYTQQ.jpg",
    }

    # Select the appropriate background image URL
    background_image_url = background_images.get(weather_text, "https://img.freepik.com/premium-photo/beautiful-cloudscape-nature-single-white-cloud-blue-sky-background_35927-644.jpg")

    # Set the background image using custom CSS in Streamlit's markdown
    st.markdown(
        f"""
            <style>
            .stApp {{
                background-image: url({background_image_url});
                background-size: cover;
            }}
            .textbox {{
                background-color: rgba(255, 255, 255, 0.85);  /* White background with 50% opacity */
                border-radius: 10px;
                padding: 10px;
            }}
            </style>
            """,
        unsafe_allow_html=True
    )

def filter_recommendations(recommendations, user_selections):
    filtered_recommendations = {}
    for category, recommendation in recommendations.items():
        if category != 'Accessories':
            if recommendation in user_selections[category]:
                filtered_recommendations[category] = recommendation
            else:
                filtered_recommendations[category] = "Appropriate item not in wardrobe"
        else:
            # For Accessories, check each item in the list
            filtered_accessories = [item for item in recommendation if item in user_selections[category]]
            if filtered_accessories:
                filtered_recommendations[category] = ', '.join(filtered_accessories)
            else:
                filtered_recommendations[category] = "Appropriate items not in wardrobe"
    return filtered_recommendations
    
if __name__ == "__main__":
    main()
