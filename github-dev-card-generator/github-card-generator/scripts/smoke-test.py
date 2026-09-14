import asyncio
import os
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
sys.path.insert(0, str(BACKEND))


async def main():
    os.environ.pop("GOOGLE_API_KEY", None)

    from main import health
    from mcp_server import analyze_profile, generate_card_html

    health_response = await health()
    assert health_response == {"status": "healthy"}

    github_data = {
        "name": "Sample Developer",
        "avatar_url": "https://example.com/avatar.png",
        "bio": "Builds developer tools.",
        "location": "Arizona",
        "public_repos": 3,
        "followers": 7,
        "top_repos": [
            {
                "name": "sample-repo",
                "stars": 5,
                "language": "Python",
                "description": "Example repo",
            }
        ],
        "most_used_languages": ["Python", "JavaScript"],
    }

    analysis = await analyze_profile(github_data)
    assert analysis["card_theme"] == "builder"
    assert analysis["top_skills"]

    html = await generate_card_html("sample-dev", github_data, analysis)
    assert "Sample Developer" in html
    assert "sample-repo" in html

    print("smoke test passed")


if __name__ == "__main__":
    asyncio.run(main())

