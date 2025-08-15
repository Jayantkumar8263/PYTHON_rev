#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h> // Required for I2C sensors like some humidity/temp sensors

// WiFi Credentials
const char* ssid = "YOUR_WIFI_SSID";
const char* password = "YOUR_WIFI_PASSWORD";

// Server Endpoint
const char* serverUrl = "https://your-data-server.com/api/windseeker/data";

// Sensor Pins 
const int windSpeedPin = 2;   
const int windDirectionPin = 4; 
const int temperaturePin = 12;  
const int humidityPin = 13;     
const int airQualityPin = 14;  

// Variables for sensor readings
float windSpeed = 0.0;
int windDirection = 0;
float temperature = 0.0;
float humidity = 0.0;
int airQuality = 0;
unsigned long lastTransmissionTime = 0;
const unsigned long transmissionInterval = 5000; // 5 seconds (5ml * 1000 = 5sec)

// Function to read wind speed 
float readWindSpeed() {
  int rawValue = analogRead(windSpeedPin);
  // Convert raw analog reading to wind speed 
  float speed = map(rawValue, 0, 1023, 0, 30); // Example: 0-30 m/s
  return speed;
}

// Function to read wind direction 
int readWindDirection() {
  int rawValue = analogRead(windDirectionPin);
  int direction = map(rawValue, 0, 1023, 0, 360); // 0-360 degrees
  return direction;
}

// Function to read temperature 
float readTemperature() {
  int rawValue = analogRead(temperaturePin);
  float temp = map(rawValue, 0, 1023, -10, 40); // -10 to 40 degrees C
  return temp;
}

// Function to read humidity 
float readHumidity() {
  int rawValue = analogRead(humidityPin); 
  float hum = map(rawValue, 0, 1023, 0, 100); // 0-100%
  return hum;
}

// Function to read air quality 
int readAirQuality() {
  int rawValue = analogRead(airQualityPin);
  int airQ = map(rawValue, 0, 1023, 0, 500); // 0-500 AQI
  return airQ;
}

// Function to transmit data to the server
void transmitData() {
  if (WiFi.status() == WL_CONNECTED) {
    HTTPClient http;
    http.begin(serverUrl);
    http.addHeader("Content-Type", "application/json");

    String jsonData = "{\"wind_speed\": " + String(windSpeed) +
                      ", \"wind_direction\": " + String(windDirection) +
                      ", \"temperature\": " + String(temperature) +
                      ", \"humidity\": " + String(humidity) +
                      ", \"air_quality\": " + String(airQuality) +
                      ", \"timestamp\": " + String(millis()/1000) + "}"; //millis() for timestamp

    int httpResponseCode = http.POST(jsonData);

    if (httpResponseCode > 0) {
      String response = http.getString();
      Serial.print("HTTP Response code: ");
      Serial.println(httpResponseCode);
      Serial.println(response);
    } else {
      Serial.print("Error code: ");
      Serial.println(httpResponseCode);
    }

    http.end();
    lastTransmissionTime = millis();
  } else {
    Serial.println("WiFi Disconnected");
  }
}

void setup() {
  Serial.begin(115200);
  pinMode(windSpeedPin, INPUT);
  pinMode(windDirectionPin, INPUT);
  pinMode(temperaturePin, INPUT);
  pinMode(humidityPin, INPUT);
  pinMode(airQualityPin, INPUT);

  // Connect to WiFi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");
}

void loop() {
  // Read sensor data
  windSpeed = readWindSpeed();
  windDirection = readWindDirection();
  temperature = readTemperature();
  humidity = readHumidity();
  
  airQuality = readAirQuality();

  // Print sensor data to serial monitor
  Serial.print("Wind Speed: "); Serial.print(windSpeed); Serial.print(" m/s, ");
  Serial.print("Direction: "); Serial.print(windDirection); Serial.print(" deg, ");
  Serial.print("Temp: "); Serial.print(temperature); Serial.print(" C, ");
  Serial.print("Humidity: "); Serial.print(humidity); Serial.print(" %, ");
  Serial.print("Air Quality: "); Serial.println(airQuality);

  // Transmit data periodically
  if (millis() - lastTransmissionTime >= transmissionInterval) {
    transmitData();
  }
  delay(100); // Small delay to prevent flooding
}