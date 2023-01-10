import numpy as np
import matplotlib.pyplot as plt

#完走率を計算する関数
def FinishRate(result_list):
    ok_cnt = 0

    for i in result_list:
        if i == "完走":
            ok_cnt += 1
    rate = ok_cnt / len(result_list)
    return rate

def main():
    #改良前
    before_result = ["完走", "失敗", "失敗", "完走", "完走"]
    print("改良前の完走率 : " + str(FinishRate(before_result)))

    #改良後
    after_result = ["完走", "完走", "完走", "完走", "完走"]
    print("改良後の完走率 : " + str(FinishRate(after_result)))

if __name__ == "__main__":
	main()