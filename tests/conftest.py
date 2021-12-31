"""Tests configuration."""
import asyncio
import pytest

@pytest.fixture(autouse=True)
def loop_factory():
    return asyncio.new_event_loop
