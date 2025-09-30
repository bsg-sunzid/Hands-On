class InvalidEmailError(Exception):
    """Exception raised when an invalid email address is provided."""
    
    def __init__(self, email, message="Invalid email address"):
        self.email = email
        self.message = message
        super().__init__(f"{self.message}: {self.email}")

def validate_email(email):
    if "@" not in email or "." not in email:
        raise InvalidEmailError(email)
    return True

# Test
try:
    validate_email("abcdgmail.com")
    print("ok")
except InvalidEmailError as e:
    print(f"Caught an error: {e}")
