
class SeleniumLibrary:
    def __init__(self, timeout = 0:00:05, implicit_wait = 0:00:00, run_on_failure = 'Capture Page Screenshot', screenshot_root_directory: Optional[str] = None, plugins: Optional[str] = None, event_firing_webdriver: Optional[str] = None): ...
    def add_cookie(self, name: str, value: str, path: Optional[str] = None, domain: Optional[str] = None, secure: Optional[bool] = None, expiry: Optional[str] = None): ...
    def add_location_strategy(self, strategy_name: str, strategy_keyword: str, persist: bool = False): ...
    def alert_should_be_present(self, text: str = '', action: str = 'ACCEPT', timeout: Optional[timedelta] = None): ...
    def alert_should_not_be_present(self, action: str = 'ACCEPT', timeout: Optional[timedelta] = None): ...
    def assign_id_to_element(self, locator: str, id: str): ...
    def capture_element_screenshot(self, locator: str, filename: str = 'selenium-element-screenshot-{index}.png'): ...
    def capture_page_screenshot(self, filename: str = 'selenium-screenshot-{index}.png'): ...
    def checkbox_should_be_selected(self, locator: str): ...
    def checkbox_should_not_be_selected(self, locator: str): ...
    def choose_file(self, locator: str, file_path: str): ...
    def clear_element_text(self, locator: str): ...
    def click_button(self, locator: str, modifier: Union[str, bool] = False): ...
    def click_element(self, locator: str, modifier: Union[str, bool] = False, action_chain: bool = False): ...
    def click_element_at_coordinates(self, locator, xoffset, yoffset): ...
    def click_image(self, locator: str, modifier: Union[str, bool] = False): ...
    def click_link(self, locator: str, modifier: Union[str, bool] = False): ...
    def close_all_browsers(self): ...
    def close_browser(self): ...
    def close_window(self): ...
    def cover_element(self, locator: str): ...
    def create_webdriver(self, driver_name: str, alias: Optional[str] = None, kwargs = {}, **init_kwargs): ...
    def current_frame_should_contain(self, text: str, loglevel: str = 'TRACE'): ...
    def current_frame_should_not_contain(self, text: str, loglevel: str = 'TRACE'): ...
    def delete_all_cookies(self): ...
    def delete_cookie(self, name): ...
    def double_click_element(self, locator: str): ...
    def drag_and_drop(self, locator: str, target: str): ...
    def drag_and_drop_by_offset(self, locator: str, xoffset: int, yoffset: int): ...
    def element_attribute_value_should_be(self, locator: str, attribute: str, expected: str, message: Optional[str] = None): ...
    def element_should_be_disabled(self, locator: str): ...
    def element_should_be_enabled(self, locator: str): ...
    def element_should_be_focused(self, locator: str): ...
    def element_should_be_visible(self, locator: str, message: Optional[str] = None): ...
    def element_should_contain(self, locator: str, expected: str, message: Optional[str] = None, ignore_case: bool = False): ...
    def element_should_not_be_visible(self, locator: str, message: Optional[str] = None): ...
    def element_should_not_contain(self, locator: str, expected: str, message: Optional[str] = None, ignore_case: bool = False): ...
    def element_text_should_be(self, locator: str, expected: str, message: Optional[str] = None, ignore_case: bool = False): ...
    def element_text_should_not_be(self, locator: str, not_expected: str, message: Optional[str] = None, ignore_case: bool = False): ...
    def execute_async_javascript(self, *code: str): ...
    def execute_javascript(self, *code: str): ...
    def frame_should_contain(self, locator: str, text: str, loglevel: str = 'TRACE'): ...
    def get_all_links(self): ...
    def get_browser_aliases(self): ...
    def get_browser_ids(self): ...
    def get_cookie(self, name: str): ...
    def get_cookies(self, as_dict: bool = False): ...
    def get_element_attribute(self, locator: str, attribute: str): ...
    def get_element_count(self, locator: str): ...
    def get_element_size(self, locator: str): ...
    def get_horizontal_position(self, locator: str): ...
    def get_list_items(self, locator: str, values: bool = False): ...
    def get_location(self): ...
    def get_locations(self, browser: str = 'CURRENT'): ...
    def get_selected_list_label(self, locator: str): ...
    def get_selected_list_labels(self, locator: str): ...
    def get_selected_list_value(self, locator: str): ...
    def get_selected_list_values(self, locator: str): ...
    def get_selenium_implicit_wait(self): ...
    def get_selenium_speed(self): ...
    def get_selenium_timeout(self): ...
    def get_session_id(self): ...
    def get_source(self): ...
    def get_table_cell(self, locator: str, row: int, column: int, loglevel: str = 'TRACE'): ...
    def get_text(self, locator: str): ...
    def get_title(self): ...
    def get_value(self, locator: str): ...
    def get_vertical_position(self, locator: str): ...
    def get_webelement(self, locator: str): ...
    def get_webelements(self, locator: str): ...
    def get_window_handles(self, browser: str = 'CURRENT'): ...
    def get_window_identifiers(self, browser: str = 'CURRENT'): ...
    def get_window_names(self, browser: str = 'CURRENT'): ...
    def get_window_position(self): ...
    def get_window_size(self, inner: bool = False): ...
    def get_window_titles(self, browser: str = 'CURRENT'): ...
    def go_back(self): ...
    def go_to(self, url): ...
    def handle_alert(self, action: str = 'ACCEPT', timeout: Optional[timedelta] = None): ...
    def input_password(self, locator: str, password: str, clear: bool = True): ...
    def input_text(self, locator: str, text: str, clear: bool = True): ...
    def input_text_into_alert(self, text: str, action: str = 'ACCEPT', timeout: Optional[timedelta] = None): ...
    def list_selection_should_be(self, locator: str, *expected: str): ...
    def list_should_have_no_selections(self, locator: str): ...
    def location_should_be(self, url: str, message: Optional[str] = None): ...
    def location_should_contain(self, expected: str, message: Optional[str] = None): ...
    def log_location(self): ...
    def log_source(self, loglevel: str = 'INFO'): ...
    def log_title(self): ...
    def maximize_browser_window(self): ...
    def mouse_down(self, locator: str): ...
    def mouse_down_on_image(self, locator: str): ...
    def mouse_down_on_link(self, locator: str): ...
    def mouse_out(self, locator: str): ...
    def mouse_over(self, locator: str): ...
    def mouse_up(self, locator: str): ...
    def open_browser(self, url: Optional[str] = None, browser: str = 'firefox', alias: Optional[str] = None, remote_url: Union[str, bool] = False, desired_capabilities: Optional[Union[str, dict, None]] = None, ff_profile_dir: Optional[str] = None, options: Optional[Any] = None, service_log_path: Optional[str] = None, executable_path: Optional[str] = None): ...
    def open_context_menu(self, locator: str): ...
    def page_should_contain(self, text: str, loglevel: str = 'TRACE'): ...
    def page_should_contain_button(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_contain_checkbox(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_contain_element(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE', limit: Optional[int] = None): ...
    def page_should_contain_image(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_contain_link(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_contain_list(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_contain_radio_button(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_contain_textfield(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_not_contain(self, text: str, loglevel: str = 'TRACE'): ...
    def page_should_not_contain_button(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_not_contain_checkbox(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_not_contain_element(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_not_contain_image(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_not_contain_link(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_not_contain_list(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_not_contain_radio_button(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def page_should_not_contain_textfield(self, locator: str, message: Optional[str] = None, loglevel: str = 'TRACE'): ...
    def press_key(self, locator: str, key: str): ...
    def press_keys(self, locator: Optional[str] = None, *keys: str): ...
    def radio_button_should_be_set_to(self, group_name: str, value: str): ...
    def radio_button_should_not_be_selected(self, group_name: str): ...
    def register_keyword_to_run_on_failure(self, keyword: str): ...
    def reload_page(self): ...
    def remove_location_strategy(self, strategy_name: str): ...
    def scroll_element_into_view(self, locator: str): ...
    def select_all_from_list(self, locator: str): ...
    def select_checkbox(self, locator: str): ...
    def select_frame(self, locator: str): ...
    def select_from_list_by_index(self, locator: str, *indexes: str): ...
    def select_from_list_by_label(self, locator: str, *labels: str): ...
    def select_from_list_by_value(self, locator: str, *values: str): ...
    def select_radio_button(self, group_name: str, value: str): ...
    def set_browser_implicit_wait(self, value: timedelta): ...
    def set_focus_to_element(self, locator: str): ...
    def set_screenshot_directory(self, path: str): ...
    def set_selenium_implicit_wait(self, value: timedelta): ...
    def set_selenium_speed(self, value: timedelta): ...
    def set_selenium_timeout(self, value: timedelta): ...
    def set_window_position(self, x: int, y: int): ...
    def set_window_size(self, width: int, height: int, inner: bool = False): ...
    def simulate_event(self, locator: str, event: str): ...
    def submit_form(self, locator: Optional[str] = None): ...
    def switch_browser(self, index_or_alias: str): ...
    def switch_window(self, locator: str = 'MAIN', timeout: Optional[str] = None, browser: str = 'CURRENT'): ...
    def table_cell_should_contain(self, locator: str, row: int, column: int, expected: str, loglevel: str = 'TRACE'): ...
    def table_column_should_contain(self, locator: str, column: int, expected: str, loglevel: str = 'TRACE'): ...
    def table_footer_should_contain(self, locator: str, expected: str, loglevel: str = 'TRACE'): ...
    def table_header_should_contain(self, locator: str, expected: str, loglevel: str = 'TRACE'): ...
    def table_row_should_contain(self, locator: str, row: int, expected: str, loglevel: str = 'TRACE'): ...
    def table_should_contain(self, locator: str, expected: str, loglevel: str = 'TRACE'): ...
    def textarea_should_contain(self, locator: str, expected: str, message: Optional[str] = None): ...
    def textarea_value_should_be(self, locator: str, expected: str, message: Optional[str] = None): ...
    def textfield_should_contain(self, locator: str, expected: str, message: Optional[str] = None): ...
    def textfield_value_should_be(self, locator: str, expected: str, message: Optional[str] = None): ...
    def title_should_be(self, title: str, message: Optional[str] = None): ...
    def unselect_all_from_list(self, locator: str): ...
    def unselect_checkbox(self, locator: str): ...
    def unselect_frame(self): ...
    def unselect_from_list_by_index(self, locator: str, *indexes: str): ...
    def unselect_from_list_by_label(self, locator: str, *labels: str): ...
    def unselect_from_list_by_value(self, locator: str, *values: str): ...
    def wait_for_condition(self, condition: str, timeout: Optional[timedelta] = None, error: Optional[str] = None): ...
    def wait_until_element_contains(self, locator: str, text: str, timeout: Optional[timedelta] = None, error: Optional[str] = None): ...
    def wait_until_element_does_not_contain(self, locator: str, text: str, timeout: Optional[timedelta] = None, error: Optional[str] = None): ...
    def wait_until_element_is_enabled(self, locator: str, timeout: Optional[timedelta] = None, error: Optional[str] = None): ...
    def wait_until_element_is_not_visible(self, locator: str, timeout: Optional[timedelta] = None, error: Optional[str] = None): ...
    def wait_until_element_is_visible(self, locator: str, timeout: Optional[timedelta] = None, error: Optional[str] = None): ...
    def wait_until_location_contains(self, expected: str, timeout: Optional[timedelta] = None, message: Optional[str] = None): ...
    def wait_until_location_does_not_contain(self, location: str, timeout: Optional[timedelta] = None, message: Optional[str] = None): ...
    def wait_until_location_is(self, expected: str, timeout: Optional[timedelta] = None, message: Optional[str] = None): ...
    def wait_until_location_is_not(self, location: str, timeout: Optional[timedelta] = None, message: Optional[str] = None): ...
    def wait_until_page_contains(self, text: str, timeout: Optional[timedelta] = None, error: Optional[str] = None): ...
    def wait_until_page_contains_element(self, locator: str, timeout: Optional[timedelta] = None, error: Optional[str] = None, limit: Optional[int] = None): ...
    def wait_until_page_does_not_contain(self, text: str, timeout: Optional[timedelta] = None, error: Optional[str] = None): ...
    def wait_until_page_does_not_contain_element(self, locator: str, timeout: Optional[timedelta] = None, error: Optional[str] = None, limit: Optional[int] = None): ...
    # methods from PythonLibCore
    def add_library_components(self, library_components): ...
    def get_keyword_names(self): ...
    def run_keyword(self, name, args, kwargs=None): ...
    def get_keyword_arguments(self, name): ...
    def get_keyword_tags(self, name): ...
    def get_keyword_documentation(self, name): ...
    def get_keyword_types(self, name): ...
    def get_keyword_source(self, keyword_name): ...
