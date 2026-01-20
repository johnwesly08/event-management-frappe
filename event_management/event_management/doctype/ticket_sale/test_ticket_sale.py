# Copyright (c) 2026, John Wesly and Contributors
# See license.txt

# import frappe
from frappe.tests import IntegrationTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]



class IntegrationTestTicketSale(IntegrationTestCase):
	"""
	Integration tests for TicketSale.
	Use this class for testing interactions between multiple components.
	"""

	pass
