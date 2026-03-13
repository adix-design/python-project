import requests

def get_weather(city_name, api_key):
    # 1. Base URL for the OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # 2. Parameters we are sending to the API
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric" # This gets the temperature in Celsius (use "imperial" for Fahrenheit)
    }
    
    try:
        # 3. Making the HTTP GET request to the API
        response = requests.get(base_url, params=params)
        
        # 4. Checking if the request was successful (Status code 200 means OK)
        if response.status_code == 200:
            data = response.json() # Parse JSON response into a Python dictionary
            
            # Extracting specific data from the dictionary
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            city = data["name"]
            
            # 5. Display the weather to the user
            print(f"\n--- Weather in {city} ---")
            print(f"Temperature: {temp}°C")
            print(f"Condition  : {description.capitalize()}")
            print("-" * 25 + "\n")
            
        elif response.status_code == 404:
            print(f"\nError: City '{city_name}' not found. Please check the spelling.\n")
        elif response.status_code == 401:
            print("\nError: Invalid API Key. Your new key might take 10-15 minutes to activate!\n")
        else:
            print(f"\nError: Failed to get weather data. Status Code: {response.status_code}\n")
            
    except requests.exceptions.RequestException as e:
        print(f"\nNetwork Error: Please check your internet connection.\nDetails: {e}\n")

if __name__ == "__main__":
    print("Welcome to the Python Weather App!")
    
    # Here is the API key you just got!
    API_KEY = "374364fd8cbfd5d9ff522ab13d7ccda3"
    
    while True:
        # Ask the user for input
        city = input("Enter a city name (or type 'quit' to exit): ")
        
        if city.lower() == 'quit':
            print("Goodbye!")
            break
        elif city.strip() == "":
            print("Please enter a valid city name.")
            continue
            
        # Call the function with the city and api key
        get_weather(city, API_KEY)