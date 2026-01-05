# 📄 Resume Builder

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3%2B-green?logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-3.3.7-purple?logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A modern, responsive, and customizable resume/CV web application built with Flask. Create a professional online resume with multiple themes and easy customization.

---

## ✨ Features

- 🎨 **6 Beautiful Themes** - Choose from multiple color schemes and layouts
- 📱 **Fully Responsive** - Looks great on desktop, tablet, and mobile
- ⚡ **Easy Customization** - Simple Python dictionary configuration
- 🔧 **Flask-Powered** - Lightweight and fast web framework
- 🎯 **SEO Friendly** - Clean HTML structure for better search visibility
- 📊 **Skills Visualization** - Progress bars to showcase your expertise
- 🔗 **Social Integration** - LinkedIn, GitHub, Twitter, and more

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/nawrin-jahan7/Resume-builder.git
   cd Resume-builder
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Open your browser** and navigate to `http://127.0.0.1:5000`

---

## 🎨 Customizing Your Resume

### Method 1: Edit defaults.py directly

Modify the `app/defaults.py` file with your information:

```python
default_data = {
    'site_title': 'Your Name - Resume',
    'name': 'Your Name',
    'tagline': 'Your Job Title',
    'email': 'your.email@example.com',
    'phone': '+1 234 567 8900',
    'website': 'yourwebsite.com',
    'linkedin': 'linkedin.com/in/yourprofile',
    'github': 'github.com/yourusername',
    'twitter': '@yourhandle',
    # ... more fields
}
```

### Method 2: Create a custom resume file

1. Create a new file `my_resume.py` in the project root:

```python
resume_data = {
    'site_title': 'Jane Smith - Software Engineer',
    'name': 'Jane Smith',
    'tagline': 'Full Stack Developer',
    'email': 'jane@example.com',
    'phone': '+1 555 123 4567',
    'website': 'janesmith.dev',
    'linkedin': 'linkedin.com/in/janesmith',
    'github': 'github.com/janesmith',
    'twitter': '@janesmith',
    'languages': [
        ['English', ' (Native)'],
        ['Spanish', ' (Fluent)']
    ],
    'education': [
        ['MS Computer Science', 'MIT', '2018 - 2020'],
        ['BS Computer Science', 'Stanford', '2014 - 2018']
    ],
    'interests': ['Open Source', 'Machine Learning', 'Travel'],
    'skills': [
        ['Python', '95%'],
        ['JavaScript', '90%'],
        ['React', '85%'],
        ['Docker', '80%']
    ],
    'summary': '<p>Your professional summary here...</p>',
    'experience': [
        ['Senior Developer', '2020 - Present', 'Tech Corp', '<p>Description...</p>']
    ],
    'project_intro': '<p>Featured projects...</p>',
    'projects': [
        ['Project Name', 'Description', 'https://github.com/...']
    ]
}
```

2. Run with your custom data:

```python
import app
from my_resume import resume_data
app.create_app(resume_data).run()
```

---

## 📁 Project Structure

```
Resume-builder/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── defaults.py          # Default resume data
│   ├── main/
│   │   ├── __init__.py
│   │   └── views.py         # Route handlers
│   ├── static/
│   │   ├── css/             # Theme stylesheets
│   │   ├── images/          # Profile picture & assets
│   │   ├── js/              # JavaScript files
│   │   └── plugins/         # Bootstrap, Font Awesome
│   └── templates/
│       └── index.html       # Main template
├── requirements.txt         # Python dependencies
├── run.py                   # Application entry point
└── README.md
```

---

## 🎨 Available Themes

| Theme | File | Description |
|-------|------|-------------|
| Default | `styles.css` | Clean blue theme |
| Theme 2 | `styles-2.css` | Professional green |
| Theme 3 | `styles-3.css` | Modern purple |
| Theme 4 | `styles-4.css` | Elegant red |
| Theme 5 | `styles-5.css` | Corporate gray |
| Theme 6 | `styles-6.css` | Creative orange |

To change themes, update the CSS link in `app/templates/index.html`.

---

## 🛠️ Development

### Running in Debug Mode

```bash
FLASK_DEBUG=1 python run.py
```

### Compiling LESS to CSS

Each theme has LESS source files in `app/static/less/`. Use a LESS compiler to customize:

```bash
lessc app/static/less/default/styles.less app/static/css/styles.css
```

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgments

- Original design by [Xiaoying Riley](http://themes.3rdwavemedia.com)
- Built with [Flask](https://flask.palletsprojects.com/)
- Icons by [Font Awesome](https://fontawesome.com/)
- Styled with [Bootstrap](https://getbootstrap.com/)

---

## 👩‍💻 Author

**Nawrin Jahan**

- GitHub: [@nawrin-jahan7](https://github.com/nawrin-jahan7)

---

<p align="center">
  Made with ❤️ for developers
</p>
