# Smart Agriculture Helper

def get_crop_recommendation(soil_moisture, temperature, humidity):
    if soil_moisture < 30:
        return "Irrigation needed, ideal for drought-resistant crops like millet or sorghum."
    elif soil_moisture >= 30 and soil_moisture <= 60:
        if temperature >= 20 and temperature <= 30 and humidity >= 50:
            return "Suitable for crops like maize, wheat, and sugarcane."
        else:
            return "Consider crops suited for lower humidity or temperature."
    else:
        return "Soil moisture is high, suitable for rice or other water-loving crops."

def main():
    # Sample sensor inputs (in real implementation, read from sensors)
    soil_moisture = float(input("Enter soil moisture (%): "))
    temperature = float(input("Enter ambient temperature (°C): "))
    humidity = float(input("Enter relative humidity (%): "))

    recommendation = get_crop_recommendation(soil_moisture, temperature, humidity)
    
    print(f"Crop Recommendation: {recommendation}")

if __name__ == "__main__":
    main()       
