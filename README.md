# AI Content Studio 🤖

<div align="center">

*A professional AI-powered content creation tool that generates emails, business proposals, blog posts, social media content, cover letters, and text summaries using Google's Gemini AI.*

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![AI](https://img.shields.io/badge/AI-Gemini-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Examples](#-examples) • [Support](#-support)

</div>

## ✨ Features

| Feature | Description | Status |
|---------|-------------|--------|
| 📧 **Email Writing** | Professional business emails and communications | ✅ |
| 📊 **Business Proposals** | Concise and persuasive business proposals | ✅ |
| ✍️ **Blog Posts** | Engaging blog content and articles | ✅ |
| 📱 **Social Media** | Platform-optimized social media posts | ✅ |
| 💼 **Cover Letters** | Professional job application letters | ✅ |
| 📝 **Text Summarization** | Quick 3-point text summaries | ✅ |
| 💾 **Export History** | Save all generated content to files | ✅ |
| 📜 **Usage Tracking** | Monitor your content generation history | ✅ |

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Google AI Studio API key ([Get it free here](https://aistudio.google.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ai-content-studio.git
   cd ai-content-studio
Install dependencies

bash
pip install -r requirements.txt
Configure your API key

bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Google AI API key
# Replace: YOUR_API_KEY_HERE=your_actual_google_ai_api_key
Run the application

bash
python src/AI_Content_Studio.py
📸 Demo
🎯 Quick Demo
bash
# After installation, you'll see:
🚀 Welcome to AI Content Studio!
Your all-in-one AI content creation tool.

==================================================
🤖 AI CONTENT STUDIO
==================================================
1. ✉️  Write Professional Email
2. 📊 Create Business Proposal
3. ✍️  Write Blog Post
4. 📱 Generate Social Media Content
5. 💼 Create Cover Letter
6. 📝 Summarize Text
7. 📜 View Generation History
8. 💾 Save History to File
9. 🚪 Exit
==================================================
🛠️ Usage
Basic Usage
Run the script: python src/AI_Content_Studio.py

Choose from 6 content types (1-6)

Enter your topic or text when prompted

Receive AI-generated content instantly

View history or export to files (options 7-8)

Example Usage
python
# The tool handles everything automatically:
# - API configuration
# - Error handling  
# - Content formatting
# - File management
🏗️ Project Structure
text
ai-content-studio/
├── src/
│   └── AI_Content_Studio.py  # Main application
├── examples/
│   ├── sample_outputs.txt    # Example generated content
│   ├── marketing_copy.txt    # Marketing examples
│   └── technical_Documentation.txt  # Technical examples
├── requirements.txt          # Python dependencies
├── .env.example             # Environment configuration template
├── .gitignore               # Git ignore rules
├── LICENSE                  # MIT License
└── README.md               # This documentation
🔧 Technical Details
Technology Stack
AI Model: Google Gemini 2.0 Flash

Programming Language: Python 3.8+

Architecture: Object-oriented design

Storage: Local file-based history

Configuration: Environment variables

Dependencies
txt
google-generativeai>=0.3.0    # Google AI API client
python-dotenv>=1.0.0         # Environment management
📊 Examples
Check out the examples/ folder for detailed examples of generated content including:

Professional emails

Business proposals

Blog posts

Social media content

Cover letters

Text summaries

🤝 Contributing
Contributions are welcome! Here's how you can help:

Fork the project

Create a feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

❓ Frequently Asked Questions
Q: How do I get a Google AI API key?
A: Visit Google AI Studio, sign in with your Google account, and generate a free API key.

Q: Is there a usage limit?
A: Google AI Studio offers free tier usage with generous limits for personal projects.

Q: Can I add custom content types?
A: Yes! Modify the templates dictionary in the AIContentStudio class to add new content types.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

👨‍💻 Author
WALEED TRADERS

GitHub: @WALEEDTRADERS

Project Link: https://github.com/YOUR_USERNAME/ai-content-studio

🙏 Acknowledgments
Google Gemini AI for the powerful language model

Python community for excellent libraries and tools

<div align="center">
⭐ If you find this project helpful, please give it a star on GitHub!
</div> ```