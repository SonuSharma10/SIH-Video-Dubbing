# Smart India Hackathon (SIH) 2023 Project

## Problem Statement
The project's goal was to develop a system that could automatically dub any English video into Hindi or any other Indian regional language while ensuring the output works both online and offline. The challenge was to build a model that could seamlessly synchronize audio and lip movements while maintaining a user-friendly interface. Additionally, the solution had to be optimized for performance, producing fast results and supporting offline usage to make it accessible in low-connectivity environments.

## Solution
Our solution addresses the problem by utilizing machine learning models and audio processing techniques to convert English audio from videos into selected Indian languages. The system performs real-time synchronization of dubbed audio with the original video, maintaining lip-sync accuracy. It can process YouTube video URLs and convert them into dubbed versions efficiently. The project includes an easy-to-use interface developed in Python with Gradio, allowing users to generate dubbed videos quickly, even in offline mode.

## Key Features
- **Offline Support**: Works without an internet connection, ensuring accessibility in low-connectivity areas.
- **YouTube Video Dubbing**: Converts English YouTube video URLs into dubbed videos in Hindi or other Indian languages.
- **Audio Synchronization**: Ensures that the dubbed audio is synchronized perfectly with the original video.
- **Lip Sync**: Maintains lip synchronization for a realistic dubbing experience.
- **Fast Output**: Provides quick results through an optimized Gradio Python UI.

## Technologies Used
- **Python**: For the core application logic and machine learning model integration.
- **Machine Learning (ML)**: To handle speech recognition, translation, and text-to-speech synthesis.
- **REST API**: For handling requests and integrating external services.
- **Audio Processing Libraries**: For audio synchronization and lip sync.
- **Gradio**: For building a simple and interactive user interface.

