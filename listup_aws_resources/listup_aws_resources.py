import os
import json
import pandas as pd
import boto3
from datetime import datetime, timezone
import argparse

# ① 개별 리소스 모듈 임포트
from resources.ec2 import get_raw_data as ec2_raw, get_filtered_data as ec2_filtered
from resources.vpc import get_raw_data as vpc_raw, get_filtered_data as vpc_filtered
from resources.rds import get_raw_data as rds_raw, get_filtered_data as rds_filtered
from resources.eks import get_raw_data as eks_raw, get_filtered_data as eks_filtered
from resources.subnets import get_raw_data as subnets_raw, get_filtered_data as subnets_filtered
# 필요 시 다른 모듈도 동일 형태로 import (secrets_manager, ebs, elb 등)

def main():
    """
    명령줄 인자로 넘긴 리전 목록을 순회하며, 각 리전에 대해
    여러 리소스를 수집하여 JSON+Excel로 저장
    """

    # 1) argparse로 리전 인자 처리
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--region',
        dest='regions',
        nargs='+',  # 스페이스로 구분된 여러 리전을 받을 수 있음
        default=['ap-northeast-2'],
        help='조회할 AWS 리전명 (여러 개 가능). 예: --region ap-northeast-2 us-west-2'
    )
    args = parser.parse_args()
    regions = args.regions

    # 2) 날짜/시간 표기
    timestamp = datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')

    # 3) 결과 저장 폴더 생성
    current_dir = os.path.dirname(__file__)
    data_dir = os.path.join(current_dir, 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Raw JSON 결과를 담을 딕셔너리 (리전별로 묶어 보관)
    all_raw_data = {}

    # Excel 파일 경로
    excel_path = os.path.join(data_dir, f'aws_resources_{timestamp}.xlsx')
    writer = pd.ExcelWriter(excel_path, engine='openpyxl')

    # 리전별로 순회
    for region in regions:
        print(f"\n=== Collecting resources in region: {region} ===")

        # 리전을 명시하여 세션 생성 (필요시 프로필도 추가)
        session = boto3.Session(region_name=region)

        # 리전에 해당하는 raw + filtered 데이터를 담을 딕셔너리
        region_raw_data = {}

        # ---------- EC2 ----------
        ec2_data_raw = ec2_raw(session, region)
        ec2_data_filtered = ec2_filtered(ec2_data_raw)
        region_raw_data['EC2'] = ec2_data_raw

        # Excel 시트명에 리전 포함 (중복 방지)
        # 예) "EC2_ap-northeast-2"
        if not ec2_data_filtered.empty:
            sheet_name = f"EC2_{region}"[:31]  # 시트명 31자 제한
            ec2_data_filtered.to_excel(writer, sheet_name=sheet_name, index=False)

        # ---------- VPC ----------
        vpc_data_raw = vpc_raw(session, region)
        vpc_data_filtered = vpc_filtered(vpc_data_raw)
        region_raw_data['VPC'] = vpc_data_raw
        if not vpc_data_filtered.empty:
            sheet_name = f"VPC_{region}"[:31]
            vpc_data_filtered.to_excel(writer, sheet_name=sheet_name, index=False)

        # ---------- RDS ----------
        rds_data_raw = rds_raw(session, region)
        rds_data_filtered = rds_filtered(rds_data_raw)
        region_raw_data['RDS'] = rds_data_raw
        if not rds_data_filtered.empty:
            sheet_name = f"RDS_{region}"[:31]
            rds_data_filtered.to_excel(writer, sheet_name=sheet_name, index=False)

        # ---------- EKS ----------
        eks_data_raw = eks_raw(session, region)
        eks_data_filtered = eks_filtered(eks_data_raw)
        region_raw_data['EKS'] = eks_data_raw
        if not eks_data_filtered.empty:
            sheet_name = f"EKS_{region}"[:31]
            eks_data_filtered.to_excel(writer, sheet_name=sheet_name, index=False)

        # ---------- Subnets ----------
        subnets_data_raw = subnets_raw(session, region)
        subnets_data_filtered = subnets_filtered(subnets_data_raw)
        region_raw_data['Subnets'] = subnets_data_raw
        if not subnets_data_filtered.empty:
            sheet_name = f"Subnets_{region}"[:31]
            subnets_data_filtered.to_excel(writer, sheet_name=sheet_name, index=False)

        # TODO: 다른 서비스 (EIP, EBS, S3 등)도 동일 패턴으로 추가

        # 리전별 raw data를 상위 딕셔너리에 저장
        # 예: all_raw_data['ap-northeast-2'] = {'EC2': ..., 'VPC': ...}
        all_raw_data[region] = region_raw_data

    # Excel 저장
    writer.close()
    print(f"[Excel] {excel_path} 생성 완료")

    # Raw JSON 결과 저장
    json_path = os.path.join(data_dir, f'aws_resources_raw_{timestamp}.json')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(all_raw_data, f, ensure_ascii=False, indent=2)
    print(f"[JSON] {json_path} 생성 완료")


if __name__ == '__main__':
    main()
