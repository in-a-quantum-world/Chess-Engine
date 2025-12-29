#trying api stuff
import aiohttp
import asyncio

async def post_chess_api(data=None):
    url = "https://chess-api.com/v1"
    headers = {"Content-Type": "application/json"}
    
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data, headers=headers) as response:
            return await response.json()

async def main():
    # 1. Execute request with FEN data
    fen_data = {"fen": "8/1P1R4/n1r2B2/3Pp3/1k4P1/6K1/Bppr1P2/2q5 w - - 0 1"}
    fen_response = await post_chess_api(fen_data)
    print(fen_response)
    """
    moves_list_html = "<div class='moves-list'>Some chess moves</div>"  
    input_data = {"input": moves_list_html}
    input_response = await post_chess_api(input_data)
    print(input_response)
    """
x = 3
if x == 3:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())