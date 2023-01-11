import numpy as np

#完走率を計算する関数
def FinishRate(result_list):
    ok_cnt = 0

    for i in result_list:
        if i == "完走":
            ok_cnt += 1

    rate = ok_cnt / len(result_list)

    return rate

def main():
    print("試行回数5回")
    #改良前
    before_result = ["完走", "失敗", "失敗", "完走", "完走"]
    print("改良前の完走率 : " + str(FinishRate(before_result)))

    #改良後
    after_result = ["完走", "完走", "完走", "完走", "完走"]
    print("改良後の完走率 : " + str(FinishRate(after_result)))

    #改良前の実験結果に"完走"を，改良後の実験結果に"失敗"を追加する
    before_result.append("完走")
    after_result.append("失敗")

    #完走率を再計算
    print("完走した結果を追加した改良前の完走率 : " + str(FinishRate(before_result)))
    print("失敗した結果を追加した改良後の完走率 : " + str(FinishRate(after_result)))


    #本文中に出てきた試行回数 15回，100回での完走率をそれぞれ計算してみる
    #追加した実験結果の削除
    del before_result[5]
    del after_result[5]

    print("試行回数15回")
    before_result_15 = before_result * 3
    after_result_15 = after_result * 3
    print("改良前の完走率 : " + str(FinishRate(before_result_15)))
    print("改良後の完走率 : " + str(FinishRate(after_result_15)))

    #改良前の実験結果に"完走"を，改良後の実験結果に"失敗"を追加する
    before_result_15.append("完走")
    after_result_15.append("失敗")

    #完走率を再計算
    print("完走した結果を追加した改良前の完走率 : " + str(FinishRate(before_result_15)))
    print("失敗した結果を追加した改良後の完走率 : " + str(FinishRate(after_result_15)))


    print("試行回数100回")
    before_result_100 = before_result * 20
    after_result_100 = after_result * 20
    print("改良前の完走率 : " + str(FinishRate(before_result_100)))
    print("改良後の完走率 : " + str(FinishRate(after_result_100)))

    #改良前の実験結果に"完走"を，改良後の実験結果に"失敗"を追加する
    before_result_100.append("完走")
    after_result_100.append("失敗")

    #完走率を再計算
    print("完完した結果を追加した改良前の完走率 : " + str(FinishRate(before_result_100)))
    print("失敗した結果を追加した改良後の完走率 : " + str(FinishRate(after_result_100)))


if __name__ == "__main__":
    main()
