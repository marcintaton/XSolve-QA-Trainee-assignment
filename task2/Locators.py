from selenium.webdriver.common.by import By


class MainPageLocators (object):
    to_cart_prod1 = (
        By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[3]/button[1]')
    to_cart_prod2 = (
        By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[3]/button[1]')
    to_cart_prod3 = (
        By.XPATH, '//*[@id="content"]/div[2]/div[3]/div/div[3]/button[1]')
    to_cart_prod4 = (
        By.XPATH, '//*[@id="content"]/div[2]/div[4]/div/div[3]/button[1]')
    success_alert = (By.CLASS_NAME, 'alert-success')
    goto_product1_page = (
        By.XPATH, '//*[@id="content"]/div[2]/div[1]/div/div[2]/h4/a')
    goto_product2_page = (
        By.XPATH, '//*[@id="content"]/div[2]/div[2]/div/div[2]/h4/a')
    goto_cart_page = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')


class LoginPageLocators (object):
    e_mail = (By.ID, "input-email")
    password = (By.ID, "input-password")
    login_button = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')


class CheckoutSuccessPageLocators:

    return_to_main_page_btn = (By.XPATH, '//*[@id="content"]/div/div/a')


class CheckoutPageLocators:

    step1_collapse = (By.ID, 'collapse-checkout-option')
    step1_guest_checkout_radio = (
        By.XPATH, '//*[@id="collapse-checkout-option"]/div/div/div[1]/div[2]/label/input')
    step1_continue = (By.ID, 'button-account')

    step2_collapse = (By.ID, 'collapse-payment-address')
    step2_name = (By.ID, 'input-payment-firstname')
    step2_last_name = (By.ID, 'input-payment-lastname')
    step2_email = (By.ID, 'input-payment-email')
    step2_phone = (By.ID, 'input-payment-telephone')
    step2_company = (By.ID, 'input-payment-company')
    step2_adress_1 = (By.ID, 'input-payment-address-1')
    step2_adress_2 = (By.ID, 'input-payment-address-2')
    step2_city = (By.ID, 'input-payment-city')
    step2_post_code = (By.ID, 'input-payment-postcode')
    step2_country = (By.ID, 'input-payment-country')
    step2_state = (By.ID, 'input-payment-zone')
    step2_button_guest = (By.ID, 'button-guest')
    step2_shipping_adr_chechbox = (
        By.XPATH, '//*[@id="collapse-payment-address"]/div/div[2]/label/input')
    step2_continue = (By.ID, 'button-guest')

    step3_collapse = (By.ID, 'collapse-shipping-address')
    step3_name = (By.ID, 'input-shipping-firstname')
    step3_last_name = (By.ID, 'input-shipping-lastname')
    step3_company = (By.ID, 'input-shipping-company')
    step3_adress_1 = (By.ID, 'input-shipping-address-1')
    step3_adress_2 = (By.ID, 'input-shipping-address-2')
    step3_city = (By.ID, 'input-shipping-city')
    step3_post_code = (By.ID, 'input-shipping-postcode')
    step3_country = (By.ID, 'input-shipping-country')
    step3_state = (By.ID, 'input-shipping-zone')
    step3_continue = (By.ID, 'button-guest-shipping')

    step4_collapse = (By.ID, 'collapse-shipping-method')
    step4_comment_area = (
        By.XPATH, '//*[@id="collapse-shipping-method"]/div/p[4]/textarea')
    step4_continue = (By.ID, 'button-shipping-method')

    step5_collapse = (By.ID, 'collapse-payment-method')
    step5_comment_area = (
        By.XPATH, '//*[@id="collapse-payment-method"]/div/p[3]/textarea')
    step5_terms_and_cond_checkbox = (By.NAME, 'agree')
    step5_terms_and_cond_link = (By.CLASS_NAME, 'agree')
    step5_continue = (By.ID, 'button-payment-method')

    step6_collapse = (By.ID, 'collapse-checkout-confirm')
    step6_submit = (By.ID, 'button-confirm')


class CartPageLocators:

    checkout_btn = (By.XPATH, '//*[@id="content"]/div[3]/div[2]/a')


class Product1PageLocators:

    button_cart = (By.ID, 'button-cart')
    quantity_field = (By.NAME, 'quantity')
    goto_cart_page = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')


class Product2PageLocators:

    button_cart = (By.ID, 'button-cart')
    quantity_field = (By.NAME, 'quantity')
    goto_cart_page = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')


class Product3PageLocators:

    button_cart = (By.ID, 'button-cart')
    quantity_field = (By.NAME, 'quantity')
    goto_cart_page = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')


class Product4PageLocators:

    button_cart = (By.ID, 'button-cart')
    quantity_field = (By.NAME, 'quantity')
    goto_cart_page = (By.XPATH, '//*[@id="top-links"]/ul/li[4]/a')
