class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        true, false, answer, start = 0, 0, 0, 0
        n = len(answerKey)

        for i in range(n):
            if answerKey[i] == "T":
                true += 1
            else:
                false += 1

            while min(true, false) > k:
                if answerKey[start] == "T":
                    true -= 1
                else:
                    false -= 1
                
                start += 1
                
            answer = max(answer, true + false)

        return answer