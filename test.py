import asyncio
from JihadLibrary import JihadLibrary

# Main function
async def main():
    print("____________________________________________")
    payload = JihadLibrary().createPattern(2012)
    payload = JihadLibrary().addReverseShell(payload)
    print("____________________________________________")
    print(payload)
    print(2012)
    foundAt = JihadLibrary().offsetPattern(payload, 2012)
    print("found at", foundAt)

# Calling the main function
asyncio.run(main())