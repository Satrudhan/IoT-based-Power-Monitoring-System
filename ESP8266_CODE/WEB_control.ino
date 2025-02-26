#include <Wire.h>
#include <Adafruit_INA219.h>
#include <LiquidCrystal.h>
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

// LCD Pin Configuration
const int rs = D7;
const int en = D8;
const int d4 = D3;
const int d5 = D4;
const int d6 = D5;
const int d7 = D6;

const int switchPin = D0;   // Switch connected to D0
bool stopSerial = false;    // Flag to control serial output
unsigned long lastDebounceTime = 0; // To manage debouncing
unsigned long debounceDelay = 200; // Debounce delay in ms

// INA219 Sensors
Adafruit_INA219 ina219_1(0x40); // Transmitter coil
Adafruit_INA219 ina219_2(0x41); // Receiver coil

// LCD Display
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);

// Wi-Fi Configuration
const char* ssid = "Sumanas";
const char* password = "Nepenthe108";
ESP8266WebServer server(80);


// Variables to store sensor readings
float voltage1, current1, power1;
float voltage2, current2, power2;

// Function to handle the root page
void handleRoot() {
  String page = R"rawliteral(
    <!DOCTYPE html>
    <html>
    <head>
      <title>NodeMCU Real-Time Monitor</title>
      <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
      <style>
        body {
          font-family: Arial, sans-serif;
          margin: 0;
          padding: 0;
          display: flex;
          flex-direction: column;
          align-items: center;
          justify-content: center;
          height: 95vh;
        }
        canvas {
          max-width: 90%; /* Responsive width adjustment */
          height: 300px; /* Reduced height */
        }
      </style>
      <script>
        let chart;
        let voltageData = { transmitter: [], receiver: [] };
        let currentData = { transmitter: [], receiver: [] };
        let powerData = { transmitter: [], receiver: [] };

        function fetchData() {
          fetch('/data')
            .then(response => response.json())
            .then(data => {
              updateGraph(chart, voltageData, data.voltage1, data.voltage2, 'Voltage');
              updateGraph(chart, currentData, data.current1, data.current2, 'Current');
              updateGraph(chart, powerData, data.power1, data.power2, 'Power');
            });
        }

        function updateGraph(chart, dataset, newValue1, newValue2, label) {
          if (dataset.transmitter.length > 20) dataset.transmitter.shift();
          if (dataset.receiver.length > 20) dataset.receiver.shift();
          dataset.transmitter.push(newValue1);
          dataset.receiver.push(newValue2);

          const datasetTransmitter = chart.data.datasets.find(ds => ds.label === label + ' (Transmitter)');
          const datasetReceiver = chart.data.datasets.find(ds => ds.label === label + ' (Receiver)');
          datasetTransmitter.data = dataset.transmitter;
          datasetReceiver.data = dataset.receiver;
          chart.update();
        }

        function setupGraph() {
          const ctx = document.getElementById('dataChart').getContext('2d');
          chart = new Chart(ctx, {
            type: 'line',
            data: {
              labels: Array(20).fill(''), // Placeholder for 20 points
              datasets: [
                {
                  label: 'Voltage (Transmitter)',
                  borderColor: 'blue',
                  yAxisID: 'voltage',
                  data: [],
                  fill: false
                },
                {
                  label: 'Voltage (Receiver)',
                  borderColor: 'lightblue',
                  yAxisID: 'voltage',
                  data: [],
                  fill: false
                },
                {
                  label: 'Current (Transmitter)',
                  borderColor: 'green',
                  yAxisID: 'current',
                  data: [],
                  fill: false
                },
                {
                  label: 'Current (Receiver)',
                  borderColor: 'lightgreen',
                  yAxisID: 'current',
                  data: [],
                  fill: false
                },
                {
                  label: 'Power (Transmitter)',
                  borderColor: 'red',
                  yAxisID: 'power',
                  data: [],
                  fill: false
                },
                {
                  label: 'Power (Receiver)',
                  borderColor: 'pink',
                  yAxisID: 'power',
                  data: [],
                  fill: false
                }
              ]
            },
            options: {
              responsive: true,
              maintainAspectRatio: false,
              scales: {
                x: { display: false },
                y: [
                  {
                    id: 'voltage',
                    type: 'linear',
                    position: 'left',
                    ticks: { color: 'blue' },
                    title: { display: true, text: 'Voltage (V)' }
                  },
                  {
                    id: 'current',
                    type: 'linear',
                    position: 'right',
                    ticks: { color: 'green' },
                    title: { display: true, text: 'Current (mA)' }
                  },
                  {
                    id: 'power',
                    type: 'linear',
                    position: 'right',
                    ticks: { color: 'red' },
                    title: { display: true, text: 'Power (mW)' },
                    grid: { drawOnChartArea: false } // Prevent grid lines overlap
                  }
                ]
              },
              plugins: {
                legend: { display: true, position: 'bottom' }
              }
            }
          });
        }

        document.addEventListener('DOMContentLoaded', () => {
          setupGraph();
          setInterval(fetchData, 1000);
        });
      </script>
    </head>
    <body>
      <h1>NodeMCU Real-Time Monitoring</h1>
      <canvas id="dataChart"></canvas>
    </body>
    </html>
  )rawliteral";

  server.send(200, "text/html", page);
}



// Function to handle the /data endpoint
void handleData() {
  String json = "{";
  json += "\"voltage1\":" + String(voltage1, 2) + ",";
  json += "\"current1\":" + String(current1, 2) + ",";
  json += "\"power1\":" + String(power1, 2) + ",";
  json += "\"voltage2\":" + String(voltage2, 2) + ",";
  json += "\"current2\":" + String(current2, 2) + ",";
  json += "\"power2\":" + String(power2, 2);
  json += "}";

  server.send(200, "application/json", json);
}


void setup() {
  Serial.begin(9600);
  Wire.begin(D1, D2);
  pinMode(switchPin, INPUT_PULLUP);

  lcd.begin(16, 2);
  lcd.print("Initializing...");
  delay(2000);
  lcd.clear();

  if (!ina219_1.begin() || !ina219_2.begin()) {
    lcd.print("INA219 Error");
    while (1) { delay(10); }
  }


  lcd.print("INA219 Ready");
  delay(2000);
  lcd.clear();

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  lcd.print("Connecting WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    lcd.setCursor(0, 1);
    lcd.print(".");
  }
  
  lcd.clear();
  lcd.print("WiFi Connected");
  delay(2000);
  lcd.clear();

  lcd.clear();
  lcd.print("IP:");
  lcd.setCursor(0, 1);
  lcd.print(WiFi.localIP());
  delay(10000); // Display the IP for 5 seconds before clearing
  lcd.clear();


  server.on("/", handleRoot); // Serve the HTML page
  server.on("/data", handleData); // Serve the sensor data as JSON
  server.begin();
  Serial.println("Web server started.");
}

void loop() {
  server.handleClient();

  int reading = digitalRead(switchPin);
  if (reading == LOW && (millis() - lastDebounceTime) > debounceDelay) {
    lastDebounceTime = millis();
    stopSerial = !stopSerial; // Toggle serial output
  }


  voltage1 = ina219_1.getBusVoltage_V();
  current1 = ina219_1.getCurrent_mA();
  power1 = ina219_1.getPower_mW();
  voltage2 = ina219_2.getBusVoltage_V();
  current2 = ina219_2.getCurrent_mA();
  power2 = ina219_2.getPower_mW();


  if (!stopSerial) {
    Serial.print("Transmitter: ");
    Serial.print(voltage1, 2); Serial.print(" V, ");
    Serial.print(current1, 2); Serial.print(" mA, ");
    Serial.println(power1, 2);

    Serial.print("Receiver: ");
    Serial.print(voltage2, 2); Serial.print(" V, ");
    Serial.print(current2, 2); Serial.print(" mA, ");
    Serial.println(power2, 2);
  }

  lcd.setCursor(0, 0);
  lcd.print("T");
  lcd.print(voltage1, 2); lcd.print("V ");
  lcd.print((int)current1); lcd.print("mA ");
  lcd.print((int)power1); lcd.print("mW");

  lcd.setCursor(0, 1);
  lcd.print("R");
  lcd.print(voltage2, 2); lcd.print("V ");
  lcd.print((int)current2); lcd.print("mA ");
  lcd.print((int)power2); lcd.print("mW");

  delay(1000);
}
