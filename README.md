Solar Energy Data Analysis

This project is designed to analyze solar energy data from various locations in Benin, Sierra Leone, and Togo. The objective is to provide insights into solar radiation trends, temperature correlations, wind patterns, and overall data quality, to assist MoonLight Energy Solutions in optimizing their solar energy strategies.

Table of Contents
Overview
Project Structure
Datasets
Setup Instructions
Analysis and Visualizations
Running the Streamlit App
Contributing
License
Overview
This project involves a thorough analysis of solar energy data from three locations in West Africa. The analysis focuses on understanding the relationships between environmental factors such as solar radiation, temperature, wind speed, and direction. By leveraging this data, MoonLight Energy Solutions aims to identify high-potential areas for solar energy installations and improve operational efficiency.

Project Structure
The project is organized into the following directories and files:

plaintext
Copy code
solar-energy-data/
├── .vscode/
│   └── settings.json
├── .github/
│   └── workflows/
│       └── unittests.yml
├── App/
│   └── main.py  # Streamlit application to explore the datasets and visualizations
├── data/
│   ├── benin-malanville.csv  # Solar energy data for Benin
│   ├── sierraleone-bumbuna.csv  # Solar energy data for Sierra Leone
│   └── togo-dapaong_qc.csv  # Solar energy data for Togo
├── notebooks/
│   └── solar_energy_analysis.ipynb  # Jupyter notebook for in-depth analysis
├── scripts/
│   └── data_cleaning.py  # Script for cleaning and preprocessing data
├── tests/
│   └── test_data_quality.py  # Tests to ensure data quality and integrity
├── README.md  # Project documentation
├── requirements.txt  # Python dependencies for the project
└── .gitignore  # Files and directories to be ignored by Git
Datasets
The datasets used in this project are stored in the data/ directory and include:

benin-malanville.csv: Solar radiation and environmental data for Malanville, Benin.
sierraleone-bumbuna.csv: Solar radiation and environmental data for Bumbuna, Sierra Leone.
togo-dapaong_qc.csv: Solar radiation and environmental data for Dapaong, Togo.
These datasets contain measurements such as Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), Diffuse Horizontal Irradiance (DHI), temperature readings, wind speed, and direction, among others.

Setup Instructions
To set up the project environment and install necessary dependencies, follow these steps:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/solar-energy-data.git
cd solar-energy-data
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
Run the Jupyter notebook for analysis:

bash
Copy code
jupyter notebook notebooks/solar_energy_analysis.ipynb
Analysis and Visualizations
The project includes several key analyses and visualizations:

Summary Statistics: Calculate mean, median, standard deviation, and other statistical metrics for the dataset.
Data Quality Check: Identify missing values, outliers, and anomalies in the data.
Time Series Analysis: Explore temporal patterns in solar radiation and other environmental variables.
Correlation Analysis: Use heatmaps and scatter plots to investigate relationships between variables such as solar radiation, temperature, and wind speed.
Wind Analysis: Polar plots to visualize wind speed and direction variability.
Temperature Analysis: Examine the influence of relative humidity (RH) on temperature readings and solar radiation.
Histograms: Visualize the frequency distribution of key variables like GHI, DNI, DHI, and temperatures.
Z-Score Analysis: Identify data points significantly different from the mean.
Bubble Charts: Explore complex relationships between variables with bubble charts, e.g., GHI vs. Tamb vs. WS, with bubble size representing RH or BP.
Running the Streamlit App
To interactively explore the data and visualizations, run the Streamlit app:

Navigate to the project’s root directory.

Execute the following command:

bash
Copy code
streamlit run App/main.py
Open your web browser and go to the local server URL that Streamlit provides.

Contributing
Contributions are welcome! If you would like to contribute to this project:

Fork the repository.
Create a feature branch (git checkout -b feature/YourFeature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/YourFeature).
Open a pull request to the main repository.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

