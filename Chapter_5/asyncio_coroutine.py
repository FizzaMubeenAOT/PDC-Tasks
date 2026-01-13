import asyncio
from random import randint


def multiply_matrices():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    result = [[0, 0], [0, 0]]
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += A[i][k] * B[k][j]
    return result

async def start_state():
    print('Start State called\n')
    input_value = randint(0, 1)
    await asyncio.sleep(1) # Using asyncio.sleep instead of time.sleep for async

    if input_value == 0:
        result = await state2(input_value)
    else:
        result = await state1(input_value)

    print('Resume of the Transition : \nStart State calling ' + result)

async def state1(transition_value):
    output_value = 'State 1 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await state3(input_value)
    else:
        result = await state2(input_value)

    return output_value + 'State 1 calling %s' % result

async def state2(transition_value):
    output_value = 'State 2 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await state3(input_value)

    return output_value + 'State 2 calling %s' % result

async def state3(transition_value):
    output_value = 'State 3 with transition value = %s\n' % transition_value
    input_value = randint(0, 1)
    await asyncio.sleep(1)

    print('...evaluating...')
    if input_value == 0:
        result = await state1(input_value)
    else:
        result = await end_state(input_value)

    return output_value + 'State 3 calling %s' % result

async def end_state(transition_value):
    output_value = 'End State with transition value = %s\n' % transition_value
    print('...stop computation...')
    
    # Perform matrix multiplication at the end of the state machine
    matrix_res = multiply_matrices()
    print("Final Matrix Result: %s" % matrix_res)
    
    return output_value

if __name__ == '__main__':
    print('Finite State Machine simulation with Asyncio Coroutine')
    asyncio.run(start_state())