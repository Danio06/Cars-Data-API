from playwright.sync_api import sync_playwright

BASE_URL = "https://danio06.github.io/CarsFrontEnd/"


def run(query: str):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        page.goto(BASE_URL)

        page.fill("#query", query)

        with page.expect_response(lambda r: "/search" in r.url and r.status in [200, 400], timeout=40000):
            page.click("#submitBtn")

        page.wait_for_selector("#results")

        content = page.locator("#results").inner_text()

        browser.close()
        return content

def test_search_best_fuel():
    content = run("f30 best petrol")

    assert "ENGINES FOUND" in content
    assert "RECOMMENDED ENGINE" in content
    assert "340i" in content or "B58" in content


def test_search_error():
    content = run("unknown query")

    assert "Please select series or model" in content or "ERROR" in content


def test_search_series():
    content = run("7 series")

    assert "7" in content or "SERIES" in content or "ENGINES FOUND" in content


def test_search_family():
    content = run("x6")

    assert "X6" in content or "ENGINES FOUND" in content