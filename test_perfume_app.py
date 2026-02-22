from perfume_app import recommend, weather_from_temperature


def test_weather_mapping():
    assert weather_from_temperature(35) == "hot"
    assert weather_from_temperature(5) == "cold"
    assert weather_from_temperature(20) == "mild"
    assert weather_from_temperature(20, rainy=True) == "rainy"


def test_recommend_for_male_hot():
    picks = recommend("male", 33)
    assert len(picks) == 2
    assert "citrus" in picks[0].notes


def test_recommend_for_female_rainy():
    picks = recommend("female", 22, rainy=True)
    assert len(picks) == 2
