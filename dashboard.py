#!/usr/bin/env python3
"""
Social FIT Analytics Dashboard

Simple dashboard to display analytics results from the ETL pipeline.
This provides a quick overview of key metrics and insights.
"""

import pandas as pd
import json
from datetime import datetime
from typing import Dict, Any

from database import DatabaseManager
from analytics import AnalyticsEngine

class SocialFITDashboard:
    """Dashboard for Social FIT analytics."""
    
    def __init__(self):
        """Initialize dashboard."""
        self.db_manager = DatabaseManager()
        self.analytics_engine = AnalyticsEngine()
    
    def get_latest_analytics(self) -> Dict[str, Any]:
        """Get the latest analytics data."""
        try:
            analytics_df = self.db_manager.get_analytics('comprehensive_analytics')
            if not analytics_df.empty:
                latest = analytics_df.iloc[-1]
                return json.loads(latest['metric_value'])
            return {}
        except Exception as e:
            print(f"Error getting analytics: {e}")
            return {}
    
    def display_summary(self):
        """Display summary dashboard."""
        print("=" * 80)
        print("🏋️  SOCIAL FIT ANALYTICS DASHBOARD")
        print("=" * 80)
        print(f"📅 Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print()
        
        # Get latest analytics
        analytics = self.get_latest_analytics()
        
        if not analytics:
            print("❌ No analytics data available. Run the ETL pipeline first.")
            return
        
        # Display student metrics
        if 'students_analytics' in analytics:
            students = analytics['students_analytics']
            print("👥 STUDENT METRICS")
            print("-" * 40)
            print(f"Total Students: {students['total_students']}")
            print(f"Active Students: {students['active_students']}")
            print(f"Inactive Students: {students['inactive_students']}")
            print(f"Gympass Users: {students['gympass_users']}")
            print(f"Average Monthly Value: R$ {students['average_monthly_value']}")
            print(f"Total Monthly Revenue: R$ {students['total_monthly_revenue']}")
            print()
        
        # Display Instagram metrics
        if 'instagram_analytics' in analytics:
            instagram = analytics['instagram_analytics']
            print("📱 INSTAGRAM METRICS")
            print("-" * 40)
            print(f"Total Posts: {instagram['total_posts']}")
            print(f"Total Likes: {instagram['total_likes']:,}")
            print(f"Total Comments: {instagram['total_comments']:,}")
            print(f"Total Saves: {instagram['total_saves']:,}")
            print(f"Total Reach: {instagram['total_reach']:,}")
            print(f"Total New Followers: {instagram['total_new_followers']:,}")
            print(f"Average Engagement Rate: {instagram['average_engagement_rate']:.2%}")
            print()
        
        # Display cross-platform insights
        if 'cross_platform_analytics' in analytics:
            cross_platform = analytics['cross_platform_analytics']
            print("🔗 CROSS-PLATFORM INSIGHTS")
            print("-" * 40)
            print(f"Engagement-Enrollment Correlation: {cross_platform['correlation_score']:.2%}")
            print(f"Engagement to Enrollment Rate: {cross_platform['engagement_to_enrollment_rate']:.6f}")
            print(f"Estimated Revenue Impact: R$ {cross_platform['revenue_impact']:,.2f}")
            print()
        
        # Display actionable insights
        if 'actionable_insights' in analytics:
            insights = analytics['actionable_insights']
            print("🎯 ACTIONABLE INSIGHTS")
            print("-" * 40)
            for i, insight in enumerate(insights, 1):
                print(f"{i}. {insight['title']}")
                print(f"   📝 {insight['description']}")
                print(f"   ✅ Action: {insight['action']}")
                print(f"   📊 Impact: {insight['impact']}")
                print()
    
    def display_detailed_analytics(self):
        """Display detailed analytics breakdown."""
        print("=" * 80)
        print("📊 DETAILED ANALYTICS BREAKDOWN")
        print("=" * 80)
        
        analytics = self.get_latest_analytics()
        
        if not analytics:
            print("❌ No analytics data available.")
            return
        
        # Plan distribution
        if 'students_analytics' in analytics:
            students = analytics['students_analytics']
            print("\n📋 PLAN DISTRIBUTION")
            print("-" * 30)
            for plan, count in students['plan_distribution'].items():
                percentage = (count / students['total_students']) * 100
                print(f"{plan}: {count} ({percentage:.1f}%)")
        
        # Neighborhood distribution
        if 'students_analytics' in analytics:
            print("\n🏘️  NEIGHBORHOOD DISTRIBUTION (Top 10)")
            print("-" * 40)
            neighborhoods = sorted(
                students['neighborhood_distribution'].items(),
                key=lambda x: x[1],
                reverse=True
            )[:10]
            for neighborhood, count in neighborhoods:
                percentage = (count / students['total_students']) * 100
                print(f"{neighborhood}: {count} ({percentage:.1f}%)")
        
        # Hashtag performance
        if 'instagram_analytics' in analytics:
            instagram = analytics['instagram_analytics']
            print("\n🏷️  HASHTAG PERFORMANCE")
            print("-" * 30)
            for hashtag, metrics in instagram['hashtag_performance'].items():
                print(f"#{hashtag}:")
                print(f"  Avg Engagement Rate: {metrics['engagement_rate']:.2%}")
                print(f"  Avg Likes: {metrics['likes']:.0f}")
                print(f"  Avg Comments: {metrics['comments']:.0f}")
                print(f"  Avg Saves: {metrics['saves']:.0f}")
        
        # Optimal posting times
        if 'cross_platform_analytics' in analytics:
            cross_platform = analytics['cross_platform_analytics']
            print("\n⏰ OPTIMAL POSTING TIMES")
            print("-" * 30)
            for day, rate in cross_platform['optimal_posting_times'].items():
                print(f"{day}: {rate:.2%} engagement rate")
    
    def export_report(self, filename: str = None):
        """Export analytics report to JSON file."""
        if not filename:
            filename = f"social_fit_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        analytics = self.get_latest_analytics()
        
        if analytics:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(analytics, f, indent=2, ensure_ascii=False, default=str)
            print(f"✅ Report exported to {filename}")
        else:
            print("❌ No analytics data to export")

def main():
    """Main dashboard function."""
    dashboard = SocialFITDashboard()
    
    print("Welcome to Social FIT Analytics Dashboard!")
    print("Choose an option:")
    print("1. Summary Dashboard")
    print("2. Detailed Analytics")
    print("3. Export Report")
    print("4. Exit")
    
    while True:
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                dashboard.display_summary()
            elif choice == "2":
                dashboard.display_detailed_analytics()
            elif choice == "3":
                filename = input("Enter filename (or press Enter for default): ").strip()
                dashboard.export_report(filename if filename else None)
            elif choice == "4":
                print("👋 Goodbye!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-4.")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main() 