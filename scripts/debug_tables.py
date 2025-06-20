#!/usr/bin/env python3
"""
Debug script to check table existence and identify issues.
"""

import os
from dotenv import load_dotenv
from supabase import create_client, Client
import json

# Load environment variables
load_dotenv()

def debug_tables():
    """Debug table existence and access issues."""
    print("🔍 Debugging Supabase Tables...")
    print("=" * 50)
    
    # Create client
    supabase_url = os.getenv('SUPABASE_URL')
    supabase_anon_key = os.getenv('SUPABASE_ANON_KEY')
    
    supabase: Client = create_client(supabase_url, supabase_anon_key)
    
    # Test different table access methods
    tables_to_test = ['students', 'instagram_posts', 'analytics']
    
    for table in tables_to_test:
        print(f"\n🔄 Testing table: {table}")
        
        try:
            # Try to select from table
            result = supabase.table(table).select('*').limit(1).execute()
            print(f"✅ Table '{table}' exists and is accessible")
            print(f"   Data: {result.data}")
        except Exception as e:
            print(f"❌ Table '{table}' error: {e}")
            
            # Try to get table info
            try:
                result = supabase.table(table).select('count', count='exact').execute()
                print(f"   Count query worked: {result}")
            except Exception as count_error:
                print(f"   Count query failed: {count_error}")
    
    # Test schema-specific queries
    print(f"\n🔄 Testing schema-specific access...")
    try:
        # Try to query with schema
        result = supabase.rpc('get_schema_tables', {'schema_name': 'social_fit'}).execute()
        print(f"✅ Schema query result: {result}")
    except Exception as e:
        print(f"❌ Schema query failed: {e}")
    
    # Test raw SQL if possible
    print(f"\n🔄 Testing raw SQL...")
    try:
        result = supabase.rpc('exec_sql', {'sql': 'SELECT table_name FROM information_schema.tables WHERE table_schema = \'social_fit\''}).execute()
        print(f"✅ Raw SQL result: {result}")
    except Exception as e:
        print(f"❌ Raw SQL failed: {e}")

if __name__ == "__main__":
    debug_tables() 