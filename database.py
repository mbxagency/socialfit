import pandas as pd
from supabase import create_client, Client
from sqlalchemy import create_engine, text
from loguru import logger
from typing import List, Dict, Any
import json

from config import settings, credential_manager
from models import Student, InstagramPost

class DatabaseManager:
    """Manages database connections and operations for Social FIT ETL."""
    
    def __init__(self):
        """Initialize database connections with professional credential management."""
        # Validate credentials before initializing
        if not credential_manager.validate_credentials():
            raise ValueError("Invalid Supabase credentials. Please check your configuration.")
        
        # Initialize Supabase client with validated credentials
        supabase_config = credential_manager.get_supabase_config()
        self.supabase: Client = create_client(supabase_config['url'], supabase_config['key'])
        
        # Initialize SQLAlchemy engine if direct database access is needed
        self.engine = None
        if settings.DATABASE_URL:
            self.engine = create_engine(settings.DATABASE_URL)
        
        logger.info("Database manager initialized successfully")
        
    def test_connection(self) -> bool:
        """Test database connection."""
        try:
            # Test Supabase connection
            result = self.supabase.table('students').select('count', count='exact').limit(1).execute()
            logger.info("✅ Supabase connection successful")
            return True
        except Exception as e:
            logger.error(f"❌ Database connection failed: {e}")
            return False
        
    def create_tables(self):
        """Create necessary tables in Supabase."""
        try:
            # Create students table
            students_table_sql = """
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                gender VARCHAR(1) NOT NULL,
                birth_date DATE NOT NULL,
                address TEXT NOT NULL,
                neighborhood VARCHAR(100) NOT NULL,
                plan_type VARCHAR(20) NOT NULL,
                gympass BOOLEAN DEFAULT FALSE,
                monthly_value DECIMAL(10,2) NOT NULL,
                total_value DECIMAL(10,2) NOT NULL,
                plan_start_date DATE NOT NULL,
                active_plan BOOLEAN DEFAULT TRUE,
                created_at TIMESTAMP DEFAULT NOW(),
                updated_at TIMESTAMP DEFAULT NOW()
            );
            """
            
            # Create Instagram posts table
            instagram_table_sql = """
            CREATE TABLE IF NOT EXISTS instagram_posts (
                id SERIAL PRIMARY KEY,
                post_date DATE NOT NULL,
                likes INTEGER NOT NULL,
                comments INTEGER NOT NULL,
                saves INTEGER NOT NULL,
                reach INTEGER NOT NULL,
                profile_visits INTEGER NOT NULL,
                new_followers INTEGER NOT NULL,
                main_hashtag VARCHAR(100) NOT NULL,
                engagement_rate DECIMAL(5,4),
                created_at TIMESTAMP DEFAULT NOW()
            );
            """
            
            # Create analytics table
            analytics_table_sql = """
            CREATE TABLE IF NOT EXISTS analytics (
                id SERIAL PRIMARY KEY,
                date DATE NOT NULL,
                metric_name VARCHAR(100) NOT NULL,
                metric_value JSONB NOT NULL,
                created_at TIMESTAMP DEFAULT NOW()
            );
            """
            
            # Execute table creation using Supabase
            # Note: In Supabase, tables are typically created through the dashboard
            # This is a fallback for programmatic creation
            logger.info("Tables will be created through Supabase dashboard or migrations")
            
            # Test if tables exist
            self._ensure_tables_exist()
            
        except Exception as e:
            logger.error(f"Error creating tables: {e}")
            raise
    
    def _ensure_tables_exist(self):
        """Ensure required tables exist in the database."""
        required_tables = ['students', 'instagram_posts', 'analytics']
        
        for table in required_tables:
            try:
                # Try to select from table to check if it exists
                self.supabase.table(table).select('*').limit(1).execute()
                logger.info(f"✅ Table '{table}' exists")
            except Exception as e:
                logger.warning(f"⚠️  Table '{table}' may not exist: {e}")
                logger.info(f"Please create table '{table}' in your Supabase dashboard")
    
    def insert_students(self, students: List[Student]) -> bool:
        """Insert students data into database."""
        try:
            students_data = []
            for student in students:
                students_data.append({
                    'name': student.name,
                    'gender': student.gender.value,
                    'birth_date': student.birth_date.date(),
                    'address': student.address,
                    'neighborhood': student.neighborhood,
                    'plan_type': student.plan_type.value,
                    'gympass': student.gympass,
                    'monthly_value': float(student.monthly_value),
                    'total_value': float(student.total_value),
                    'plan_start_date': student.plan_start_date.date(),
                    'active_plan': student.active_plan
                })
            
            # Insert using Supabase with batch processing
            batch_size = settings.BATCH_SIZE
            for i in range(0, len(students_data), batch_size):
                batch = students_data[i:i + batch_size]
                result = self.supabase.table('students').insert(batch).execute()
                logger.info(f"Inserted batch {i//batch_size + 1} of students")
            
            logger.info(f"✅ Inserted {len(students)} students successfully")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error inserting students: {e}")
            return False
    
    def insert_instagram_posts(self, posts: List[InstagramPost]) -> bool:
        """Insert Instagram posts data into database."""
        try:
            posts_data = []
            for post in posts:
                engagement_rate = (post.likes + post.comments + post.saves) / post.reach if post.reach > 0 else 0
                posts_data.append({
                    'post_date': post.date.date(),
                    'likes': post.likes,
                    'comments': post.comments,
                    'saves': post.saves,
                    'reach': post.reach,
                    'profile_visits': post.profile_visits,
                    'new_followers': post.new_followers,
                    'main_hashtag': post.main_hashtag,
                    'engagement_rate': round(engagement_rate, 4)
                })
            
            # Insert using Supabase with batch processing
            batch_size = settings.BATCH_SIZE
            for i in range(0, len(posts_data), batch_size):
                batch = posts_data[i:i + batch_size]
                result = self.supabase.table('instagram_posts').insert(batch).execute()
                logger.info(f"Inserted batch {i//batch_size + 1} of Instagram posts")
            
            logger.info(f"✅ Inserted {len(posts)} Instagram posts successfully")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error inserting Instagram posts: {e}")
            return False
    
    def insert_analytics(self, analytics_data: Dict[str, Any]) -> bool:
        """Insert analytics data into database."""
        try:
            analytics_record = {
                'date': analytics_data.get('date'),
                'metric_name': analytics_data.get('metric_name'),
                'metric_value': json.dumps(analytics_data.get('metric_value'))
            }
            
            # Insert using Supabase
            result = self.supabase.table('analytics').insert(analytics_record).execute()
            logger.info(f"✅ Inserted analytics data: {analytics_data.get('metric_name')}")
            return True
            
        except Exception as e:
            logger.error(f"❌ Error inserting analytics: {e}")
            return False
    
    def get_students(self) -> pd.DataFrame:
        """Retrieve students data from database."""
        try:
            result = self.supabase.table('students').select('*').execute()
            df = pd.DataFrame(result.data)
            logger.info(f"✅ Retrieved {len(df)} students from database")
            return df
        except Exception as e:
            logger.error(f"❌ Error retrieving students: {e}")
            return pd.DataFrame()
    
    def get_instagram_posts(self) -> pd.DataFrame:
        """Retrieve Instagram posts data from database."""
        try:
            result = self.supabase.table('instagram_posts').select('*').execute()
            df = pd.DataFrame(result.data)
            logger.info(f"✅ Retrieved {len(df)} Instagram posts from database")
            return df
        except Exception as e:
            logger.error(f"❌ Error retrieving Instagram posts: {e}")
            return pd.DataFrame()
    
    def get_analytics(self, metric_name: str = None) -> pd.DataFrame:
        """Retrieve analytics data from database."""
        try:
            query = self.supabase.table('analytics').select('*')
            if metric_name:
                query = query.eq('metric_name', metric_name)
            result = query.execute()
            df = pd.DataFrame(result.data)
            logger.info(f"✅ Retrieved {len(df)} analytics records from database")
            return df
        except Exception as e:
            logger.error(f"❌ Error retrieving analytics: {e}")
            return pd.DataFrame()
    
    def clear_tables(self, table_names: List[str] = None):
        """Clear data from specified tables (use with caution)."""
        if table_names is None:
            table_names = ['students', 'instagram_posts', 'analytics']
        
        for table in table_names:
            try:
                self.supabase.table(table).delete().neq('id', 0).execute()
                logger.info(f"✅ Cleared table: {table}")
            except Exception as e:
                logger.error(f"❌ Error clearing table {table}: {e}") 