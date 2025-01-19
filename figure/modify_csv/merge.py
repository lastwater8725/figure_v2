# merge csv
import os
import pandas as pd

# 1. csv 확인하기
# 2. csv 합치기

def merge(base_folder, outfile):
    csv_list = []
    file_count = 0
    
    for root, _, files in os.walk(base_folder):
        for file in files:
            if file.endswith(".csv"):
                csv_path = os.path.join(root, file)
                print(f"파일 추가 중: {csv_path}")
                try:
                    df = pd.read_csv(csv_path)
                    csv_list.append(df)
                    file_count += 1
                except Exception as e:
                    print(f"파일 읽기 실패: {csv_path} - {e}")
                
    if csv_list:
        merged_df = pd.concat(csv_list, ignore_index = True)
        
        os.makedirs(os.path.dirname(outfile), exist_ok=True)
        
        merged_df.to_csv(outfile, index=False, encoding='utf-8-sig')
        print(f"csv가 모두 저장되었습니다: {outfile}")
        print(f"총 결합된 파일 수: {file_count}")
    else:
        print("결합할 CSV 파일이 없습니다.")   
                

base_folder = "./data/processed_files"
outfile = "./data/merged.csv"
merge(base_folder, outfile)