from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from enum import Enum

class Gender(str, Enum):
    MALE = "M"
    FEMALE = "F"

class PlanType(str, Enum):
    MONTHLY = "Mensal"
    QUARTERLY = "Trimestral"
    ANNUAL = "Anual"

class Student(BaseModel):
    """Student data model for Social FIT."""
    id: int
    name: str = Field(alias="Nome")
    gender: Gender = Field(alias="Gênero")
    birth_date: datetime = Field(alias="Data de Nascimento")
    address: str = Field(alias="Endereço")
    neighborhood: str = Field(alias="Bairro")
    plan_type: PlanType = Field(alias="Tipo_Plano")
    gympass: bool = Field(alias="Gympass")
    monthly_value: float = Field(alias="Valor_Plano_Mensal (R$)")
    total_value: float = Field(alias="Valor_Plano_Total (R$)")
    plan_start_date: datetime = Field(alias="Data Início Plano")
    active_plan: bool = Field(alias="Plano Ativo")
    
    class Config:
        allow_population_by_field_name = True

class InstagramPost(BaseModel):
    """Instagram post data model for Social FIT."""
    date: datetime = Field(alias="Data")
    likes: int = Field(alias="Likes")
    comments: int = Field(alias="Comentários")
    saves: int = Field(alias="Salvamentos")
    reach: int = Field(alias="Alcance")
    profile_visits: int = Field(alias="Visitas ao Perfil")
    new_followers: int = Field(alias="Novos Seguidores")
    main_hashtag: str = Field(alias="Hashtag Principal")
    
    class Config:
        allow_population_by_field_name = True

class StudentAnalytics(BaseModel):
    """Analytics model for student data."""
    total_students: int
    active_students: int
    inactive_students: int
    plan_distribution: dict
    neighborhood_distribution: dict
    gender_distribution: dict
    gympass_users: int
    average_monthly_value: float
    total_monthly_revenue: float

class InstagramAnalytics(BaseModel):
    """Analytics model for Instagram data."""
    total_posts: int
    total_likes: int
    total_comments: int
    total_saves: int
    total_reach: int
    total_profile_visits: int
    total_new_followers: int
    average_engagement_rate: float
    hashtag_performance: dict
    daily_performance: dict

class CrossPlatformAnalytics(BaseModel):
    """Cross-platform analytics model."""
    correlation_score: float
    engagement_to_enrollment_rate: float
    top_performing_content_types: list
    optimal_posting_times: dict
    geographic_insights: dict
    revenue_impact: float 