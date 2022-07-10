import pytest
from .factories import SongFactory

@pytest.fixture
def songs():
    return SongFactory.create_batch(10)