class Solution:
    def sortVowels(self, s: str) -> str:
        # 모음을 정의
        vowels = set("aeiouAEIOU")
        
        # s에서 모음만 추출하여 리스트에 저장
        vowel_list = [char for char in s if char in vowels]
        
        # 추출된 모음을 ASCII 값에 따라 오름차순 정렬
        vowel_list.sort()
        
        # 결과 문자열을 구성
        result = []
        vowel_index = 0 # 정렬된 모음 리스트의 인덱스
        
        # 원래 문자열 s를 순회하면서 모음 위치에 정렬된 모음을 배치
        for char in s:
            if char in vowels:
                result.append(vowel_list[vowel_index])
                vowel_index += 1
            else:
                result.append(char)
                
        return ''.join(result)