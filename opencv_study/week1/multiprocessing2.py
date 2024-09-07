from multiprocessing import Pool
import pandas as pd

def process_file(file_name):
    # 대용량 파일 처리 로직
    data = pd.read_csv(file_name)
    # 복잡한 데이터 처리 작업 수행
    processed_data = data
    return processed_data

if __name__ == '__main__':
    files = ['file1.csv', 'file2.csv', 'file3.csv'] # 처리할 파일 목록
    with Pool(processes=3) as pool:
        results = pool.map(process_file, files)