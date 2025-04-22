"""
Configuration management for MySQL MCP Server
"""
from pydantic import BaseModel, Field

class MySQLConfig(BaseModel):
    """MySQL connection configuration"""
    host: str = Field(default="localhost", description="MySQL server host")
    port: int = Field(default=3306, description="MySQL server port")
    user: str = Field(..., description="MySQL user name")
    password: str = Field(..., description="MySQL user password")
    database: str = Field(default="", description="Default database name")
    charset: str = Field(default="utf8mb4", description="Connection charset")
    
    class Config:
        """Pydantic model configuration"""
        frozen = True  # Make config immutable