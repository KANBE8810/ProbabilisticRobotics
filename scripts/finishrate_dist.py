import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axisartist.axislines import SubplotZero

#ベイズの定理
class Bayes_Theorem:
    def __init__(self):
        #離散化した完走率 t
        self.t = []
        for i in range(101):
            self.t.append(i / 100)

    #事前分布推移
    def Prior_distribution(self):
        return np.full(101, 1/101)

    #事後分布
    def Posterior_distribution(self, P_at, Prior_dist):
        return  P_at * Prior_dist / sum(P_at * Prior_dist)

    #p(a|t)
    def P_at(self, a, FinishRate):
        if a == "完走":
            return FinishRate
        elif a == "失敗":
            return np.ones(101) - FinishRate

    #試行ごとの分布を計算
    def Calc_distribution(self, Trial_list, Posterior_dist_list):
        prior_dist = self.Prior_distribution() 
        Posterior_dist_list.append(prior_dist) #プロット用に保存

        for i, trial in enumerate(Trial_list):
            P_at = self.P_at(trial, self.t)
            posterior_dist = self.Posterior_distribution(P_at, prior_dist)
            prior_dist = posterior_dist #i回目までの試行を反映したP(t|a_1:t)を次の事前分布とみなす
            Posterior_dist_list.append(posterior_dist) #プロット用保存

#グラフのプロット
class Plot_graph:
    def __init__(self):
        self.Posterior_dist_list = []
        self.axies_list = [0]*6

    def Plot(self, x, graph_title_list, graph_name):
        fig = plt.figure(figsize=(14, 10))

        for i in range(6):
            self.axies_list[i] = SubplotZero(fig, 2, 3, i+1)
            fig.add_subplot(self.axies_list[i])
            for direction in ["right", "top"]:
                self.axies_list[i].axis[direction].set_visible(False)
            for direction in ["left",  "bottom"]:
                self.axies_list[i].axis[direction].set_axisline_style("-|>")

            y = self.Posterior_dist_list[i]
            self.axies_list[i].plot(x, y)
            plt.grid()
            self.axies_list[i].set_title(graph_title_list[i], y = -0.15)
            self.axies_list[i].set_xlabel('t')
            self.axies_list[i].set_ylabel('Probability')
            self.axies_list[i].set_xlim(0, 1)
            self.axies_list[i].set_ylim(0, 0.09)

        fig.tight_layout()
        fig.savefig("../images/" + graph_name + ".png", bbox_inches="tight")


def main():
    bayes = Bayes_Theorem()

    #改良前
    before_result = ["完走", "失敗", "失敗", "完走", "完走"]
    pg1 = Plot_graph()
    #試行ごとに計算
    bayes.Calc_distribution(before_result, pg1.Posterior_dist_list)
    #試行ごとのtの分布をプロット
    Title_list = ["Before experiment", "1st attempt (success)", "2nd attempt (Fail)", "3rd attempt (Fail)", "4th attempt (success)", "5th attempt (sucess)"]
    pg1.Plot(bayes.t, Title_list, "改良前のtの分布の推移")

    #改良後
    after_result = ["完走", "完走", "完走", "完走", "完走"]
    pg2 = Plot_graph()
    #試行ごとに計算
    bayes.Calc_distribution(after_result, pg2.Posterior_dist_list)
    #試行ごとのtの分布をプロット
    Title_list = ["Before experiment", "1st attempt (success)", "2nd attempt (success)", "3rd attempt (success)", "4th attempt (success)", "5th attempt (success)"]
    pg2.Plot(bayes.t, Title_list, "改良後のtの分布の推移")


if __name__ == "__main__":
    main()