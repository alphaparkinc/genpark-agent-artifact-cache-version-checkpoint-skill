from client import AgentArtifactCacheVersionCheckpointClient

def main():
    client = AgentArtifactCacheVersionCheckpointClient()
    res = client.create_checkpoint("q3_agent_orchestration_run")
    print(f"Checkpoint ID: {res['checkpoint_id']}")
    print(f"Cache Latency: {res['cache_hit_latency_ms']}ms")
    print(f"Snapshot Stored: {res['snapshot_stored']}")

if __name__ == "__main__":
    main()
