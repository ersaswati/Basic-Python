"""
File: item_amount_multiprocessing.py
Purpose:
    Update item_amount for 3-10 lakh rows using multiprocessing
    with a class-based design,specifically for windows user
Author: Saswati Barik
Level: Advanced Python (AI / Data Engineer)

Documention is to understand each part with the demo data as base_amount
= [11,22,33,44,55,66,77,88,99,100]
"""
import pandas as pd
import multiprocessing
import os
import time


class ItemAmountProcessor:
    """
    Processes item amounts using multiprocessing.

    Logic:
        new_amount = base_amount[i] + (i + 1)
    """

    def __init__(self, total_rows, base_amount):
        self.total_rows = total_rows
        self.base_amount = base_amount

    @staticmethod
    def process_chunk(start_index, chunk):
        '''
        Main task should be inside process_chunk
        Task 1
        :param start_index: 0
        :param chunk: [11,22,33]
        | offset | value | calculation      | result |
        | ------ | ----- | ---------------- | ------ |
        | 0      | 11    | 11 + (0 + 0 + 1) | 12     |
        | 1      | 22    | 22 + (0 + 1 + 1) | 24     |
        | 2      | 33    | 33 + (0 + 2 + 1) | 36     |

        Task 2
        start_index = 3
        chunk = [44,55,66]
        | offset | value | calculation      | result |
        | ------ | ----- | ---------------- | ------ |
        | 0      | 44    | 44 + (3 + 0 + 1) | 48     |
        | 1      | 55    | 55 + (3 + 1 + 1) | 59     |
        | 2      | 66    | 66 + (3 + 2 + 1) | 72     |

        Task 3 (Last Chunk)
        start_index = 6
        chunk = [77,88,99,100]
        | offset | value | calculation       | result |
        | ------ | ----- | ----------------- | ------ |
        | 0      | 77    | 77 + (6 + 0 + 1)  | 84     |
        | 1      | 88    | 88 + (6 + 1 + 1)  | 96     |
        | 2      | 99    | 99 + (6 + 2 + 1)  | 108    |
        | 3      | 100   | 100 + (6 + 3 + 1) | 110    |

        '''
        pid = os.getpid()
        print(f"⚙️ PID {pid} | Processing rows {start_index} → {start_index + len(chunk)}")
        updated = []
        for offset, value in enumerate(chunk):
            # actual row index = start_index + offset
            updated.append(value + (start_index + offset + 1))  
        return updated

    def run(self):
        cpu_cores = os.cpu_count()
        process_count = max(1, cpu_cores - 2)
        print("🧠 CPU Cores:", cpu_cores)
        print("⚙️ Processes Used:", process_count)
        #-----------------------CHUNK SIZE CREATION-----------------------------------
        chunk_size = self.total_rows // process_count  # integer division
        '''
        suppose total row = 10, process_count = 3 then chunk_size = 10 // 3 = 3
        Chunk ranges (index-based)
            Process	Start	End	Indices	Values
            P1	0	3	0,1,2	[11,22,33]
            P2	3	6	3,4,5	[44,55,66]
            P3	6	10	6,7,8,9	[77,88,99,100]

            chunk_size = total_rows // process_count 10 // 3 = 3
            last_chunk = remainder
            remainder = total_rows % process_count = 10 % 3 = 1
        '''
        #-----------------------------------------------------------------------------
        tasks = []

        for i in range(process_count):
            start = i * chunk_size
            end = start + chunk_size if i < process_count - 1 else self.total_rows
            # 🔥 Only pass slice, not full list
            chunk = self.base_amount[start:end]
            tasks.append((start, chunk))

        '''
        tasks now stores like:
        [
            (0,   [11,22,33]),
            (3,   [44,55,66]),
            (6,   [77,88,99,100])
        ]

        Memory usage:
        ✅ Each process gets ONLY its chunk
        ❌ No full base_amount duplication
        '''
        start_time = time.time()

        with multiprocessing.Pool(processes=process_count) as pool:
            results = pool.starmap(ItemAmountProcessor.process_chunk,tasks)

        '''
        What pool.starmap Collects
        results = [
            [12, 24, 36],
            [48, 59, 72],
            [84, 96, 108, 110]
        ]
        '''

        final_values = [v for sublist in results for v in sublist]
        print("⏱️ Time Taken:", round(time.time() - start_time, 2), "seconds")
        print("✅ First 5:", final_values[:5])
        print("✅ Last 5:", final_values[-5:])
        return final_values


# --------------------------------------------------
# Main Execution
# --------------------------------------------------
if __name__ == "__main__":
    #==========> time taking process <=============
    input_file="./data/test_data.xlsx"
    output_file="./data/output_data.xlsx"
    base_column="Sum of Item Net Value"
    df = pd.read_excel(input_file)
    item_amount_real = df[base_column].tolist()
    #=============================================

    print("====> multiprocess starting...")
    processor = ItemAmountProcessor(
        total_rows=len(item_amount_real),  # 3 lakh
        base_amount=item_amount_real
    )
    result = processor.run()
    print("====> multiprocess ended...")

    #==========> time taking process <============
    # df["modified_amount"] = result
    # df.to_excel(output_file, index=False)
    #=============================================


'''
OUTPUT

🧠 CPU Cores: 8
⚙️ Processes Used: 6
⚙️ PID 18420 | Rows 0 → 65619
⚙️ PID 19320 | Rows 65619 → 131238
⚙️ PID 23820 | Rows 131238 → 196857
⚙️ PID 21644 | Rows 196857 → 262476
⚙️ PID 7840 | Rows 262476 → 328095
⚙️ PID 7536 | Rows 328095 → 393717
⏱️ Time Taken: 4.26 seconds
✅ First 5: [15.99, 7.82, 42.74, 33.989999999999995, 46.66]
✅ Last 5: [393725.48, 393788.88, 393739.96, 393728.48, 393729.48]

'''
