from dash.testing.application_runners import import_app
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_initial_render(dash_duo):
    """
    Test the initial rendering of the Dash app.
    """
    app = import_app('usage')
    dash_duo.start_server(app)

    open_g_picker = dash_duo.find_element('#open-picker-button')
    assert 'Open Google Picker' == open_g_picker.text

def test_google_popup(dash_duo):
    """
    Test if the google login popup is opened correctly.
    """
    app = import_app('usage')
    dash_duo.start_server(app)

    initial_handles = dash_duo.driver.window_handles
    open_g_picker = dash_duo.find_element('#open-picker-button')

    time.sleep(1) # Wait a second until everything renders
    open_g_picker.click()

    wait = WebDriverWait(dash_duo.driver, 10)  # Wait for a maximum of 10 seconds
    updated_handles = wait.until(EC.number_of_windows_to_be(len(initial_handles) + 1))

    if len(updated_handles) > len(initial_handles):
        new_window_handle = updated_handles[-1] 
        dash_duo.driver.switch_to.window(new_window_handle)
        print("A new window was opened.")
        assert True  
    else:
        print("No new window was opened.")
        assert False 

# Further tests are not easily possible since google forbids automated logins.