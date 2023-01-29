import unittest


from booking.data_management.manage_form_data import add_contact_form_to_database


class TestSendingForm(unittest.TestCase):
    def test_valid_data_correct(self):
        """
        Test that Valid form is validated correctly
        """
        validation = add_contact_form_to_database("Witam, czy kino jest otwarte?", "kowalski112@wp.pl")
        self.assertTrue(validation)

    def test_invalid_email_returns(self):
        """
        Test that form with invalid email is validated correctly
        """
        validation = add_contact_form_to_database("Witam, czy kino jest otwarte?", "Kolejowa 14a")
        self.assertFalse(validation)

    def test_too_short_message_returns(self):
        """
        Test that form with invalid message is validated correctly
        """
        validation = add_contact_form_to_database("?", "kowalski112@wp.pl")
        self.assertFalse(validation)
    
    def test_null_question_returns(self):
        """
        Test that form with null data is validated correctly
        """
        validation = add_contact_form_to_database(None, "kowalski112@wp.pl")
        self.assertFalse(validation)

    def test_null_email_returns(self):
        """
        Test that form with null data is validated correctly
        """
        validation = add_contact_form_to_database("Witam", None)
        self.assertFalse(validation)

if __name__ == "__main__":
    unittest.main()
