# Book Recommender System

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)  
[![Notebook](https://img.shields.io/badge/jupyter-notebook-orange)](https://jupyter.org/)  
[![Flask](https://img.shields.io/badge/flask-3.0.3-lightgrey)](https://flask.palletsprojects.com/)  
[![Scikit-learn](https://img.shields.io/badge/scikit--learn-1.6.1-green)](https://scikit-learn.org/)

**Live Demo:** [https://adil-book-recommender.onrender.com](https://adil-book-recommender.onrender.com)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Datasets](#datasets)
- [Model](#model)
- [Web Application](#web-application)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Overview

The **Book Recommender System** is an end-to-end project that leverages machine learning algorithms to deliver personalized book recommendations. By analyzing user preferences and reading history, the system suggests books tailored to individual tastes, improving discovery and reader satisfaction.

---

## Features

- **Personalized Recommendations:** Suggestions based on both collaborative filtering and popularity metrics.
- **Hybrid Recommendation Engine:** Combines popularity-based and collaborative filtering methods for balanced results.
- **Interactive Feedback:** Users can rate recommendations to refine future suggestions.
- **Restful Web API:** Provides endpoints for integration with other services or front-ends.
- **Live Deployment:** Hosted on Render with automatic updates.

---

## Architecture

![Architecture Diagram](docs/architecture-diagram.png)

1. **Data Layer:** CSV datasets stored in `Datasets/`, sourced from [Kaggle](https://www.kaggle.com/datasets/adilshamim8/books-datasets).
2. **Model Layer:** Jupyter Notebook in `Model/` for preprocessing, training, and persisting models (`popularity_model.pkl`, `collab_model.pkl`).
3. **Application Layer:** Flask app in `Website/` exposing recommendation endpoints and rendering HTML templates.

---

## Technologies

- **Python 3.8+**
- **Pandas & NumPy** for data manipulation
- **Scikit-learn** for model training
- **Joblib** for model serialization
- **Flask** for web application
- **Jinja2** templating
- **Bootstrap 5** for UI styling

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AdilShamim8/Book-Recommender-System.git
   cd Book-Recommender-System
   ```

2. **Navigate to the Website folder**
   ```bash
   cd Website
   ```

3. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```


### Running the Application

1. **Start the Flask server**
   ```bash
   flask run --host=0.0.0.0 --port=5000
   ```

2. **Open your browser** and navigate to `http://localhost:5000` to interact with the recommender.

---

## Project Structure

```
Book-Recommender-System/
├── Datasets/             # Raw CSV files and dataset metadata
├── Model/                # Jupyter Notebook for training & model artifacts
│   └── book-recommender-system.ipynb
├── Website/              # Flask web application
│   ├── app.py
│   ├── requirements.txt
│   ├── collab_model.pkl
│   ├── popularity_model.pkl
│   ├── templates/        # Jinja2 HTML templates
│   └── static/           # CSS & JS assets
└── README.md             # Project overview and setup instructions
```

---

## Datasets

The book dataset is hosted on Kaggle and contains over 100,000 book entries with features such as title, author, genre, ratings, and description.

- **Kaggle Link:** https://www.kaggle.com/datasets/adilshamim8/books-datasets

---

## Model

Model training and evaluation are performed in the Jupyter Notebook located in the `Model/` directory. The notebook covers:

- Data cleaning and preprocessing
- Feature engineering
- Training popularity-based and collaborative filtering models
- Model evaluation and selection
- Exporting trained models to `Website/` for deployment

---

## Web Application

The Flask application in the `Website/` folder provides:

- **Home Page:** Displays popular book recommendations
- **User Portal:** Allows users to input book preferences and receive recommendations
- **API Endpoints:** `/recommend/popular` and `/recommend/collaborative` for programmatic access

---

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Contact

* **Author:** Adil Shamim
* **Email:** [adilshamim696@gmail,com]
* **Website:** adilshamim.me

