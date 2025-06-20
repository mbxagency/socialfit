# Social FIT Data Intelligence Platform

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen.svg)]()
[![Tests](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)]()
[![Code Quality](https://img.shields.io/badge/Code%20Quality-A%2B-brightgreen.svg)]()

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
│   │   ├── __init__.py
│   │   └── etl_pipeline.py
│   ├── analytics/         # Analytics and insights engine
│   │   ├── __init__.py
│   │   └── analytics.py
│   ├── database/          # Database management
│   │   ├── __init__.py
│   │   └── database.py
│   ├── models/            # Data models and schemas
│   │   ├── __init__.py
│   │   └── models.py
│   ├── config/            # Configuration management
│   │   ├── __init__.py
│   │   └── config.py
│   ├── dashboard.py       # Web dashboard
│   └── app.py            # Main application entry point
├── tests/                 # Test suite
│   ├── unit/             # Unit tests
│   │   ├── test_models.py
│   │   └── test_etl.py
│   ├── integration/      # Integration tests
│   │   ├── test_pipeline.py
│   │   ├── test_database.py
│   │   └── test_supabase_connection.py
│   └── conftest.py       # Test configuration
├── scripts/              # Utility scripts
│   ├── create_tables_public_final.sql
│   └── debug_tables.py
├── docs/                 # Documentation
│   ├── API.md
│   ├── DEVELOPMENT.md
│   └── DEPLOYMENT.md
├── .github/workflows/    # CI/CD pipeline
│   └── ci.yml
├── data/                 # Data files
├── logs/                 # Application logs
├── main.py              # CLI entry point
├── Makefile             # Development automation
├── pyproject.toml       # Modern Python configuration
├── requirements.txt     # Python dependencies
└── README.md           # This file
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

### Development Features
- **Modular Architecture** - Clean separation of concerns
- **Comprehensive Testing** - Unit and integration tests
- **Code Quality Tools** - Black, flake8, mypy, bandit
- **CI/CD Pipeline** - Automated testing and deployment
- **Documentation** - Complete API and development guides

## 📋 Prerequisites

- Python 3.9 or higher
- Supabase account and project
- Access to Social FIT data sources

## 🛠️ Quick Start

### 1. Clone and Setup

```bash
# Clone the repository
git clone https://github.com/your-username/social_fit.git
cd social_fit

# Quick setup (recommended for new developers)
make quickstart
```

### 2. Manual Setup (Alternative)

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
pip install -e .[dev]

# Configure environment
cp env_example.txt .env
# Edit .env with your Supabase credentials
```

### 3. Configure Environment

Create a `.env` file with your credentials:

```env
# Supabase Configuration
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_ANON_KEY=your-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-service-role-key

# Application Configuration
DEBUG=True
LOG_LEVEL=INFO
BATCH_SIZE=100
```

### 4. Setup Database

```bash
# Run SQL script in Supabase SQL editor
# Copy content from scripts/create_tables_public_final.sql
```

### 5. Run the Pipeline

```bash
# Run complete ETL pipeline
make run

# Or use Python directly
python main.py
```

## 🚀 Usage

### Development Commands

```bash
# Quick start for new developers
make quickstart

# Run ETL pipeline
make run

# Run tests
make test

# Run specific test categories
make test-unit
make test-integration

# Code quality
make lint
make format

# Clean build artifacts
make clean

# Start dashboard
make dashboard

# View logs
make logs
```

### Python Commands

```bash
# Run ETL pipeline
python main.py

# Run with options
python main.py run          # Full pipeline
python main.py incremental  # Incremental update
python main.py test         # Test mode

# Run tests
pytest tests/
pytest tests/unit/
pytest tests/integration/

# Run with coverage
pytest --cov=src --cov-report=html
```

### Docker Commands

```bash
# Build and run with Docker
make docker-build
make docker-run

# Stop Docker container
make docker-stop
```

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
make test

# Run specific test categories
make test-unit
make test-integration

# Run with coverage
pytest --cov=src --cov-report=html

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
- Security scanning with bandit

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
- **v1.3.0** - Professional project structure and CI/CD

## 🙏 Acknowledgments

- Social FIT team for business requirements
- Supabase for the backend infrastructure
- Open source community for libraries and tools

---

**Built with ❤️ for Social FIT**