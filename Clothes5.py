# Import of the libraries needed for the web application
# Reference: Course Content
import streamlit as st
import requests
import json
import pandas as pd
import sqlite3



# API key for accessing OpenWeatherMap
# Reference:
API_key_OpenWeather = 'fd52fa375b7a291780785bd3a1b46caa'

# Function to get geolocation ID and weather data, then provide clothing recommendation
# Reference:
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



# Initialization of clothing recommendation variables
# Reference: Course Content
    outerwear_items = ''
    topwear_items = ''
    layering_items = ''
    bottomwear_items = ''
    footwear_items = ''
    accessories = []  # Accessories as a list for easier use

# Example clothing recommendation logic based on weather_temp and weather_text
# Reference: Course Content
    if weather_temp < -10:  # first if for distinction of temperatire brackets
        if weather_text in ['Rain', 'Thunderstorm', 'Drizzle', 'Snow']: # If/else to see if Waterproof clothes are needed
            outerwear_items = ['Winter Jacket/Coat']
            topwear_items = ['Long-Sleeve Shirt', 'Long-Sleeve Blouse']
            layering_items =['Heavy Sweater', 'Fleece/Thermal Layer']
            bottomwear_items = ['Pants', 'Jeans', 'Insulated Pants']
            footwear_items = ['Insulated Winter Boots']
            accessories.extend(['Belt', 'Warm Scarf', 'Beanie', 'Insulated Winter Gloves/Mittens', 'Thermal Socks', 'Thermal Legginings/Tights'])
        else:
            outerwear_items = ['Winter Jacket/Coat']
            topwear_items = ['Long-Sleeve Shirt', 'Long-Sleeve Blouse']
            layering_items = ['Heavy Sweater', 'Fleece/Thermal Layer']
            footwear_items = ['Pants', 'Jeans']
            footwear = ['Insulated Winter Boots']
            accessories.extend(['Belt', 'Warm Scarf', 'Beanie', 'Insulated Winter Gloves/Mittens', 'Thermal Socks', 'Thermal Legginings/Tights'])

    elif -10 <= weather_temp < 0:
        if weather_text in ['Rain', 'Thunderstorm', 'Drizzle', 'Snow']: # If/else to see if Waterproof clothes are needed
            outerwear_items = ['Winter Jacket/Coat']
            topwear_items = ['Long-Sleeve Shirt', 'Long-Sleeve Blouse']
            layering_items =['Heavy Sweater', 'Fleece/Thermal Layer']
            bottomwear_items = ['Pants', 'Jeans', 'Insulated Pants']
            footwear_items = ['Insulated Winter Boots']
            accessories.extend(['Belt', 'Warm Scarf', 'Beanie', 'Insulated Winter Gloves/Mittens', 'Thermal Socks', 'Thermal Legginings/Tights'])
        else:
            outerwear_items = ['Winter Jacket/Coat']
            topwear_items = ['Long-Sleeve Shirt', 'Long-Sleeve Blouse']
            layering_items = ['Heavy Sweater', 'Fleece/Thermal Layer']
            bottomwear_items = ['Pants', 'Jeans']
            footwear_items = ['Insulated Winter Boots']
            accessories.extend(['Belt', 'Warm Scarf', 'Beanie', 'Insulated Winter Gloves/Mittens', 'Thermal Socks', 'Thermal Legginings/Tights'])

    elif 0 <= weather_temp < 5:
        if weather_text in ['Rain', 'Thunderstorm', 'Drizzle', 'Snow']: # If/else to see if Waterproof clothes are needed
            outerwear_items = ['Winter Jacket/Coat']
            topwear_items = ['Long-Sleeve Shirt', 'Long-Sleeve Blouse']
            layering_items = ['Heavy Sweater', 'Cardigan']
            bottomwear_items = ['Pants', 'Jeans', 'Insulated Pants']
            footwear_items = ['Insulated Winter Boots']
            accessories.extend(['Belt', 'Warm Scarf', 'Beanie', 'Insulated Winter Gloves/Mittens', 'Thermal Socks', 'Thermal Legginings/Tights'])
        else:
            outerwear_items = ['Winter Jacket/Coat', 'Wool Coat', 'Parka']
            topwear_items = ['Long-Sleeve Shirt', 'Long-Sleeve Blouse']
            layering_items = ['Heavy Sweater', 'Cardigan']
            bottomwear_items = ['Pants', 'Jeans', 'Insulated Pants']
            footwear_items = ['Classic Boots']
            accessories.extend(['Belt', 'Warm Scarf', 'Beanie', 'Standard Gloves/Mittens', 'Thermal Socks', 'Thermal Legginings/Tights'])

    elif 5 <= weather_temp < 10:
        if weather_text in ['Rain', 'Thunderstorm', 'Drizzle', 'Snow']: # If/else to see if Waterproof clothes are needed
            outerwear_items = ['Trench Coat', 'Lightweight Down Jacket', 'Softshell Jacket']
            topwear_items = ['Long-Sleeve Shirt', 'Long-Sleeve Blouse', 'Long-Sleeve Dress']
            layering_items =['Heavy Sweater', 'Cardigan', 'Hoodie']
            bottomwear_items = ['Pants', 'Jeans', 'Insulated Pants']
            footwear_items = ['Insulated Winter Boots', 'Classic Boots']
            accessories.extend(['Belt', 'Warm Scarf', 'Beanie', 'Insulated Winter Gloves/Mittens', 'Thermal Socks', 'Thermal Legginings/Tights'])
        else:
            outerwear_items = ['Trench Coat', 'Lightweight Down Jacket', 'Softshell Jacket', 'Leather Jacket']
            topwear_items = ['Long-Sleeve Shirt', 'Long-Sleeve Blouse', 'Long-Sleeve Dress']
            layering_items =['Cardigan', 'Hoodie', 'Lightweight Sweater']
            bottomwear_items = ['Pants', 'Jeans']
            footwear_items = ['Classic Boots', 'Ankle Boots']
            accessories.extend(['Belt', 'Warm Scarf', 'Standard Gloves/Mittens', 'Thermal Socks'])

    elif 10 <= weather_temp < 20:
        if weather_text in ['Rain', 'Thunderstorm', 'Drizzle', 'Snow']: # If/else to see if Waterproof clothes are needed
            outerwear_items = ['Softshell Jacket', 'Raincoat', 'Windbreaker']
            topwear_items = ['T-Shirt', 'Short-Sleeve Blouse', 'Short-Sleeve Dress']
            layering_items =['Cardigan', 'Hoodie', 'Lightweight Sweater']
            bottomwear_items = ['Pants', 'Jeans']
            footwear_items = ['Ankle Boots', 'Rubber Rain Boots']
            accessories.extend(['Belt', 'Light Scarf', 'Socks'])
        else:
            outerwear_items = ['Leather Jacket', 'Denim Jacket', 'Windbreaker', 'Blazer']
            topwear_items = ['T-Shirt', 'Short-Sleeve Blouse', 'Short-Sleeve Dress']
            layering_items =['Cardigan', 'Hoodie', 'Lightweight Sweater']
            bottomwear_items = ['Pants', 'Jeans']
            footwear_items = ['Ankle Boots', 'Sneakers']
            accessories.extend(['Belt', 'Light Scarf', 'Socks'])

    elif 20 <= weather_temp < 25:
        if weather_text in ['Rain', 'Thunderstorm', 'Drizzle']: # If/else to see if Waterproof clothes are needed
            outerwear_items = ['Raincoat']
            topwear_items = ['T-Shirt', 'Short-Sleeve Blouse', 'Short-Sleeve Dress']
            layering_items =[]
            bottomwear_items = ['Jeans', 'Capri Pants']
            footwear_items = ['Sneakers', 'Rubber Rain Boots']
            accessories.extend(['Belt', 'Socks'])
        else:
            outerwear_items = ['Denim Jacket', 'Blazer']
            topwear_items = ['T-Shirt', 'Short-Sleeve Blouse', 'Short-Sleeve Dress']
            layering_items =[]
            bottomwear_items = ['Jeans', 'Capri Pants']
            footwear_items = ['Sneakers', 'Loafers', 'Sandals']
            accessories.extend(['Belt', 'Socks'])

    elif 25 <= weather_temp < 30:
        if weather_text in ['Rain', 'Thunderstorm', 'Drizzle']: # If/else to see if Waterproof clothes are needed
            outerwear_items = ['Raincoat']
            topwear_items = ['T-Shirt', 'Short-Sleeve Blouse', 'Short-Sleeve Dress', 'Tank Top']
            layering_items = []
            bottomwear_items = ['Shorts', 'Skirt']
            footwear_items = ['Sneakers']
            accessories.extend(['Belt', 'Cap', 'Socks'])
        else:
            outerwear_items = []
            topwear_items = ['T-Shirt', 'Short-Sleeve Blouse', 'Short-Sleeve Dress', 'Tank Top']
            layering_items = []
            bottomwear_items = ['Shorts', 'Skirt']
            footwear_items = ['Sneakers', 'Loafers', 'Sandals']
            accessories.extend(['Belt', 'Cap', 'Socks'])

    elif weather_temp >= 30:
        if weather_text in ['Rain', 'Thunderstorm', 'Drizzle']: # If/else to see if Waterproof clothes are needed
            outerwear_items = ['Raincoat']
            topwear_items = ['T-Shirt', 'Short-Sleeve Blouse', 'Short-Sleeve Dress', 'Tank Top']
            layering_items = []
            bottomwear_items = ['Shorts', 'Skirt']
            footwear_items = ['Sneakers']
            accessories.extend(['Belt', 'Cap', 'Socks'])
        else:
            outerwear_items = []
            topwear_items = ['T-Shirt', 'Short-Sleeve Blouse', 'Short-Sleeve Dress', 'Tank Top']
            layering_items = []
            bottomwear_items = ['Shorts', 'Skirt']
            footwear_items = ['Sandals']
            accessories.extend(['Belt', 'Cap'])

    # Additional accessories based on weather condition
    if weather_text == 'Clear':
        accessories.append('Sunglasses')
    elif weather_text in ['Rain', 'Thunderstorm', 'Drizzle']:
        accessories.append('Umbrella')

    # Returning the results
    return weather_text, weather_temp, outerwear_items, topwear_items, layering_items, bottomwear_items, footwear_items, accessories





# Session state initialization
# Reference:
if 'submitted' not in st.session_state:
    st.session_state['submitted'] = False



# Function to create a new table in the database for a new user's wardrobe
# Reference:
def create_user_table(user_name, DB):
    table_name = f"wardrobe_{user_name}" # To formulate the table name dynamically based on the user's name
    c =DB.cursor()  # To create a cursor object to interact with the database

    # To execute an SQL command to create a new table if it doesn't already exist with the table having columns for category, standard item name, and a custom name
    c.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            category TEXT,
            standard_item_name TEXT,
            custom_name TEXT
        )
    ''')

    # To commit to the changes to the database to ensure the creation of the table is saved
    DB.commit()



# Function to add a new item to the user's wardrobe table in the database
# Reference:
def add_item_to_wardrobe(user_name, category, item, custom_name, DB):
    table_name = f"wardrobe_{user_name}" # To formulate the table name dynamically based on the user's name

    # To create a DataFrame with the new item's details: category, standard item name, and custom name
    # With the DataFrame structured with column names and the corresponding values for the new item
    df = pd.DataFrame({
        'Category': [category],
        'Standard_Item_Name': [item],
        'Custom_Name': [custom_name]
    })

    # To append the new item's data to the specified table in the database
    # 'if_exists' is set to 'append' to add this new row to the table if it already exists
    # 'index=False' ensures that the DataFrame's index is not included as an extra column in the table
    df.to_sql(table_name, DB, if_exists='append', index=False)



# Function to retrieve the current wardrobe items for a specific user from the database
# Reference:
def get_wardrobe_items(user_name, DB):
    table_name = f"wardrobe_{user_name}"  # To formulate the table name dynamically based on the user's name

    # To execute an SQL query to select all records from the user's wardrobe table
    # With the query fetching all rows and columns from the specified table
    df = pd.read_sql(f'SELECT * FROM {table_name}', DB)

    # To print the column names of the DataFrame for debugging or informational purposes to help in understanding the structure of the retrieved data
    print("DataFrame Columns:", df.columns)  # Add this line to print the column names

    # To return the DataFrame containing the user's wardrobe items
    return df



# Function to initialize lists to keep track of present and missing items in the wardrobe
# Reference:
def check_wardrobe_for_items(user_name, recommended_items, DB):
    present_items = [] # To create list about present user items
    missing_items = [] # To create list about missing user items
    detailed_present_items_rows = []  # To create list to collect detailed information about present user items

    # To retrieve the current items in the user's wardrobe from the database
    wardrobe_items = get_wardrobe_items(user_name, DB) 

    # To iterate over each category and its items in the recommended items
    for category, items in recommended_items.items(): 
        for item in items: # To check if the current item is in the user's wardrobe
            if item in wardrobe_items['standard_item_name'].values:
                present_items.append(item) # If present, add to the list of present items
                detailed_present_items_rows.append(wardrobe_items[wardrobe_items['standard_item_name'] == item]) # To collect detailed information about this item
            else:
                missing_items.append(item) # If not present, to add to the list of missing items

    # To create a DataFrame from the collected rows of present items
    # If there are no present items, to create an empty DataFrame
    detailed_present_items = pd.concat(detailed_present_items_rows, ignore_index=True) if detailed_present_items_rows else pd.DataFrame()

    # To return the lists of present and missing items, and the DataFrame of detailed present items
    return present_items, missing_items, detailed_present_items



# Function to process the submission of city and user names
# Reference:
def submit(city_name, user_name):
    st.session_state['submitted'] = True # To update the inital session state to indicate that a submission has been made
    st.session_state['city'] = city_name # To store the submitted city name in the session state

    # To call the function to get weather data and clothing recommendations based on the submitted city
    weather_text, weather_temp, outerwear_items, topwear_items, layering_items, bottomwear_items, footwear_items, accessories = get_weather_and_clothing(city_name)
    
    # To open a connection to the wardrobe database
    with sqlite3.connect('wardrobe.db') as DB:
        present_items, missing_items, detailed_present_items = check_wardrobe_for_items(user_name, {
            'Outerwear': outerwear_items,
            'Topwear': topwear_items,
            'Layering': layering_items,
            'Bottomwear': bottomwear_items,
            'Footwear': footwear_items,
            'Accessories': accessories
        }, DB) # To check which recommended clothing items are present in the user's wardrobe and which are missing
    
    # To store the results of the wardrobe check in the session state for later access
    st.session_state['results'] = (weather_text, weather_temp, present_items, missing_items, detailed_present_items)



# To Establish a connection to the SQLite database named 'chinook.db'
# Reference:
DB = sqlite3.connect('chinook.db')





# Function to define the Streamlit web application
# Reference:
def main():
    st.sidebar.title("Navigation") # To set the title for the sidebar navigation

    # To assign the respective elements within the sidebar navigation
    pages = {
        "Home": main_page,
        "Results": results_page
    }
    
    if 'navigate_to_results' in st.session_state and st.session_state['navigate_to_results']:
        current_page = "Results"  # To check if the user has navigated to the results page, if so, set the current page to 'Results'
    else:
        current_page = st.sidebar.radio("Select a page:", list(pages.keys())) # Otherwise, to display a radio button selection for navigation in the sidebar

    # To display the selected page based on current_page
    pages[current_page]()


# Main Page - Function to display the main page of the app
# Reference:
def main_page():

    # To set a background image for the app
    st.markdown(
        """
        <style>
        .stApp {
            background-image: url("https://wallpapercave.com/wp/wp11789974.jpg");
            background-size: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    ) 


    # Title of the main page
    st.title('NimbusWardrobe')
    
    # Introductory text explaining the purpose of the app
    st.write('In order to provide you with an outfit recommendation for the current weather, we need to know a little about you and your personal wardrobe.')


    # Input field for user name
    user_name = st.text_input('Enter your user name:', key='user_name')

    # Operations to perform if the user has entered a name
    # Reference:
    if user_name:
        with sqlite3.connect('wardrobe.db') as DB: # To connect to the wardrobe database
            create_user_table(user_name, DB) # To create a table for the user if it does not exist
            df_wardrobe = get_wardrobe_items(user_name, DB) # To fetch the current wardrobe items from the database

            # To display the user's current wardrobe if it's not empty
            if not df_wardrobe.empty:
                print("DataFrame Columns:", df_wardrobe.columns)
                st.header('Your Current Wardrobe')
                st.write('It appears that you have the following wardrobe items registered on NimbusWardrobe:')

                # To loop through categories and display each category's items in the wardrobe
                categories = ['Outerwear', 'Topwear', 'Layering', 'Bottomwear', 'Footwear', 'Accessories']
                for category in categories:
                    st.subheader(f"{category} Items")
                    # Ensure the column name used here matches exactly with what's printed above
                    df_category = df_wardrobe[df_wardrobe['category'] == category]
                    if not df_category.empty:
                        st.dataframe(df_category)
                    else:
                        st.write(f"No items found in the {category} category.")


    # Section for managing the user's wardrobe
    # Reference:
    st.header('Manage Your Wardrobe')
    st.write("Please enter all your wardrobe items, if you haven't done so already:")

    # Definition of categories and corresponding items for wardrobe management, allowing users to choose from predefined categories and items
    categories = {
        'Outerwear': ['Winter Jacket/Coat', 'Wool Coat', 'Parka', 'Trench Coat', 'Lightweight Down Jacket', 'Softshell Jacket', 
        'Leather Jacket', 'Denim Jacket', 'Raincoat', 'Windbreaker', 'Blazer'],
        'Topwear': ['Long-Sleeve Shirt', 'T-Shirt', 'Short-Sleeve Blouse', 'Long-Sleeve Blouse', 'Long-Sleeve Dress', 'Short-Sleeve Dress', 'Tank Top'],
        'Layering': ['Heavy Sweater', 'Fleece/Thermal Layer', 'Cardigan', 'Hoodie', 'Lightweight Sweater'],
        'Bottomwear': ['Snow Pants', 'Pants', 'Jeans', 'Capri Pants', 'Shorts', 'Skirt'],
        'Footwear': ['Insulated Winter Boots', 'Classic Boots', 'Rubber Rain Boots', 'Ankle Boots', 'Sneakers', 'Loafers', 'Sandals', 'Rubber Rain Boots'],
        'Accessories': ['Sunglasses', 'Umbrella', 'Belt', 'Warm Scarf', 'Light Scarf', 'Beanie', 'Cap', 'Insulated Winter Gloves/Mittens', 
        'Standard Gloves/Mittens', 'Thermal Socks', 'Socks', 'Thermal Legginings/Tights']
    }

    category = st.selectbox('Select the category of your wardrobe item:', list(categories.keys())) # Drop-down menu for selecting a category
    item = st.selectbox('Select an item:', categories[category]) # Drop-down menu for selecting an item within the chosen category
    custom_name = st.text_input('Please name this item in your wardrobe:') # Text input for giving a custom name to the item

    # Button to submit the new item to the wardrobe
    if st.button('Submit New Item'):
        add_item_to_wardrobe(user_name, category, item, custom_name, DB) # Function call to add the new item to the user's wardrobe in the database
        st.success('Item added to your wardrobe!') # To display a confirmation message upon successful addition
        df_wardrobe = get_wardrobe_items(user_name, DB) # To refresh the wardrobe items to include the newly added item

    # To close the database connection
    DB.close()


    # Section for user to input weather and get clothing recommendation
    st.header("Check Local Weather for Clothing Advice")
    city_input = st.text_input("Enter the name of your city to get the current weather:", key='city_input') # Text input for entering the city name

    # Button to get clothing recommendations based on the entered city
    if st.button('Get Recommendations'):
        submit(city_input, user_name) # Function call to process the city input and get recommendations
        st.session_state['navigate_to_results'] = True  # To set a flag in session state to navigate to the results page



# Weather and Clothing Recommendations Page - Function to display the results page of the app
# Reference:
def results_page():
    st.title('NimbusWardrobe Recommendations') # To set the title of the results page in the Streamlit app


    # To check if there are results (weather and wardrobe data) stored in the session state
    if 'results' in st.session_state:
        weather_text, weather_temp, present_items, missing_items, detailed_present_items = st.session_state['results']  # To unpack weather data and wardrobe item lists from the session state

         # To display the current weather conditions for the specified city
        st.header(f"Weather in {st.session_state['city']}:")
        st.write(f"Weather Condition: {weather_text}")
        st.write(f"Temperature: {weather_temp}°C")


        # Recommendation section for items in the user's wardrobe
        st.header("Suitable Items in Your Wardrobe:") # To check if the DataFrame with present items is not empty
        if not detailed_present_items.empty: # Debugging line to check column names
            print("DataFrame Columns:", detailed_present_items.columns) # For debugging: to print the column names of the DataFrame to the console

            # List of categories to organize the displayed wardrobe items
            categories = ['Outerwear', 'Topwear', 'Layering', 'Bottomwear', 'Footwear', 'Accessories']
            for category in categories: # To loop through each category and display items under each
                st.subheader(f"{category}")
                df_category = detailed_present_items[detailed_present_items['category'] == category] # To filter and display items belonging to the current category
                if not df_category.empty:
                    st.dataframe(df_category) # To display the items in a table format
                else:
                    st.write(f"No items found in {category} category.") # To display message if no items are found in the category
        else:
            st.write('No specific items found in your wardrobe.') # Message displayed if there are no suitable items found in the wardrobe


         # Suggestion section for items missing from the user's wardrobe
        if missing_items:
            st.header("Consider Purchasing the Following Items:")
            st.write("It seems that you don't own certain items that are recommended for these temperatures. Consider acquiring the following pieces:")  # To display message with suggested items that are not in the wardrobe but recommended for current weather
            bullet_points = "\n".join([f"- {item}" for item in missing_items])  # To list the missing items in bullet points
            st.markdown(bullet_points, unsafe_allow_html=True)



# App execution when this script is run directly
# Reference:
if __name__ == '__main__':
    main()
