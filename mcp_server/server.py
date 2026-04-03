from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo-mcp-server")

@mcp.tool()
def calcular_media(numeros: list[float]) -> float:
    """
    Calcula a média aritmética de uma lista de números.
    """
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

if __name__ == "__main__":
    mcp.run(transport="stdio")