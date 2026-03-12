import os
import sys

_scenario_dir = os.path.join(os.path.dirname(__file__), "..")
for _key in list(sys.modules.keys()):
    if _key == "lib" or _key.startswith("lib."):
        del sys.modules[_key]
if _scenario_dir not in sys.path:
    sys.path.insert(0, _scenario_dir)

from lib.ledger import Ledger


def _make_ledger():
    ledger = Ledger()
    ledger.create_account("checking", opening_balance=1000)
    ledger.create_account("savings", opening_balance=500)
    ledger.create_account("vendor", opening_balance=0)
    return ledger


# ---------- transfer ----------

def test_transfer_updates_balances():
    ledger = _make_ledger()
    ledger.transfer("checking", "vendor", 200)
    assert ledger.get_balance("checking") == 800
    assert ledger.get_balance("vendor") == 200


def test_transfer_multiple():
    ledger = _make_ledger()
    ledger.transfer("checking", "vendor", 100)
    ledger.transfer("savings", "vendor", 50)
    assert ledger.get_balance("checking") == 900
    assert ledger.get_balance("savings") == 450
    assert ledger.get_balance("vendor") == 150


def test_transfer_records_transaction():
    ledger = _make_ledger()
    ledger.transfer("checking", "vendor", 300)
    assert len(ledger.transactions) == 1
    assert ledger.transactions[0]["amount"] == 300


# ---------- net_balance ----------

def test_net_balance_unchanged_after_transfers():
    """Transfers move money — the net sum of all accounts should stay constant."""
    ledger = _make_ledger()
    original_net = ledger.net_balance()
    ledger.transfer("checking", "vendor", 200)
    ledger.transfer("savings", "checking", 100)
    assert ledger.net_balance() == original_net


# ---------- total_transferred ----------

def test_total_transferred():
    ledger = _make_ledger()
    ledger.transfer("checking", "vendor", 200)
    ledger.transfer("savings", "vendor", 300)
    assert ledger.total_transferred() == 500


# ---------- edge cases ----------

def test_transfer_rejects_zero():
    ledger = _make_ledger()
    try:
        ledger.transfer("checking", "vendor", 0)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass


def test_transfer_rejects_negative():
    ledger = _make_ledger()
    try:
        ledger.transfer("checking", "vendor", -50)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
