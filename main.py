def twoSum(nums, target):
    num_index_map = {}  # 숫자와 인덱스를 매핑할 딕셔너리

    # 리스트를 순회하며 각 숫자와 인덱스를 딕셔너리에 저장
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_index_map:
            # complement(=target-num)과 매칭되는 인덱스와 현재 인덱스를 반환
            return [num_index_map[complement], i]
        # 딕셔너리에 현재 숫자와 인덱스를 저장
        num_index_map[num] = i

    # 해당 조건을 만족하는 쌍이 없을 경우 빈 리스트 반환
    return []

# 정수로 이루어진 리스트 입력 받기
nums = list(map(int, input("정수로 이루어진 리스트를 입력하세요 (예: 1 2 3 4): ").split()))

# 합을 입력 받기
target = int(input("두 정수의 합이 되는 값을 입력하세요: "))

# 함수 호출하여 결과 출력
result = twoSum(nums, target)
if result:
    print(f"두 정수의 합이 {target}이 되는 인덱스는 {result}입니다.")
else:
    print("해당 조건을 만족하는 두 정수의 쌍이 존재하지 않습니다.")