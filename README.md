# Weather-forcast-system

## Overview

This project is a weather forecasting system that utilizes computer vision techniques to analyze environmental factors and provide weather predictions. Unlike traditional approaches that rely on machine learning, this system leverages image processing and analysis to interpret weather-related visual data.

## Features

- **Real-time Weather Analysis**: Capture and analyze live images from the environment to assess weather conditions.
- **Image Processing**: Use OpenCV for image enhancement and feature extraction to identify weather indicators such as cloud cover, brightness, and precipitation.
- **Audio Notifications**: Alerts users with audio cues based on the weather predictions.
- **Threading for Efficiency**: Implements threading to handle real-time image capture and processing without lag.

## Technologies Used

- **Python**: The primary programming language for developing the system.
- **OpenCV**: For image processing and computer vision tasks.
- **Playsound**: To play audio notifications for weather updates.
- **NumPy**: For numerical operations and data manipulation.
- **Requests**: For making HTTP requests if external data is needed (e.g., fetching additional weather information).
- **Imutils**: For convenient image processing functions.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/weather-forecasting-system.git
   ```

2. Navigate to the project directory:

   ```bash
   cd weather-forecasting-system
   ```

3. Install the required packages:

   ```bash
   pip install opencv-python numpy playsound requests imutils
   ```

## Usage

To run the system, execute the following command in your terminal:

```bash
python main.py
```
**Note:** You must have to use an IP camera for video capturing. There are many found at [***Google Play Store***](play.google.com).

The system will start capturing images from your camera, analyze the data, and provide real-time weather predictions along with audio notifications.

## Contributing

Contributions are welcome! If you'd like to improve this project, please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- Inspired by traditional weather forecasting methods and the potential of computer vision.
- Thanks to the developers of the libraries used in this project.
