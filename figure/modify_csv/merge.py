# import os
# import pandas as pd

# def merge_with_chunks(base_folder, outfile, chunksize=10000):
#     file_count = 0
#     os.makedirs(os.path.dirname(outfile), exist_ok=True)
    
#     # 출력 파일 초기화
#     with open(outfile, 'w', encoding='utf-8-sig') as fout:
#         for root, _, files in os.walk(base_folder):
#             for file in files:
#                 if file.endswith(".csv"):
#                     csv_path = os.path.join(root, file)
#                     print(f"파일 추가 중: {csv_path}")
#                     try:
#                         # CSV를 청크 단위로 읽기
#                         for chunk in pd.read_csv(csv_path, chunksize=chunksize):
#                             # 첫 번째 파일은 헤더를 포함, 이후 파일은 제외
#                             header = file_count == 0
#                             chunk.to_csv(fout, index=False, header=header, mode='a', encoding='utf-8-sig')
#                         file_count += 1
#                     except Exception as e:
#                         print(f"파일 읽기 실패: {csv_path} - {e}")
    
#     print(f"csv가 모두 저장되었습니다: {outfile}")
#     print(f"총 결합된 파일 수: {file_count}")
                

# base_folder = "./data/processed_files_V2"
# outfile = "./data/merged_V2.csv"
# merge_with_chunks(base_folder, outfile)

# merge csv
import os
import pandas as pd

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
                

base_folder = "./data/processed_files_V3"
outfile = "./data/merged_V3.csv"
merge(base_folder, outfile)