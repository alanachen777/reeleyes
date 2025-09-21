# ReelEyes 👁️👄👁️

**AI Video Detection Platform for Social Media**

ReelEyes is a web application that analyzes uploaded videos to detect if they were generated using AI tools. Built for SteelHacks 2025, it functions as a social media platform that only allows authentic, human-created content.

## 🚀 Features

- **Real-time AI Detection**: Upload videos and get instant analysis
- **Smart Content Filtering**: AI-generated videos are rejected automatically
- **Social Media Feed**: View and interact with verified authentic videos
- **Video Management**: Delete your uploaded videos from the feed
- **Modern UI**: Clean design with Orbitron and Inter fonts
- **Responsive Design**: Works on desktop and mobile devices

## 🛠️ Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript
- **Backend**: Python Flask with CORS support
- **Storage**: Browser localStorage for video data
- **Fonts**: Orbitron (titles) + Inter (UI elements)
- **Analysis**: File entropy, codec detection, filename patterns

## 📋 Prerequisites

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
   pip install Flask Flask-CORS
   python app.py
   ```

3. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

## 🎯 How It Works

### Upload & Analysis Flow
1. **Upload Video**: Drag & drop or click to select a video file
2. **AI Detection**: System analyzes the video for AI generation indicators
3. **Smart Filtering**: 
   - ✅ **Real videos** → Uploaded to feed automatically
   - ❌ **AI videos** → Rejected with explanation
4. **Feed Redirect**: Successfully uploaded videos redirect you to the social feed

### Detection Methods
- **Filename Analysis**: Checks for AI-related keywords
- **Codec Signatures**: Identifies patterns from AI generation tools  
- **File Entropy**: Measures data randomness and compression patterns
- **Size Analysis**: Evaluates file characteristics typical of AI content

## 📱 User Interface

### Upload Page (`/`)
- Futuristic **REELEYES** title with gradient text
- Drag & drop upload area
- Real-time analysis with loading spinner
- **Feed** button to view uploaded content

### Social Feed (`/feed`)
- Grid layout of verified authentic videos
- Playable video previews
- Upload timestamps and verification badges
- Delete functionality for content management

## 📁 Project Structure

```
reeleyes/
├── backend/
│   └── app.py              # Flask server with AI detection
├── frontend/
│   ├── index.html          # Upload/analysis page
│   ├── style.css           # Main page styling
│   ├── feed.html           # Social media feed
│   └── feed.css            # Feed page styling
├── logo/
│   └── ReelEyes.png        # Platform logo
├── run.bat                 # Windows startup script
├── requirements.txt        # Python dependencies
└── README.md              # This documentation
```

## 🎨 Design Features

- **Color Scheme**: Maroon (#5B0B24) + Light Pink (coral) (#CC847E) + Cream (#E0D6CC)
- **Typography**: Orbitron for branding, Inter for interface elements
- **Animations**: Smooth hover effects and loading states
- **Responsive**: Mobile-friendly grid layouts

## 🚀 API Endpoints

- `GET /` - Main upload/analysis interface
- `GET /feed` - Social media feed page
- `POST /api/analyze` - Video analysis endpoint
- `GET /logo/<filename>` - Logo assets
- `GET /<filename>` - Static file serving

## 🔮 Future Enhancements

- User authentication and profiles
- Advanced ML model integration
- Video comments and social features
- Content moderation tools
- Mobile app development
- Cloud storage integration

## 🏆 SteelHacks 2025

Built for **SteelHacks 2025** to address the growing challenge of AI-generated content on social media platforms. As deepfakes and AI videos become more sophisticated, platforms need reliable detection systems to maintain content authenticity and user trust. 

## 👥 Team - Chalant **(Go WVU! 🏔️)**

- **Alana Chen** - Full-stack developer, ayc00003@mix.wvu.edu
- **Kara Adzima** - Front-end developer, kaa00024@mix.wvu.edu  
- **Ava Hill** - Front-end developer, amh00065@mix.wvu.edu
- **Josiah Brown** - Backend developer, jbd00076@mix.wvu.edu

## 📄 License

MIT License - Built for educational and hackathon purposes.

---

**⚠️ Note**: This is a hackathon prototype demonstrating AI content detection concepts. For production deployment, implement robust ML models, user authentication, and enhanced security measures.