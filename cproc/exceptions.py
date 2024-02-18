class GraphNotFoundException(Exception):
    def __init__(self, graph_id: str) -> None:
        self.graph_id = graph_id

    def __str__(self) -> str:
        return f"Graph id not found: {self.graph_id}"

class CodeExecutionException(Exception):
  def __init__(self, message_id: str) -> None:
    self.message_id = message_id

  def __str__(self) -> str:
    return f"Code excecution exception. message_id: {self.message_id}"