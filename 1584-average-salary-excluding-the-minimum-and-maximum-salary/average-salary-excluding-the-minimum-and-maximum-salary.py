class Solution:
    def average(self, salary: List[int]) -> float:

        min_salary = salary.remove(min(salary))
        max_salary = salary.remove(max(salary))

        div_num = len(salary)
        res = sum(salary) / div_num
        return float(res)
        