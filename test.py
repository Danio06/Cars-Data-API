from carparser import parse_query

MODELS = ["E21", "E30", "E36", "E46", "E90", "F30", "G20",
          "E87", "F20", "F40", "X3", "X5", "X6"]
SERIES = ["1_series", "2_series", "3_series", "x_series", "m_series"]

def test_exact_model():
    r = parse_query("E90 petrol", MODELS, SERIES)
    assert r["scope"]["type"] == "model"
    assert r["scope"]["value"] == "E90"
    assert r["fuel"] == "petrol"

def test_series_number():
    r = parse_query("series 3 best diesel", MODELS, SERIES)
    assert r["scope"]["type"] == "series"
    assert r["scope"]["value"] == "3_series"
    assert r["intent"] == "best"
    assert r["fuel"] == "diesel"

def test_suv_intent():
    r = parse_query("suv best petrol", MODELS, SERIES)
    assert r["scope"]["type"] == "series"
    assert r["scope"]["value"] == "x_series"

def test_x_family():
    r = parse_query("X best diesel", MODELS, SERIES)
    assert r["scope"]["type"] == "series"
    assert r["scope"]["value"] == "x_series"

def test_no_model():
    r = parse_query("best petrol", MODELS, SERIES)
    assert r["scope"]["type"] == "all"

def test_fuel_hybrid():
    r = parse_query("F40 hybrid", MODELS, SERIES)
    assert r["fuel"] == "hybrid"