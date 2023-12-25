from whisper_live.server import TranscriptionServer
import logging

if __name__ == "__main__":
    logging.info("Starting server...")
    server = TranscriptionServer()
    server.run("0.0.0.0")
    logging.info("Server started.")
