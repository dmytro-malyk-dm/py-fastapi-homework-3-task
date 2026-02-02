from pydantic import BaseModel, EmailStr, Field, field_validator

from database.validators import accounts as accounts_validators


class UserRegistrationRequestSchema(BaseModel):
    """
    Schema for user registration request.
    """

    email: EmailStr
    password: str

    @field_validator("password")
    @classmethod
    def validate_password_strength(cls, v: str) -> str:
        """
        Validate password strength using existing validator.
        """
        return accounts_validators.validate_password_strength(v)


class UserActivationRequestSchema(BaseModel):
    """
    Schema for account activation request.
    """

    activation_token: str = Field(min_length=1)


class PasswordResetRequestSchema(BaseModel):
    """
    Schema for password reset request.
    """
    email: EmailStr


class PasswordResetCompleteRequestSchema(BaseModel):
    """
    Schema for password reset completion.
    """

    reset_token: str = Field(min_length=1)
    new_password: str

    @field_validator("new_password")
    @classmethod
    def validate_new_password_strength(cls, v: str) -> str:
        """Validate new password strength using existing validator."""
        return accounts_validators.validate_password_strength(v)


class UserLoginRequestSchema(BaseModel):
    """
    Schema for user login request.
    """

    email: EmailStr
    password: str = Field(min_length=1)


class TokenRefreshRequestSchema(BaseModel):
    """
    Schema for token refresh request.
    """

    refresh_token: str = Field(min_length=1)


class UserRegistrationResponseSchema(BaseModel):
    """
    Schema for user registration response.
    """

    activation_token: str


class MessageResponseSchema(BaseModel):
    """
    Generic message response schema.
    """

    detail: str


class PasswordResetTokenResponseSchema(BaseModel):
    """
    Schema for password reset token response.
    """

    reset_token: str


class UserLoginResponseSchema(BaseModel):
    """
    Schema for user login response.
    """

    access_token: str
    refresh_token: str
    token_type: str = "bearer"


class TokenRefreshResponseSchema(BaseModel):
    """
    Schema for token refresh response.
    """

    access_token: str
