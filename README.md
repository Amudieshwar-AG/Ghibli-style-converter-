# 🎨 Ghibli Style Image Converter

Transform your ordinary photos into stunning Ghibli-inspired art! This project uses deep learning and style transfer with AnimeGAN2 to give your images a magical Studio Ghibli look.

## 🚀 Features

- Upload your own images from a web dashboard.
- Instantly generate Ghibli-style versions.
- Download your stylized images.
- Beautiful, easy-to-use interface with a custom background.

## 📷 Demo

![Demo Screenshot](https://your-screenshot-link-if-you-have-one)

## 📁 Folder Structure
├── app.py # Flask application
├── templates/
│ └── index.html # Main HTML page
├── static/
│ ├── background/ # Background image
│ ├── uploads/ # Uploaded images
│ └── results/ # Stylized output images
├── style.css # Custom styles
└── README.md
1. Clone the repository:
   ```bash
   git clone https://github.com/Amudieshwar-AG/Ghibli-style-converter-.git
   cd Ghibli-style-converter-
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Run the application:

bash
Copy code
python app.py
Open your browser and visit http://127.0.0.1:5000/ to use the app.

🖼️ Usage
On the dashboard, click Choose File and select an image.

Click Upload — your uploaded image and stylized result will appear.

Click Download to save your Ghibli-styled image.

🛠️ Built With
Flask

AnimeGAN2

HTML, CSS

🙏 Acknowledgements
AnimeGAN2 pretrained weights for style transfer.

Studio Ghibli for inspiration.

📜 License
This project is for educational purposes only. All Ghibli-related content belongs to Studio Ghibli.



