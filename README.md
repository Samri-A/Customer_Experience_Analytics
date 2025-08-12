# Customer Experience Analytics

Customer Experience Analytics is a Django-based web application designed to analyze, process, and visualize customer experience data. The project leverages machine learning and data processing pipelines to extract insights from customer feedback, app reviews, and other data sources.

## Features
- Data ingestion and preprocessing from CSV and other sources
- Machine learning models for sentiment analysis and theme detection
- REST API endpoints for data access and analytics
- Frontend built with Vite for interactive data visualization
- Integration with vector stores for advanced search and retrieval

## Project Structure
```
Customer_Experience_Analytics/
├── anaylsis/                # Django app for analytics and ML
│   ├── data/                # Data files and vector store
│   ├── scripts/             # Data pipelines and utilities
│   ├── migrations/          # Django migrations
│   └── ...
├── Customer_Experience_Analytics/ # Django project settings
├── data/                    # Additional data and vector store
├── frontend/                # Frontend (Vite, React, etc.)
├── db.sqlite3               # SQLite database
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── package.json             # Frontend dependencies
└── README.md                # Project documentation
```

## Setup Instructions

### Backend (Django)
1. **Create and activate a virtual environment:**
	```powershell
	python -m venv env
	.\env\Scripts\activate
	```
2. **Install Python dependencies:**
	```powershell
	pip install -r requirements.txt
	```
3. **Apply migrations:**
	```powershell
	python manage.py migrate
	```
4. **Run the development server:**
	```powershell
	python manage.py runserver
	```

### Frontend (Vite)
1. **Install Node.js dependencies:**
	```powershell
	cd frontend
	npm install
	```
2. **Start the frontend development server:**
	```powershell
	npm run dev
	```

## Usage
- Access the backend API at `http://localhost:8000/`
- Access the frontend at `http://localhost:5173/` (default Vite port)

## Key Files
- `anaylsis/ml_model.py`: Machine learning models and utilities
- `anaylsis/scripts/playstore_data_pipeline.py`: Data pipeline for Play Store reviews
- `anaylsis/views.py`: API views for analytics endpoints
- `frontend/src/`: Frontend source code

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License.