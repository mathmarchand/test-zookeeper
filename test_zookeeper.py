from kazoo.client import KazooClient
import argparse
import logging

logger = logging.getLogger(__name__)

def main():
    logging.basicConfig(level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('--host')
    args = parser.parse_args()
    zk = KazooClient(hosts=args.host)
    logger.info(f"Will connect to {args.host}")
    try:
        zk.start()
        zk.ensure_path("/test/zookeeper")
        logger.info(f"Ensuring the path exist, creating if needed")
        zk.create("/test/zookeeper/node-test", b"a test value")
        logger.info(f"Writing a test value to /test/zookeeper/node-test")
        if zk.exists("/test/zookeeper/node-test"):
            logger.info(f"znode was created")
            data, stat = zk.get("/test/zookeeper/node-test")
            logger.info(f"Version: {stat.version}, data: {data.decode('utf-8')}")
        else:
            logger.error("Test node not found")
            exit(1)
        logger.info("Test successful!")
    except Exception as ee:
        logger.error(f"{ee}")
    finally:
        logger.info("Cleaning up")
        zk.delete("/test", recursive=True)
        zk.stop()
        zk.close()


if __name__ == "__main__":
    main()
