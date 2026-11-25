# Ansyclo in python
import asyncio
import time

async def kaam(name: str, delay: int):
    print(f"Start: {name}")
    await asyncio.sleep(delay)
    print(f"Done: {name}")
    return f"{name} ok "


async def main():
    t0 = time.perf_counter()
    res = await asyncio.gather(
        kaam("A" , 2), kaam("B" , 2), kaam("C" , 2)
    )
    print("Result:" , res)
    print(f"Time: {time.perf_counter() - t0:.2f}s")


    if __name__ == "__main__":
        asyncio.run(main())
        