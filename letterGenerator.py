import asyncio
from JihadLibrary import JihadLibrary

# Main function
async def main():
    print("____________________________________________")
    payload = JihadLibrary().createPattern(2500)
    print("____________________________________________")
    print(payload)
    print(2500)
    foundAt = JihadLibrary().offsetPattern(payload, 2500)
    print("found at", foundAt)

# Calling the main function
asyncio.run(main())