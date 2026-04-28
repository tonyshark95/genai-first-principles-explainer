import pytest
from ai_service import FirstPrinciplesAI

# A mock class to simulate the AI response without hitting the real API and costing money
class MockResponse:
    def __init__(self, text):
        self.text = text

def test_ai_service_initialization(monkeypatch):
    # Test that the service fails securely if the API key is missing
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)
    with pytest.raises(ValueError):
        FirstPrinciplesAI()

def test_deconstruct_topic_returns_string(monkeypatch):
    # Inject a fake API key for the test
    monkeypatch.setenv("GEMINI_API_KEY", "fake_key")
    service = FirstPrinciplesAI()
    
    # We mock the actual API call so our test runs instantly and offline
    def mock_generate(*args, **kwargs):
        return MockResponse("This is a mock first-principles breakdown.")
    
    service.model.generate_content = mock_generate
    
    result = service.deconstruct_topic("Gravity", 0.0, "University Level")
    
    # Assertions prove your code behaves as expected
    assert isinstance(result, MockResponse)
    assert "mock" in result.text