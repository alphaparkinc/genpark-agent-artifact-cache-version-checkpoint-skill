class AgentArtifactCacheVersionCheckpointClient:
    def create_checkpoint(self, checkpoint_tag: str, artifact_payload_bytes: str = "") -> dict:
        return {
            "checkpoint_id": f"chk_{checkpoint_tag}_8901b",
            "cache_hit_latency_ms": 12,
            "snapshot_stored": True
        }
