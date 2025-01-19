# modify csv
import os
import json
import pandas as pd

def process(csv_path, json_path, outfolder):
    
    csv_data = pd.read_csv(csv_path)
    
    with open(json_path, 'r', encoding='utf-8') as f:
        annotation_data = json.load(f)
    
    actor_gender = annotation_data.get('actor', {}).get('actor_gender')
    actor_level = annotation_data.get('actor', {}).get('actor_level')
    motion_category2 = (
        annotation_data.get('annotations', [{}])[0].get('motion_category2')
    )


    csv_data['gender'] = actor_gender
    csv_data['level'] = actor_level
    csv_data['label'] = motion_category2
    
    # 저장경로 생성
    #경로의 하위경로 반환
    relative_path = os.path.relpath(csv_path, start=os.path.commonpath([csv_path, json_path]))
    output_filename = relative_path.replace(os.sep, "_")
    base_output_path = os.path.join(outfolder, output_filename)
    output_path = base_output_path
    counter = 1
    
    while os.path.exists(output_path):
        output_path = f"{base_output_path}_{counter}.csv"
        counter +=1
    
    # 출력 폴더 생성성
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    #저장
    csv_data.to_csv(output_path, index=False, encoding='utf-8-sig')
    
    # 경로 출력
    print(f"CSV 파일 경로: {csv_path}")
    print(f"JSON 파일 경로: {json_path}")
    print(f"수정된 csv저장: {output_path}")
    
def process_all_files(base_folder, outfolder):
    for root, _, files in os.walk(base_folder):
        if '정상' in root and 'camera0' in root and 'local_keypoints' in root:
            for file in files:
                if file.endswith(".csv"):
                    csv_path = os.path.join(root, file)
                    # json파일 csv 이름에 맞게 탐색
                    json_dir = root.replace('local_keypoints','video') 
                    json_path = os.path.join(json_dir, 'annotation.json')
                    
                    # json 에서 video_name검증
                    if os.path.exists(json_path):
                        with open(json_path, 'r', encoding = 'utf-8') as f:
                            annotation_data = json.load(f)
                            
                        video_name = annotation_data.get("video_name", "").replace(".avi", ".csv")
                        if video_name == file:
                            process(csv_path, json_path, outfolder)
                        
# 기준 폴더 설정
base_folder = "./data"  # 루트 폴더
outfolder = "./data/processed_files"  # 수정된 CSV 파일이 저장될 폴더
process_all_files(base_folder, outfolder)

