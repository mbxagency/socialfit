# Social FIT Data Intelligence POC

A comprehensive data intelligence Proof of Concept (POC) for Social FIT Condicionamento Físico LTDA, integrating gym ERP data with social media analytics to generate actionable business insights.

## 🎯 Business Objectives

- **Convert social media engagement into gym enrollments**
- **Identify target audiences** based on social media behavior
- **Optimize content strategy** using data-driven insights
- **Measure business impact** of social media campaigns
- **Generate actionable insights** for business growth

## 🏗️ Architecture Overview

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Data Sources  │    │   ETL Pipeline  │    │   Analytics     │
│                 │    │                 │    │                 │
│ • Students CSV  │───▶│ • Data Loading  │───▶│ • Business      │
│ • Instagram CSV │    │ • Transformation│    │   Intelligence  │
│ • ERP Systems   │    │ • Loading       │    │ • Dashboards    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Supabase      │
                       │   Database      │
                       │                 │
                       │ • PostgreSQL    │
                       │ • Real-time     │
                       │ • Secure        │
                       └─────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Supabase account
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd social_fit
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp env_example.txt .env
   # Edit .env with your Supabase credentials
   ```

4. **Initialize Supabase**
   ```bash
   python supabase_setup.py
   ```

5. **Run ETL Pipeline**
   ```bash
   python main.py
   ```

6. **Launch Dashboard**
   ```bash
   python dashboard.py
   ```

## 📁 Project Structure

```
social_fit/
├── data/                          # Data files
│   ├── social_fit_students.csv    # Student data
│   └── social_fit_instagram_en.csv # Instagram analytics
├── config.py                      # Configuration management
├── models.py                      # Data models (Pydantic)
├── database.py                    # Database operations
├── etl_pipeline.py               # ETL orchestration
├── analytics.py                  # Business intelligence
├── dashboard.py                  # Interactive dashboard
├── main.py                       # Main application
├── supabase_setup.py            # Database initialization
├── test_etl.py                  # Test suite
├── requirements.txt              # Python dependencies
├── setup.py                      # Project setup
├── .env                          # Environment variables
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file based on `env_example.txt`:

```bash
# Supabase Configuration
SUPABASE_URL=your_supabase_project_url
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
SUPABASE_ANON_KEY=your_anon_key

# Data Sources
STUDENTS_CSV_PATH=data/social_fit_students.csv
INSTAGRAM_CSV_PATH=data/social_fit_instagram_en.csv

# Application Settings
DEBUG=True
LOG_LEVEL=INFO
```

### Supabase Setup

1. Create a Supabase project
2. Get your project URL and API keys
3. Update your `.env` file
4. Run `python supabase_setup.py` to initialize tables

## 📊 Data Models

### Student Data
- **ID**: Unique identifier
- **Name**: Student name
- **Gender**: M/F
- **Birth_Date**: Date of birth
- **Address**: Full address
- **Neighborhood**: Neighborhood
- **Plan_Type**: Monthly/Quarterly/Annual
- **Gympass**: Boolean flag
- **Monthly_Value_USD**: Monthly plan value
- **Total_Value_USD**: Total plan value
- **Plan_Start_Date**: Plan start date
- **Active_Plan**: Boolean flag

### Instagram Data
- **Date**: Post date
- **Likes**: Number of likes
- **Comments**: Number of comments
- **Saves**: Number of saves
- **Reach**: Post reach
- **Profile_Visits**: Profile visits from post
- **New_Followers**: New followers gained
- **Main_Hashtag**: Primary hashtag used

## 🔄 ETL Pipeline

The ETL pipeline processes data through three main stages:

### 1. Extract
- Load CSV files from data sources
- Validate data structure and types
- Handle missing values and errors

### 2. Transform
- Clean and standardize data
- Calculate derived metrics
- Apply business rules and transformations

### 3. Load
- Insert data into Supabase tables
- Handle duplicates and conflicts
- Maintain data integrity

## 📈 Analytics & Insights

### Key Metrics
- **Engagement Rate**: (Likes + Comments) / Reach
- **Conversion Rate**: New Followers / Profile Visits
- **Revenue per Student**: Total Value / Number of Students
- **Plan Distribution**: Monthly vs Quarterly vs Annual

### Business Intelligence
- **Audience Analysis**: Demographics and behavior patterns
- **Content Performance**: Best performing hashtags and content types
- **Revenue Optimization**: Plan type analysis and pricing insights
- **Growth Forecasting**: Trend analysis and predictions

## 🎛️ Dashboard Features

### Interactive Visualizations
- **Real-time Metrics**: Live updates of key performance indicators
- **Engagement Analytics**: Social media performance tracking
- **Revenue Dashboard**: Financial insights and trends
- **Audience Insights**: Demographics and behavior analysis

### Filtering & Drill-down
- **Date Range Selection**: Custom time periods
- **Plan Type Filtering**: Filter by subscription type
- **Geographic Analysis**: Neighborhood-based insights
- **Performance Comparison**: Before/after analysis

## 🧪 Testing

Run the test suite to ensure data integrity:

```bash
python test_etl.py
```

Tests cover:
- Data validation
- ETL pipeline functionality
- Database operations
- Analytics calculations

## 🔒 Security

### Credential Management
- Environment variables for sensitive data
- Secure credential loading
- No hardcoded secrets

### Data Protection
- Encrypted database connections
- Secure API key handling
- Access control and permissions

## 📝 API Documentation

### Database Operations
```python
from database import DatabaseManager

# Initialize database
db = DatabaseManager()

# Insert student data
db.insert_students(students_data)

# Query analytics
results = db.query_analytics()
```

### Analytics Functions
```python
from analytics import AnalyticsEngine

# Initialize analytics
analytics = AnalyticsEngine()

# Get engagement metrics
engagement = analytics.get_engagement_metrics()

# Generate insights
insights = analytics.generate_insights()
```

## 🚀 Deployment

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Run development server
python dashboard.py
```

### Production Deployment
1. Set up production Supabase instance
2. Configure production environment variables
3. Set up monitoring and logging
4. Deploy to cloud platform (Heroku, AWS, etc.)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is proprietary software for Social FIT Condicionamento Físico LTDA.

## 📞 Support

For technical support or questions:
- Create an issue in the repository
- Contact the development team
- Check the documentation

## 🔄 Version History

- **v1.0.0**: Initial POC release
  - Basic ETL pipeline
  - Supabase integration
  - Analytics dashboard
  - Data models and validation

---

**Social FIT Data Intelligence POC** - Transforming gym data into actionable business insights.