"""This module contains XPath and CSS locators."""


class Locators:
    # XPath locators
    @staticmethod
    def get_xpath():
        return {
            "login_button": "//button[text()='Login']",
            "username_input": "//input[@id='user-name']",
            "password_input": "//input[@type='password']",
            "login_form_submit": "//form[@id='login-form']//button[@type='submit']",
            "register_link": "//a[@href='/register']",
            "error_message": "//div[@class='alert alert-danger']",
            "home_link": "//nav[@class='navbar']//a[text()='Home']",
            "welcome_header": "//h1[contains(text(), 'Welcome')]",
            "email_placeholder": "//input[@placeholder='Email']",
            "terms_footer_link": "//footer//a[text()='Terms']",
            "remember_me_checkbox": "//input[@type='checkbox' and @id='remember-me']",
            "second_row_third_column": "//table[@class='table']//tr[2]//td[3]",
            "profile_menu_link": "//ul[@class='dropdown-menu']//a[@href='/profile']",
            "danger_button": "//button[contains(@class, 'btn-danger')]",
            "user_label": "//form[@id='login-form']//label[@for='user-name']",
            "main_container_h2": "//div[@id='main-container']//h2",
            "search_input": "//input[@aria-label='Search']",
            "close_dialog_button": "//div[@role='dialog']//button[text()='Close']",
            "contact_link": "//ul[@class='navbar-nav']//li/a[text()='Contact']",
            "search_text_input": "//form[@name='search']//input[@type='text']",
            "trash_icon": "//span[@data-icon='trash']",
            "navbar_brand_logo": "//header//a[@class='navbar-brand']",
            "disabled_save_button": "//button[@id='save-changes'][@disabled]",
            "no_results_message": "//p[contains(text(), 'No results found')]",
            "pagination_next_button": "//div[@class='pagination']//a[@aria-label='Next']",
        }

    # CSS locators
    @staticmethod
    def get_css():
        return {
            "login_button": "button:contains('Login')",
            "username_input": "input#user-name",
            "password_input": "input[type='password']",
            "login_form_submit": "form#login-form button[type='submit']",
            "register_link": "a[href='/register']",
            "error_message": "div.alert.alert-danger",
            "home_link": "nav.navbar a:contains('Home')",
            "welcome_header": "h1:contains('Welcome')",
            "email_placeholder": "input[placeholder='Email']",
            "terms_footer_link": "footer a:contains('Terms')",
            "remember_me_checkbox": "input[type='checkbox']#remember-me",
            "second_row_third_column": "table.table tr:nth-child(2) td:nth-child(3)",
            "profile_menu_link": "ul.dropdown-menu a[href='/profile']",
            "danger_button": "button.btn-danger",
            "user_label": "form#login-form label[for='user-name']",
            "main_container_h2": "div#main-container h2",
            "search_input": "input[aria-label='Search']",
            "close_dialog_button": "div[role='dialog'] button:contains('Close')",
            "contact_link": "ul.navbar-nav li a:contains('Contact')",
            "search_text_input": "form[name='search'] input[type='text']",
            "trash_icon": "span[data-icon='trash']",
            "navbar_brand_logo": "header a.navbar-brand",
            "disabled_save_button": "button#save-changes:disabled",
            "no_results_message": "p:contains('No results found')",
            "pagination_next_button": "div.pagination a[aria-label='Next']",
        }


if __name__ == "__main__":
    # Get locators
    xpath_locators = Locators.get_xpath()
    css_locators = Locators.get_css()

    # Using locator
    login_button_xpath = xpath_locators["login_button"]
    login_button_css = css_locators["login_button"]

    # Displaying locators
    print('XPath locator of the login button:')
    print(login_button_xpath)

    print('\nCSS locator of the login button:')
    print(login_button_css)
