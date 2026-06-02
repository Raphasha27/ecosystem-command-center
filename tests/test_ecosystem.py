"""Tests for ecosystem_command_center."""
import pytest
from ecosystem_command_center import scan_repos, check_health, generate_report, EcosystemCommandCenter

class TestEcosystemCommandCenter:
    def test_initialization(self):
        center = EcosystemCommandCenter(token="test-token")
        assert center.token == "test-token"

    def test_scan_repos(self):
        repos = scan_repos("Raphasha27", limit=2)
        assert len(repos) <= 2

    def test_check_health(self):
        result = check_health({"has_readme": True, "has_license": True})
        assert result["score"] > 0

    def test_generate_report(self):
        data = [{"name": "repo1", "health_score": 85}, {"name": "repo2", "health_score": 60}]
        report = generate_report(data)
        assert "repo1" in report
