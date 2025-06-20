# Social FIT Data Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()

A comprehensive ETL pipeline and analytics platform that integrates gym ERP data with social media analytics (Instagram) to generate actionable business insights for Social FIT.

## 🎯 Overview

Social FIT Data Intelligence Platform is a sophisticated data integration solution that combines:
- **Student Management Data** (enrollments, plans, demographics)
- **Instagram Analytics** (engagement, reach, follower growth)
- **Cross-Platform Insights** (correlation analysis, revenue impact)

The platform provides real-time analytics and actionable insights to optimize marketing strategies and business performance.

## 🏗️ Architecture

```
social_fit/
├── src/                    # Main source code
│   ├── etl/               # ETL pipeline components
│   ├── analytics/         # Analytics and insights engine
│   ├── database/          # Database management
│   ├── models/            # Data models and schemas
│   ├── config/            # Configuration management
│   ├── dashboard.py       # Web dashboard
│   └── main.py           # Main application entry point
├── tests/                 # Test suite
│   ├── unit/             # Unit tests
│   └── integration/      # Integration tests
├── scripts/              # Utility scripts
├── docs/                 # Documentation
├── data/                 # Data files
├── logs/                 # Application logs
├── main.py              # CLI entry point
└── requirements.txt     # Python dependencies
```

## 🚀 Features

### Core Functionality
- **Automated ETL Pipeline** - Extract, transform, and load data from multiple sources
- **Real-time Analytics** - Generate insights on student engagement and social media performance
- **Cross-Platform Correlation** - Analyze relationships between gym data and social media metrics
- **Actionable Insights** - Provide recommendations for business optimization

### Data Processing
- **Automatic Column Mapping** - Intelligent detection and mapping of CSV columns
- **Data Validation** - Robust validation using Pydantic models
- **Batch Processing** - Efficient handling of large datasets
- **Error Handling** - Comprehensive error management and logging

### Analytics Capabilities
- **Student Analytics** - Demographics, plan distribution, revenue analysis
- **Instagram Analytics** - Engagement rates, content performance, follower growth
- **Cross-Platform Insights** - Correlation analysis, optimal posting times, revenue impact

## 📋 Prerequisites

- Python 3.9 or higher
- Supabase account and project
- Access to Social FIT data sources

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/social_fit.git
   cd social_fit
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment**
   ```bash
   cp env_example.txt .env
   # Edit .env with your Supabase credentials
   ```

## ⚙️ Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# Database Configuration (optional)
DATABASE_URL=

# Application Configuration
DEBUG=True
LOG_LEVEL=INFO
BATCH_SIZE=100

# Dashboard Configuration
DASHBOARD_HOST=localhost
DASHBOARD_PORT=8050
```

### Supabase Setup

1. Create a new Supabase project
2. Execute the SQL script in `scripts/create_tables_public_final.sql`
3. Configure Row Level Security (RLS) policies as needed

## 🚀 Usage

### Running the ETL Pipeline

```bash
# Run the complete ETL pipeline
python main.py

# Run with specific options
python main.py run          # Full pipeline
python main.py incremental  # Incremental update
python main.py test         # Test mode
```

### Running Tests

```bash
# Run all tests
python -m pytest tests/

# Run specific test categories
python -m pytest tests/unit/
python -m pytest tests/integration/
```

### Running the Dashboard

```bash
python src/dashboard.py
```

Access the dashboard at `http://localhost:8050`

## 📊 Data Models

### Student Model
```python
class Student(BaseModel):
    id: int
    name: str
    gender: Gender
    birth_date: datetime
    address: str
    neighborhood: str
    plan_type: PlanType
    gympass: bool
    monthly_value: float
    total_value: float
    plan_start_date: datetime
    active_plan: bool
```

### Instagram Post Model
```python
class InstagramPost(BaseModel):
    date: datetime
    likes: int
    comments: int
    saves: int
    reach: int
    profile_visits: int
    new_followers: int
    main_hashtag: str
```

## 🔧 Development

### Project Structure

- **`src/etl/`** - ETL pipeline implementation
- **`src/analytics/`** - Analytics engine and insights generation
- **`src/database/`** - Database operations and management
- **`src/models/`** - Data models and validation schemas
- **`src/config/`** - Configuration management
- **`tests/`** - Test suite with unit and integration tests
- **`scripts/`** - Utility scripts for setup and maintenance

### Adding New Features

1. Create feature branch: `git checkout -b feature/new-feature`
2. Implement changes in appropriate module
3. Add tests in `tests/` directory
4. Update documentation
5. Submit pull request

### Code Style

- Follow PEP 8 guidelines
- Use type hints
- Add docstrings to all functions and classes
- Write comprehensive tests

## 🧪 Testing

### Test Structure

```
tests/
├── unit/                 # Unit tests
│   ├── test_etl.py      # ETL pipeline tests
│   ├── test_analytics.py # Analytics tests
│   └── test_models.py   # Model validation tests
└── integration/         # Integration tests
    ├── test_database.py # Database integration tests
    └── test_pipeline.py # End-to-end pipeline tests
```

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src

# Run specific test file
pytest tests/unit/test_etl.py

# Run with verbose output
pytest -v
```

## 📈 Analytics & Insights

The platform generates comprehensive analytics including:

### Student Analytics
- Total and active student counts
- Plan distribution analysis
- Revenue metrics
- Demographic insights

### Instagram Analytics
- Engagement rate calculations
- Content performance metrics
- Follower growth analysis
- Hashtag effectiveness

### Cross-Platform Insights
- Correlation between social media and enrollments
- Optimal posting times
- Revenue impact analysis
- Geographic insights

## 🔒 Security

- Environment variable management for sensitive data
- Supabase Row Level Security (RLS)
- Input validation and sanitization
- Secure credential handling

## 📝 Logging

The application uses structured logging with Loguru:

- **Console Output** - Colored, formatted logs
- **File Logging** - Rotated log files in `logs/` directory
- **Error Tracking** - Comprehensive error logging and monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Ensure all tests pass
6. Submit a pull request

### Development Guidelines

- Follow the existing code style
- Add comprehensive tests
- Update documentation
- Use meaningful commit messages

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

For support and questions:

- Create an issue in the GitHub repository
- Contact the development team
- Check the documentation in `docs/`

## 🔄 Version History

- **v1.0.0** - Initial release with ETL pipeline and analytics
- **v1.1.0** - Added dashboard and enhanced analytics
- **v1.2.0** - Improved error handling and performance

## 🙏 Acknowledgments

- Social FIT team for business requirements
- Supabase for the backend infrastructure
- Open source community for libraries and tools

---

**Built with ❤️ for Social FIT**