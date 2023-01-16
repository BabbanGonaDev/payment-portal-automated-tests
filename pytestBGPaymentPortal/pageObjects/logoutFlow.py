from pytestBGPaymentPortal.pageObjects.LoginPage import BGPaymentLogin
from pytestBGPaymentPortal.pageObjects.TGHarvestPage import TGHarvest
from pytestBGPaymentPortal.pageObjects.logoutPage import BGLogout
from pytestBGPaymentPortal.utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        # login to the portal
        login_page = BGPaymentLogin(self.driver)
        login_page.set_username("akinola.oladapo")
        login_page.set_password("password")
        login_page.click_login()

        # assert we are logged in
        login_page.set_displayed()

        # navigation to the TG harvest payment page.
        harvest_page = TGHarvest(self.driver)
        harvest_page.harvest_page()
        harvest_page.harvest_page_next()

        # this is a wait to ensure the TG harvest page finishes loading
        harvest_page.wait_for_element()

        # logout
        # wait for the page to reload
        logout_page = BGLogout(self.driver)
        logout_page.set_logout()

        # assert we are logged out
        logout_page.logout_assertion()




