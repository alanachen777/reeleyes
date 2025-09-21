# ReelEyes 👁️🤖

**AI Video Detection Platform for Social Media**

ReelEyes is a web application that analyzes uploaded videos to detect if they were generated using AI tools. Built for SteelHacks 2025, it's designed to be a short-form social media platform (like TikTok) with an emphasis on preventing AI-generated content.

## 🚀 Features

- **Real-time AI Detection**: Upload videos and get instant analysis
- **Smart Analysis**: Detects AI generation patterns, codec signatures, and file characteristics
- **Clean Interface**: Modern, responsive web design
- **Fast Processing**: Lightweight backend with efficient analysis
- **Detailed Results**: Shows specific indicators found during analysis

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask
- **Analysis**: File entropy, codec detection, pattern recognition
- **Styling**: Modern design with responsive layout

## 📋 Prerequisites

Before running ReelEyes, make sure you have:

- **Python 3.7+** installed on your system
- **pip** (Python package manager)
- A modern web browser

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/reeleyes.git
   cd reeleyes
   ```

2. **Run the application**:
   ```bash
   # On Windows
   run.bat
   
   # On Mac/Linux
   cd backend
   pip install flask flask-cors requests
   python app.py
   ```

3. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

## 🎯 How to Use

1. **Upload Video**: Click the upload area or drag & drop a video file
2. **Analyze**: Click "Analyze Video" button
3. **View Results**: Get instant feedback on whether the video is AI-generated
4. **Review Details**: See specific indicators that influenced the detection

## 🔍 Detection Methods

ReelEyes uses multiple analysis techniques:

- **Filename Analysis**: Checks for AI-related keywords
- **Codec Detection**: Identifies signatures from AI generation tools
- **Entropy Analysis**: Measures data randomness patterns
- **File Characteristics**: Analyzes compression and size patterns

## 📁 Project Structure

```
reeleyes/
├── backend/
│   ├── app.py          # Main Flask server
│   ├── analyzer.py     # AI detection logic
│   ├── ml_detector.py  # Machine learning detector
│   └── run_server.py   # Server runner
├── frontend/
│   ├── index.html      # Main web interface
│   └── style.css       # Styling and responsive design
├── scripts/
│   ├── train_ml.py     # ML model training
│   ├── test_*.py       # Test files
│   └── extract_*.py    # Data extraction tools
├── run.bat            # Windows startup script
├── requirements.txt   # Python dependencies
└── README.md          # This file
```

## 🎨 Interface Preview

- **Upload Area**: Drag & drop or click to select videos
- **Analysis Button**: Processes the uploaded video
- **Results Display**: Shows AI/Real verdict with confidence details
- **Loading Animation**: Smooth spinner during processing

## 🚀 API Endpoints

- `GET /` - Serves the main web interface
- `POST /api/analyze` - Analyzes uploaded video files
- `GET /<filename>` - Serves static files (CSS, etc.)

## 🔮 Future Enhancements

- Integration with advanced ML models
- Support for more video formats
- Batch processing capabilities
- API rate limiting and authentication
- Enhanced detection algorithms

## 🏆 Hackathon Context

Built for **SteelHacks 2025** to address the growing need for AI content detection on social media platforms. As AI-generated videos become more sophisticated, platforms need reliable tools to maintain content authenticity.

## 🤝 Contributing

This is a hackathon project, but contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

MIT License - feel free to use this project for educational purposes.

## 👥 Team

Built with ❤️ for SteelHacks 2025 by Chalant (Go WVU!!!)

Alana Chen - Full-stack developer, ayc00003@mix.wvu.edu
Kara Adzima - Front-end developer, kaa00024@mix.wvu.edu
Ava Hill - Front-end developer, amh00065@mix.wvu.edu
Josiah Brown - Backend developer, jed00076@mix.wvu.edu

---

**Note**: This is a proof-of-concept *DEMO* built for a hackathon. For production use, consider implementing more robust AI detection models and security measures.