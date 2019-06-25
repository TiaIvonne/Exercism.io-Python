class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        """return the last value in a list"""
        return self.scores[-1]

    def personal_best(self):
        """return max value in a list"""
        return max(self.scores)

    def personal_top_three(self):
        """highest score"""
        return sorted(self.scores, reverse=True)[:3]
