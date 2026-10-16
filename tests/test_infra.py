import unittest
from pathlib import Path


class InfrastructureTests(unittest.TestCase):

    def test_public_network_access_is_disabled(self):
        content = Path("infra/storage.bicep").read_text()

        self.assertIn(
            "publicNetworkAccess: 'Disabled'",
            content
        )


if __name__ == "__main__":
    unittest.main()
