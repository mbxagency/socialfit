-- Create students table in public schema (accessible via Supabase API)
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

-- Create Instagram posts table in public schema
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

-- Create analytics table in public schema
CREATE TABLE IF NOT EXISTS analytics (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    metric_name VARCHAR(100) NOT NULL,
    metric_value JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Grant permissions to anon and service_role users
GRANT ALL ON ALL TABLES IN SCHEMA public TO anon, service_role;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO anon, service_role;

-- Set default permissions for future tables
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO anon, service_role;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO anon, service_role; 