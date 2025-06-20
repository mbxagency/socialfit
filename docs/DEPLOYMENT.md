# Social FIT Data Intelligence Platform - Deployment Guide

## Overview

This guide covers deploying the Social FIT Data Intelligence Platform to various environments, from development to production.

## Deployment Options

### 1. Local Development
### 2. Docker Containerization
### 3. Cloud Deployment (AWS, GCP, Azure)
### 4. Serverless Deployment
### 5. CI/CD Pipeline

## Local Development Deployment

### Prerequisites

- Python 3.9+
- Virtual environment
- Supabase project
- Required data files

### Setup Steps

1. **Environment Setup**
   ```bash
   # Clone repository
   git clone https://github.com/your-username/social_fit.git
   cd social_fit
   
   # Create virtual environment
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

2. **Configuration**
   ```bash
   # Copy environment template
   cp env_example.txt .env
   
   # Edit .env with your credentials
   nano .env
   ```

3. **Database Setup**
   ```bash
   # Run SQL script in Supabase SQL editor
   # Copy content from scripts/create_tables_public_final.sql
   ```

4. **Test Deployment**
   ```bash
   # Run tests
   pytest
   
   # Run ETL pipeline
   python main.py
   
   # Start dashboard
   python src/dashboard.py
   ```

## Docker Deployment

### Dockerfile

```dockerfile
# Use Python 3.9 slim image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Create non-root user
RUN useradd --create-home --shell /bin/bash app \
    && chown -R app:app /app
USER app

# Create necessary directories
RUN mkdir -p logs data

# Expose port for dashboard
EXPOSE 8050

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8050/health')"

# Default command
CMD ["python", "main.py"]
```

### Docker Compose

```yaml
# docker-compose.yml
version: '3.8'

services:
  social-fit:
    build: .
    ports:
      - "8050:8050"
    environment:
      - SUPABASE_URL=${SUPABASE_URL}
      - SUPABASE_ANON_KEY=${SUPABASE_ANON_KEY}
      - SUPABASE_SERVICE_ROLE_KEY=${SUPABASE_SERVICE_ROLE_KEY}
      - DEBUG=False
      - LOG_LEVEL=INFO
      - BATCH_SIZE=1000
    volumes:
      - ./data:/app/data
      - ./logs:/app/logs
    restart: unless-stopped
    healthcheck:
      test: ["CMD", "python", "-c", "import requests; requests.get('http://localhost:8050/health')"]
      interval: 30s
      timeout: 10s
      retries: 3

  # Optional: Add PostgreSQL for local development
  postgres:
    image: postgres:13
    environment:
      POSTGRES_DB: social_fit
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Docker Deployment Commands

```bash
# Build image
docker build -t social-fit .

# Run container
docker run -d \
  --name social-fit \
  -p 8050:8050 \
  --env-file .env \
  -v $(pwd)/data:/app/data \
  -v $(pwd)/logs:/app/logs \
  social-fit

# Using Docker Compose
docker-compose up -d

# View logs
docker logs social-fit

# Stop container
docker stop social-fit
```

## Cloud Deployment

### AWS Deployment

#### EC2 Deployment

1. **Launch EC2 Instance**
   ```bash
   # Connect to EC2 instance
   ssh -i your-key.pem ubuntu@your-instance-ip
   
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python and dependencies
   sudo apt install python3 python3-pip python3-venv -y
   ```

2. **Deploy Application**
   ```bash
   # Clone repository
   git clone https://github.com/your-username/social_fit.git
   cd social_fit
   
   # Setup virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Configure environment
   cp env_example.txt .env
   nano .env  # Edit with production credentials
   ```

3. **Setup Systemd Service**
   ```bash
   # Create service file
   sudo nano /etc/systemd/system/social-fit.service
   ```

   ```ini
   [Unit]
   Description=Social FIT Data Intelligence Platform
   After=network.target
   
   [Service]
   Type=simple
   User=ubuntu
   WorkingDirectory=/home/ubuntu/social_fit
   Environment=PATH=/home/ubuntu/social_fit/venv/bin
   ExecStart=/home/ubuntu/social_fit/venv/bin/python main.py
   Restart=always
   RestartSec=10
   
   [Install]
   WantedBy=multi-user.target
   ```

4. **Start Service**
   ```bash
   sudo systemctl daemon-reload
   sudo systemctl enable social-fit
   sudo systemctl start social-fit
   sudo systemctl status social-fit
   ```

#### ECS Deployment

1. **Create ECS Task Definition**
   ```json
   {
     "family": "social-fit",
     "networkMode": "awsvpc",
     "requiresCompatibilities": ["FARGATE"],
     "cpu": "512",
     "memory": "1024",
     "executionRoleArn": "arn:aws:iam::account:role/ecsTaskExecutionRole",
     "containerDefinitions": [
       {
         "name": "social-fit",
         "image": "your-account.dkr.ecr.region.amazonaws.com/social-fit:latest",
         "portMappings": [
           {
             "containerPort": 8050,
             "protocol": "tcp"
           }
         ],
         "environment": [
           {
             "name": "SUPABASE_URL",
             "value": "https://your-project.supabase.co"
           },
           {
             "name": "SUPABASE_ANON_KEY",
             "value": "your-anon-key"
           },
           {
             "name": "SUPABASE_SERVICE_ROLE_KEY",
             "value": "your-service-role-key"
           }
         ],
         "logConfiguration": {
           "logDriver": "awslogs",
           "options": {
             "awslogs-group": "/ecs/social-fit",
             "awslogs-region": "us-east-1",
             "awslogs-stream-prefix": "ecs"
           }
         }
       }
     ]
   }
   ```

2. **Deploy to ECS**
   ```bash
   # Build and push Docker image
   aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin your-account.dkr.ecr.us-east-1.amazonaws.com
   
   docker build -t social-fit .
   docker tag social-fit:latest your-account.dkr.ecr.us-east-1.amazonaws.com/social-fit:latest
   docker push your-account.dkr.ecr.us-east-1.amazonaws.com/social-fit:latest
   
   # Create ECS service
   aws ecs create-service \
     --cluster your-cluster \
     --service-name social-fit \
     --task-definition social-fit:1 \
     --desired-count 1 \
     --launch-type FARGATE \
     --network-configuration "awsvpcConfiguration={subnets=[subnet-12345],securityGroups=[sg-12345],assignPublicIp=ENABLED}"
   ```

### Google Cloud Platform (GCP)

#### Cloud Run Deployment

1. **Build and Deploy**
   ```bash
   # Build container
   gcloud builds submit --tag gcr.io/your-project/social-fit
   
   # Deploy to Cloud Run
   gcloud run deploy social-fit \
     --image gcr.io/your-project/social-fit \
     --platform managed \
     --region us-central1 \
     --allow-unauthenticated \
     --set-env-vars SUPABASE_URL=https://your-project.supabase.co \
     --set-env-vars SUPABASE_ANON_KEY=your-anon-key \
     --set-env-vars SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
   ```

2. **Setup Cloud Scheduler**
   ```bash
   # Create scheduled job for ETL pipeline
   gcloud scheduler jobs create http social-fit-etl \
     --schedule="0 6 * * *" \
     --uri="https://your-service-url/run-etl" \
     --http-method=POST \
     --headers="Authorization=Bearer your-auth-token"
   ```

### Azure Deployment

#### Azure Container Instances

```bash
# Deploy to Azure Container Instances
az container create \
  --resource-group your-resource-group \
  --name social-fit \
  --image your-registry.azurecr.io/social-fit:latest \
  --dns-name-label social-fit \
  --ports 8050 \
  --environment-variables \
    SUPABASE_URL=https://your-project.supabase.co \
    SUPABASE_ANON_KEY=your-anon-key \
    SUPABASE_SERVICE_ROLE_KEY=your-service-role-key
```

## Serverless Deployment

### AWS Lambda

1. **Create Lambda Function**
   ```python
   # lambda_function.py
   import json
   import sys
   from pathlib import Path
   
   # Add src to path
   sys.path.insert(0, str(Path(__file__).parent / "src"))
   
   from src.etl import SocialFITETL
   from loguru import logger
   
   def lambda_handler(event, context):
       """AWS Lambda handler for ETL pipeline"""
       try:
           etl = SocialFITETL()
           success = etl.run_full_pipeline()
           
           return {
               'statusCode': 200 if success else 500,
               'body': json.dumps({
                   'success': success,
                   'message': 'ETL pipeline completed' if success else 'ETL pipeline failed'
               })
           }
       except Exception as e:
           logger.error(f"Lambda execution failed: {e}")
           return {
               'statusCode': 500,
               'body': json.dumps({
                   'success': False,
                   'error': str(e)
               })
           }
   ```

2. **Deploy Lambda**
   ```bash
   # Create deployment package
   zip -r lambda-deployment.zip . -x "*.git*" "tests/*" "docs/*"
   
   # Create Lambda function
   aws lambda create-function \
     --function-name social-fit-etl \
     --runtime python3.9 \
     --role arn:aws:iam::account:role/lambda-execution-role \
     --handler lambda_function.lambda_handler \
     --zip-file fileb://lambda-deployment.zip \
     --timeout 900 \
     --memory-size 1024
   ```

## CI/CD Pipeline

### GitHub Actions

```yaml
# .github/workflows/deploy.yml
name: Deploy Social FIT

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest --cov=src --cov-report=xml
    
    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  deploy:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v2
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-east-1
    
    - name: Login to Amazon ECR
      id: login-ecr
      uses: aws-actions/amazon-ecr-login@v1
    
    - name: Build and push Docker image
      env:
        ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
        ECR_REPOSITORY: social-fit
        IMAGE_TAG: ${{ github.sha }}
      run: |
        docker build -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
        docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
    
    - name: Deploy to ECS
      run: |
        aws ecs update-service \
          --cluster your-cluster \
          --service social-fit \
          --force-new-deployment
```

## Environment Configuration

### Production Environment Variables

```env
# Supabase Configuration
SUPABASE_URL=https://your-production-project.supabase.co
SUPABASE_ANON_KEY=your-production-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-production-service-role-key

# Application Configuration
DEBUG=False
LOG_LEVEL=WARNING
BATCH_SIZE=1000

# Dashboard Configuration
DASHBOARD_HOST=0.0.0.0
DASHBOARD_PORT=8050

# Security
SECRET_KEY=your-production-secret-key
ALLOWED_HOSTS=your-domain.com,www.your-domain.com
```

### Environment-Specific Configurations

```python
# src/config/config.py
import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Environment detection
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Supabase Configuration
    SUPABASE_URL: str
    SUPABASE_ANON_KEY: str
    SUPABASE_SERVICE_ROLE_KEY: str
    
    # Application Configuration
    DEBUG: bool = ENVIRONMENT == "development"
    LOG_LEVEL: str = "DEBUG" if ENVIRONMENT == "development" else "WARNING"
    BATCH_SIZE: int = 50 if ENVIRONMENT == "development" else 1000
    
    # Security
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev-secret-key")
    ALLOWED_HOSTS: list = ["localhost", "127.0.0.1"]
    
    class Config:
        env_file = ".env"
```

## Monitoring and Logging

### Application Monitoring

```python
# src/monitoring.py
import time
import psutil
from loguru import logger
from typing import Dict, Any

class ApplicationMonitor:
    """Monitor application performance and health"""
    
    @staticmethod
    def get_system_metrics() -> Dict[str, Any]:
        """Get system performance metrics"""
        return {
            "cpu_percent": psutil.cpu_percent(),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_usage": psutil.disk_usage('/').percent,
            "timestamp": time.time()
        }
    
    @staticmethod
    def health_check() -> Dict[str, Any]:
        """Perform application health check"""
        try:
            from src.database import DatabaseManager
            from src.etl import SocialFITETL
            
            # Test database connection
            db = DatabaseManager()
            db_healthy = db.test_connection()
            
            # Test ETL pipeline
            etl = SocialFITETL()
            etl_healthy = etl.extract_data() is not None
            
            return {
                "status": "healthy" if db_healthy and etl_healthy else "unhealthy",
                "database": "connected" if db_healthy else "disconnected",
                "etl_pipeline": "operational" if etl_healthy else "failed",
                "timestamp": time.time()
            }
        except Exception as e:
            logger.error(f"Health check failed: {e}")
            return {
                "status": "unhealthy",
                "error": str(e),
                "timestamp": time.time()
            }
```

### Logging Configuration

```python
# src/logging_config.py
import sys
from loguru import logger
from pathlib import Path

def setup_logging(environment: str = "development"):
    """Setup logging configuration based on environment"""
    
    # Remove default handler
    logger.remove()
    
    # Console logging
    logger.add(
        sys.stdout,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level="DEBUG" if environment == "development" else "INFO"
    )
    
    # File logging
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    
    logger.add(
        log_dir / "social_fit.log",
        rotation="1 day",
        retention="30 days",
        compression="zip",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="DEBUG" if environment == "development" else "WARNING"
    )
    
    # Error logging
    logger.add(
        log_dir / "errors.log",
        rotation="1 day",
        retention="90 days",
        compression="zip",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        level="ERROR",
        backtrace=True,
        diagnose=True
    )
```

## Security Considerations

### Environment Security

1. **Secrets Management**
   ```bash
   # Use AWS Secrets Manager
   aws secretsmanager create-secret \
     --name social-fit/supabase-credentials \
     --description "Social FIT Supabase credentials" \
     --secret-string '{"url":"https://your-project.supabase.co","anon_key":"your-key","service_role_key":"your-key"}'
   ```

2. **Network Security**
   ```bash
   # Configure security groups (AWS)
   aws ec2 create-security-group \
     --group-name social-fit-sg \
     --description "Security group for Social FIT"
   
   aws ec2 authorize-security-group-ingress \
     --group-name social-fit-sg \
     --protocol tcp \
     --port 8050 \
     --cidr 0.0.0.0/0
   ```

3. **SSL/TLS Configuration**
   ```python
   # Dashboard SSL configuration
   import ssl
   
   ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
   ssl_context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")
   
   app.run_server(
       host="0.0.0.0",
       port=8050,
       ssl_context=ssl_context
   )
   ```

## Backup and Recovery

### Database Backup

```python
# scripts/backup.py
import os
import subprocess
from datetime import datetime
from pathlib import Path

def backup_database():
    """Create database backup"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir = Path("backups")
    backup_dir.mkdir(exist_ok=True)
    
    backup_file = backup_dir / f"social_fit_backup_{timestamp}.sql"
    
    # Create backup using pg_dump
    subprocess.run([
        "pg_dump",
        "-h", "your-supabase-host",
        "-U", "postgres",
        "-d", "postgres",
        "-f", str(backup_file)
    ])
    
    print(f"Backup created: {backup_file}")

if __name__ == "__main__":
    backup_database()
```

### Data Recovery

```python
# scripts/recovery.py
import subprocess
from pathlib import Path

def restore_database(backup_file: str):
    """Restore database from backup"""
    backup_path = Path("backups") / backup_file
    
    if not backup_path.exists():
        raise FileNotFoundError(f"Backup file not found: {backup_path}")
    
    # Restore using psql
    subprocess.run([
        "psql",
        "-h", "your-supabase-host",
        "-U", "postgres",
        "-d", "postgres",
        "-f", str(backup_path)
    ])
    
    print(f"Database restored from: {backup_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        restore_database(sys.argv[1])
    else:
        print("Usage: python recovery.py <backup_file>")
```

## Performance Optimization

### Production Optimizations

1. **Database Connection Pooling**
   ```python
   from sqlalchemy import create_engine
   
   engine = create_engine(
       DATABASE_URL,
       pool_size=20,
       max_overflow=30,
       pool_pre_ping=True,
       pool_recycle=3600
   )
   ```

2. **Caching**
   ```python
   import redis
   from functools import wraps
   
   redis_client = redis.Redis(host='localhost', port=6379, db=0)
   
   def cache_result(expire_time=3600):
       def decorator(func):
           @wraps(func)
           def wrapper(*args, **kwargs):
               cache_key = f"{func.__name__}:{hash(str(args) + str(kwargs))}"
               result = redis_client.get(cache_key)
               
               if result is None:
                   result = func(*args, **kwargs)
                   redis_client.setex(cache_key, expire_time, str(result))
               
               return result
           return wrapper
       return decorator
   ```

3. **Async Processing**
   ```python
   import asyncio
   import aiohttp
   
   async def async_etl_pipeline():
       """Async ETL pipeline for better performance"""
       async with aiohttp.ClientSession() as session:
           # Parallel data extraction
           tasks = [
               extract_students_data(session),
               extract_instagram_data(session)
           ]
           results = await asyncio.gather(*tasks)
           
           # Process results
           students_data, instagram_data = results
           # ... processing logic
   ```

## Troubleshooting

### Common Deployment Issues

1. **Database Connection Issues**
   ```bash
   # Test database connection
   python -c "
   from src.database import DatabaseManager
   db = DatabaseManager()
   print('Connection successful' if db.test_connection() else 'Connection failed')
   "
   ```

2. **Memory Issues**
   ```bash
   # Monitor memory usage
   ps aux | grep python
   free -h
   ```

3. **Port Conflicts**
   ```bash
   # Check port usage
   netstat -tulpn | grep 8050
   lsof -i :8050
   ```

### Debug Commands

```bash
# View application logs
tail -f logs/social_fit.log

# Check system resources
htop
df -h
free -h

# Test application endpoints
curl http://localhost:8050/health
curl http://localhost:8050/run-etl

# Database connection test
python -c "
import os
from supabase import create_client
url = os.getenv('SUPABASE_URL')
key = os.getenv('SUPABASE_ANON_KEY')
supabase = create_client(url, key)
print('Supabase connection successful')
"
```

## Maintenance

### Regular Maintenance Tasks

1. **Log Rotation**
   ```bash
   # Setup logrotate
   sudo nano /etc/logrotate.d/social-fit
   ```

   ```
   /path/to/social_fit/logs/*.log {
       daily
       rotate 30
       compress
       delaycompress
       missingok
       notifempty
       create 644 ubuntu ubuntu
   }
   ```

2. **Database Maintenance**
   ```sql
   -- Run in Supabase SQL editor
   VACUUM ANALYZE;
   REINDEX DATABASE postgres;
   ```

3. **Application Updates**
   ```bash
   # Update application
   git pull origin main
   pip install -r requirements.txt
   sudo systemctl restart social-fit
   ```

### Monitoring Setup

```python
# monitoring_setup.py
import schedule
import time
from src.monitoring import ApplicationMonitor

def monitor_application():
    """Monitor application health"""
    metrics = ApplicationMonitor.get_system_metrics()
    health = ApplicationMonitor.health_check()
    
    # Log metrics
    logger.info(f"System metrics: {metrics}")
    logger.info(f"Health status: {health}")
    
    # Alert if unhealthy
    if health["status"] == "unhealthy":
        # Send alert (email, Slack, etc.)
        send_alert(f"Application unhealthy: {health}")

# Schedule monitoring
schedule.every(5).minutes.do(monitor_application)

while True:
    schedule.run_pending()
    time.sleep(60)
``` 