from dataclasses import dataclass
@dataclass(frozen=True)
class Signals:
 database_replica_lag_s:int; backup_verified:bool; error_budget:float; kubernetes_ready:float; change_approved:bool
def plan(s:Signals)->dict:
 reasons=[]
 if s.database_replica_lag_s>60:reasons.append('replication-lag')
 if not s.backup_verified:reasons.append('backup-unverified')
 if s.kubernetes_ready<.99:reasons.append('workloads-unready')
 if s.error_budget<.2:reasons.append('error-budget-low')
 if reasons:return {'action':'stabilize-and-page','reasons':reasons}
 return {'action':'proceed-approved-change' if s.change_approved else 'await-change-approval','reasons':[]}
