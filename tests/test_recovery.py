import unittest
from src.recovery import Signals,plan
class T(unittest.TestCase):
 def s(self,**k):
  d=dict(database_replica_lag_s=2,backup_verified=True,error_budget=.8,kubernetes_ready=1,change_approved=True);d.update(k);return Signals(**d)
 def test_change(self):self.assertEqual(plan(self.s())['action'],'proceed-approved-change')
 def test_backup(self):self.assertIn('backup-unverified',plan(self.s(backup_verified=False))['reasons'])
 def test_lag(self):self.assertEqual(plan(self.s(database_replica_lag_s=61))['action'],'stabilize-and-page')
