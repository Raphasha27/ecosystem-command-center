"""Tests for ecosystem_command_center."""
import pytest
from ecosystem_command_center import scan_repos, check_health, generate_report, EcosystemCommandCenter

class TestEcosystemCommandCenter:
    def test_initialization(self):
        center = EcosystemCommandCenter(token="test-token")
        assert center.token == "test-token"

    def test_check_health(self):
        result = check_health({"has_readme": True, "has_license": True})
        assert result["score"] > 0
