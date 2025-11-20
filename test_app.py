
import pytest
from app import app

# 1. Test if header is present
def test_header_is_present(dash_duo):
    dash_duo.start_server(app)
    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales Visualiser" in header.text

# 2. Test if graph is present
def test_graph_is_present(dash_duo):
    dash_duo.start_server(app)
    graph = dash_duo.find_element("#sales-graph")  # matches id in your app
    assert graph is not None

# 3. Test if region picker is present
def test_region_picker_is_present(dash_duo):
    dash_duo.start_server(app)
    radios = dash_duo.find_elements("input[type='radio']")
    assert len(radios) == 5  # All, North, East, South, West
