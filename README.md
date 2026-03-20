# Book Recommender System

A machine learning-powered Book Recommender System that provides personalized book recommendations based on user reading preferences and habits. The system employs collaborative filtering and content-based filtering techniques to suggest books that align with users' interests.

**[📱 Live Demo](https://adil-book-recommender8.onrender.com/)** | **[🐳 Docker Hub](https://hub.docker.com/r/adilshamim/book-recommender)**

## Features
- **Personalized Recommendations**: Get book suggestions tailored to your reading history and preferences
- **Similar Book Discovery**: Find books similar to ones you've enjoyed in the past
- **User-friendly Interface**: Simple and intuitive design for seamless navigation
- **Diverse Book Collection**: Access recommendations from a vast library of books across various genres
- **Real-time Processing**: Quickly generate recommendations using optimized algorithms

## Tech Stack
| Component | Technology |
|-----------|-----------|
| **Backend** | Python, Flask |
| **ML Framework** | Scikit-learn, Pandas, NumPy |
| **Model Serialization** | Joblib |
| **Production Server** | Gunicorn |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Containerization** | Docker |
| **Hosting** | Render |
| **Server** | WSGI-compatible (Gunicorn) |

## Installation & Setup

### Method 1: Local Setup

1. **Clone the repository**
```bash
git clone https://github.com/AdilShamim8/Book-Recommender-System.git
cd Book-Recommender-System
```

2. **Create and activate a virtual environment**
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
   - Open your browser and navigate to `http://localhost:5000`

### Method 2: Docker Setup

**Using Docker Hub:**
```bash
docker run -p 5000:5000 adilshamim/book-recommender
```

The recommender system analyzes patterns in book metadata and user ratings using two complementary machine learning approaches:

### Recommendation Algorithms

1. **Collaborative Filtering**
   - Recommends books based on similarity between users
   - Uses TF-IDF vectorization for text feature extraction
   - Applies cosine similarity to find related books
   - Best for discovering new books similar to user preferences

```
Book-Recommender-System/
├── app.py                          # Flask application entry point
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Docker containerization config
├── LICENSE                         # MIT License
├── README.md                       # Project documentation
│
├── Datasets/
│   ├── README.md                   # Dataset documentation
│   └── [book and rating data]      # Raw and processed book datasets
│
├── static/
│   └── css/
│       └── style.css               # Application styling
│
├── templates/
│   ├── base.html                   # Base template with navigation
│   ├── index.html                  # Home page
│   ├── popular_books.html          # Popular books listing
│   ├── collaborative.html          # Collaborative filtering interface
│   └── personal.html               # Personalized recommendations
│
└── *.pkl (Model files)
    ├── popularity_model.pkl        # Pre-trained popularity rankings
    └── collab_model.pkl            # Pre-trained collaborative filtering model
    ↓
Search/Select Book
    ↓
TF-IDF Vectorization
    ↓
Cosine Similarity Computation
    ↓
Rank & Return Top 5 Books
```

The system uses pre-trained ML models for fast inference without requiring real-time retraining

The system leverages comprehensive book datasets containing:
- **Book Metadata**: Titles, authors, publishers, publication years
- **User Interactions**: Ratings and reviews data
- **Content Features**: Categories, genres, and textual descriptions
- **Popularity Metrics**: Books sorted by user engagement and ratings

All data is pre-processed and vectorized using TF-IDF to enable efficient similarity computations.
```
Book-Recommender-System/
├── Datasets/               # Contains book data and user ratings
├── Model/                  # ML models and preprocessing scripts
├── Website/                # Frontend implementation
│  Roadmap & Future Improvements

- [ ] **Hybrid Recommendations**: Combine collaborative + content-based filtering
- [ ] **User Authentication**: Persistent user profiles and history
- [ ] **Advanced NLP**: Sentiment analysis on book reviews
- [ ] **Mobile Optimization**: Responsive design for mobile devices
- [ ] **API Integration**: Connect with Goodreads/OpenLibrary APIs
- [Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author & Contact

**Adil Shamim**  
🌐 [Portfolio](https://adilshamim.me/)  
📧 [Email](mailto:adil@example.com)  
🐙 [GitHub](https://github.com/AdilShamim8)

## Acknowledgements

- [Goodreads](https://www.goodreads.com/) for inspiring this project
- Open-source community for excellent libraries (Flask, Scikit-learn, Pandas, etc.)
- Dataset providers for making book data accessible
- Render platform for hosting support

---

## Support

If you find this project helpful, please consider:
- ⭐ Giving it a star on GitHub
- 🐳 Using the Docker Hub image
- 📢 Sharing it with others
- 🐛 Reporting issues or suggesting improvements

**Happy Reading! 📚**d book metadata. It employs two main approaches:

1. **Collaborative Filtering**: Recommends books based on user similarity
2. **Content-Based Filtering**: Recommends books with similar content features

The system processes user input, compares it against the trained model, and generates a list of recommended books that the user might enjoy.

## Dataset
The recommendation system is built using the following datasets:
- Books metadata (titles, authors, publishers, etc.)
- User ratings and reviews
- Book categories and genres

## Future Improvements
- Implement hybrid recommendation techniques
- Add user authentication and profiles
- Incorporate natural language processing for review analysis
- Enhance mobile responsiveness
- Add book availability from various online stores

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author
- [Adil Shamim](https://adilshamim.me/)

## Acknowledgements
- [Goodreads](https://www.goodreads.com/) for the inspiration
- All the open-source libraries that made this project possible
- Dataset providers for making the book data accessible for analysis

---

If you find this project helpful, please consider giving it a star! ⭐
