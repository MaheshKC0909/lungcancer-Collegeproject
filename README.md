# Lung Cancer Detection Project

## Project Structure

This project follows a modular Django architecture with a separate API layer and distinct apps for different functionalities.

### Apps
- **users**: User authentication and management.
- **ct_scans**: Handling CT scan uploads, preprocessing, and management.
- **predictions**: Managing ML model predictions and results.
- **dashboard**: Analytics and visualization of dataset and model performance.
- **api**: REST API endpoints for external access.

### Data
The `data/` directory contains the dataset split into `train`, `test`, and `valid` sets, organized by class labels.

### Machine Learning
ML models and metadata are stored in `ml_models/`. Notebooks for experiments are in `notebooks/`.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Database Setup**:
   ```bash
   python scripts/setup_database.py
   ```

3. **Run Server**:
   ```bash
   python manage.py runserver
   ```
